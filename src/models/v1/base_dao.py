from src.utils.sgql_utils import GraphQLEndpoint
from src.utils.errors import GraphQLError
from sgqlc.operation import Operation
from src.graphql.schema import Query, Mutation
import src.graphql.schema as graphql_schema
import re
import json

# TODO
# instead of creating recursive helper functions to validate the structure of mutations, use something like marshmallow

class BaseGraphQL:
    """
    Base GraphQL data access object. Implements querying and creating nodes in a generic way.
    Inheriting children are expected to enrich these methods to tailor to their specific type.
    However, this base class will provide most of the utilities

    Parameters
    ----------
    model: str
       The name of the model, must be a valid model in the schema.py 
    **kwargs
       key-value pairs that will be set as object attributes

    Note
    ----
    If the model is not valid the BaseGraphQL will raise a ValueError
    """
    def __init__(self, model, **kwargs):
        # get endpoint from singleton
        self.endpoint = GraphQLEndpoint()
        # check if the model specified exists in the schema
        if not hasattr(graphql_schema, model):
            raise ValueError(f"model {model} does not exist") 
        self.model = getattr(graphql_schema, model)

        # set the attributes from **kwargs
        for key in kwargs:
           setattr(self, key, kwargs[key])

    def mutate(self,mutation_values):
        """
        High level function to mutate data in graphql using sgql operations in a generic way.
        Sub-classes can use this function within their own create functions to allow for a
        way of implemeting easily adaptable mutate queries. In addition this method is built in
        with an automated roll back system in case of failure of one of the transactions

        Parameters
        ----------       
        mutation_values: list
            A list containing the desired mutations and values in the order to be executed
            [
                {
                    "CreateSurvey": {
                        "values": {
                            "uniqueName": "test_sur_1"
                        },
                        "fields": [
                            "uid"
                        ]
                    }
                },
                {
                    "CreateTemplate": {
                        "values": [
                            "surveyTemplate": "{'hello': 'hi'}"
                            "evalese": "test evalese"
                        ],
                        "fields": [
                            "uid"
                        ]
                    }
                }, 
                {
                    "AddSurveyLatest" : {
                        "values": {
                            "from" : {
                                "type": "_SurveyInput"
                                "fields: {
                                    {
                                        "uid": "CreateSurvey.uid"
                                    }
                                }
                            },
                            "to" : {
                                "type": "_SurveyInput
                                "fields": {
                                    {
                                        "uid": {
                                            "reference": "CreateTemplate.uid"
                                        }
                                    }
                                } 
                            }
                        }
                        "fields": [
                            {
                                "from" : {
                                    "type": "_SurveyInput"
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]

        """
        validated_mutations = self._validate_mutations(mutation_values)
        mutation_results = {}
        for mutation_name in validated_mutations:
            converted_mutation_name = self._convert_from_sgql_to_graphql(mutation_name, True)
            mutation_operation = Operation(Mutation)
            mutation_operation = self._build_mutation(
                mutation_operation,
                mutation_name,
                validated_mutations[mutation_name],
                mutation_results
            )
            data = self.endpoint.query(mutation_operation)
            if data.get("exception") is not None:
                # TODO: here is where the roll back function would be implemented
                raise GraphQLError(
                    f"An error has occured for mutation {converted_mutation_name}. " +
                    "See the following exceptions " + str(data)   
                )
            mutation_results[converted_mutation_name] = data["data"][converted_mutation_name]
        return mutation_results

    def _build_mutation(self, operation, mutation_name, mutation, mutation_results):
        """
        Helper function to build mutation

        Parameters
        ----------
        operation: sgqlc.operation.Operation
           the sgqlc mutation operation
        values: dict
           the values for the mutation
        mutation_results: dict
           previous mutation results needed for reference values
        """
        mutation_values = mutation.get("values")
        mutation_fields = mutation.get("fields")
        built_mutation_values = {}
        for value in mutation_values:
            built_mutation_values[value] = self.__build_mutation_values(mutation_values[value], mutation_results)
        mutation_operation = getattr(operation, mutation_name)
        mutation_operation(**built_mutation_values)
        if mutation_fields is not None:
            self._build_query(mutation_operation, mutation_fields)
        return operation

    def __build_mutation_values(self,value, mutation_results):
        if isinstance(value, dict):
            if value.get("reference") is not None:
                # get the reference value from the previous mutation
                # we don't need to worry about validating anything since 
                # we already validated the mutation to be plausible before even executing it
                reference_path = value["reference"].split(".")
                reference_type = reference_path[0]
                converted_reference_type = self._convert_from_sgql_to_graphql(reference_type, True)
                reference_result = mutation_results[converted_reference_type]
                for i in reference_path[1:]:
                    converted_i = self._convert_from_sgql_to_graphql(i)
                    reference_result = reference_result[converted_i]
                return reference_result
            else:
                sub_values = value.get("values")
                sub_values_built = {}
                for sub in sub_values:
                    sub_values_built[sub] = self.__build_mutation_values(sub_values[sub], mutation_results)
                return sub_values_built
        return value





        
    def _validate_mutations(self, mutations):
        """
        Helper function used to validate the structure and value of issued
        mutations. If the mutations issued are invalid a value error will be raised
        """

        # validated mutations will be stored here with their transformed names
        # using a dioctionary instead of a list because we can only issue one type of mutation in a mutation
        validated_mutations = {}
        count = 0
        for mutation in mutations:
            # validate index is a dictionary
            if not isinstance(mutation, dict):
                type_name = type(mutation).__name__
                msg = (
                    "All mutations must be defined in a dictionary. " +
                    f"Found {type_name} at index {count}"
                )
                raise ValueError(msg)
            # check that this dictionary only has one key which refers to the mutation type
            mutation_keys = list(mutation.keys())
            if not len(list(mutation_keys)) == 1:
                num_keys = len(list(mutation.keys()))
                msg = (
                    "All mutation definitions must be a dictionary " +
                    "with only one top level key which is the mutation type. " +
                    f"Found {num_keys} at index {count}"
                )
                raise ValueError(msg)
            
            # top level structure of mutation is validated at this point
            # pull the name of the mutation, check it exists then convert it's name and check if its unique
            
            mutation_name = mutation_keys[0]
            converted_mutation_name = self._convert_from_graphql_to_sgql(mutation_name)
            mutation_definition = mutation[mutation_name]
            if "Add" in mutation_name or "Remove" in mutation_name:
                sgql_mutation_name = "_" + mutation_name + "Payload"
            elif "Create" in mutation_name:
                sgql_mutation_name = mutation_name.split("Create")[1]
            elif "Update" in mutation_name:
                sgql_mutation_name = mutation_name.split("Update")[1]
            elif "Delete" in mutation_name:
                sgql_mutation_name = mutation_name.split("Delete")[1] 
            else:
                sgql_mutation_name = mutation_name

            if not hasattr(graphql_schema, sgql_mutation_name):
                msg = f"Mutation {sgql_mutation_name} at index {count} is not a valid mutation"
                raise ValueError(msg)


            if validated_mutations.get(converted_mutation_name) is not None:
                msg = f"Mutation {mutation_name} at index {count} is not unique"
                raise ValueError(msg)

            # Now we go through the guts of the mutations
            # first we will obviously make sure that the structure exists
            # a mutation must have the fields it wants returned and the values to mutate

            mutation_values = mutation_definition.get("values")
            mutation_fields = mutation_definition.get("fields")
            # make sure that values entry exists
            if mutation_values is None:
                msg = (
                    f"Values to mutate have not been defined for mutation {mutation_name} " +
                    f"at index {count}"
                )
                raise ValueError(msg)
            # make sure that it is a list
            elif not isinstance(mutation_values, dict):
                type_name = type(mutation_values)
                msg = (
                    f"Values to mutate must be of type dict, found {type_name} on mutation {mutation_name} " +
                    f"at index {count}"
                )
                raise ValueError(msg)
            
            # validate and transform values
            mutation_sgql_class =  getattr(graphql_schema, sgql_mutation_name)
            converted_mutation_values = self._validate_and_transform_values(
                mutation_values,
                mutation_sgql_class,
                validated_mutations,
                mutation_name
            )
            
            validated_mutations[converted_mutation_name] = {
                "values": converted_mutation_values
            }
            # fields may not exist in the definition 
            if mutation_fields is not None:
                if isinstance(mutation_fields, list):
                    converted_mutations_fields = self._validate_and_transform_fields(
                        mutation_fields,
                        mutation_sgql_class
                    )
                    validated_mutations[converted_mutation_name]["fields"] = converted_mutations_fields
                else:
                    type_name = type(mutation_fields)
                    msg = (
                        f"Fields on which to return after a mutation must be of type list, found {type_name}"
                    )
                    raise ValueError(msg)
            count += 1
        return validated_mutations
    
    def _validate_and_transform_values(self, values, mutation_type, validated_mutations, mutation_name, prefixes = []):
        """
        Recursive helper function used to validate the mutation values on an individual mutation

        Parameters
        ----------
        values: dict
            the dictionary of the values
            i.e.
            {
                "from" : {
                    "type": "_SurveyInput"
                    "values": : {
                        "uid": {
                            "reference": "CreateSurvey.uid"
                        }
                    }
                },
                "to" : {
                    "type": "_SurveyInput
                    "values": {
                        "uid": {
                            "reference": "CreateSurvey.uid"
                        }
                        
                    } 
                }
            }
        mutation_type: sgqlc.type.Type
            the mutation type
        validated_mutations: dict
            a dictionary of pre-validated mutations
        prefixes: list, optional
            used to help generate more clearer error messages 
        """
        if not isinstance(values, dict) or not bool(dict):
            raise TypeError("values must be a dictionary with atleast one key")


        validated_values = {}
        
        for value in values:
            # convert the value name from graphql format to sgql format
            converted_value_name = self._convert_from_graphql_to_sgql(value)

            # check if it already exists
            if validated_values.get(converted_value_name) is not None:
                msg = f"value {value} already exists"
                msg = self.__generate_uniqueness_err_message(msg, prefixes)
                raise ValueError(msg)

            value_definition = values[value]
            if isinstance(value_definition, (str, int, float)):
                validated_values[converted_value_name] = value_definition
            # value definition is a string, check if it is refrencing a field from a validated mutation
            elif isinstance(value_definition, dict):
                # reference value 
                if value_definition.get("reference") is not None:
                    # make sure the reference is a string
                    value_definition_reference = value_definition.get("reference")
                    if not isinstance(value_definition_reference, str):
                        msg = f"reference is not of type string on value {value}"
                        msg = self.__generate_uniqueness_err_message(msg, prefixes)
                        raise ValueError(msg)
                    
                    # split on the dot which denotes a path
                    value_definition_reference_path = value_definition_reference.split(".")
                
                    # the minimum length of the path should be two, if this is not the case the path is not valid
                    if len(value_definition_reference_path) < 2:
                        msg = f"The defined path {value_definition_reference} for reference value {value} is not valid"
                        msg = self.__generate_uniqueness_err_message(msg, prefixes)
                        raise ValueError(msg)
                    
                    # path structure is valid, mutation type should be the first index
                    value_definition_reference_type = value_definition_reference_path[0]
                    # fist lets make sure this type even exists within the schema
                    if "Add" in value_definition_reference_type or "Remove" in value_definition_reference_type:
                        sgql_value_definition_reference_type = "_" + value_definition_reference_type + "Payload"
                    elif "Create" in value_definition_reference_type:
                        sgql_value_definition_reference_type = value_definition_reference_type.split("Create")[1]
                    elif "Update" in value_definition_reference_type:
                        sgql_value_definition_reference_type = value_definition_reference_type.split("Update")[1]
                    elif "Delete" in value_definition_reference_type:
                        sgql_value_definition_reference_type = value_definition_reference_type.split("Delete")[1] 
                    else:
                        sgql_value_definition_reference_type = value_definition_reference_type

                    if not hasattr(graphql_schema, sgql_value_definition_reference_type):
                        msg = f"reference Type {value_definition_reference_type} for reference value {value} is not a valid type"
                        msg = self.__generate_uniqueness_err_message(msg, prefixes)
                        raise ValueError(msg)
                    # then we want to convert the paths to sgql form 
                    converted_value_definition_reference_path = [ self._convert_from_graphql_to_sgql(i) for i in value_definition_reference_path]
                    converted_value_definition_reference_type = converted_value_definition_reference_path[0]

                    # check if this even exists in the mutation sequence
                    if validated_mutations.get(converted_value_definition_reference_type) is None:
                        msg = (
                            f"Valid reference type {value_definition_reference_type} for value {value}. " +
                            f"However, this does not exit prior to the mutation {mutation_name} in the mutation sequence"
                        )
                        msg = self.__generate_uniqueness_err_message(msg, prefixes)
                        raise ValueError(msg)
                    # reference type is now validated, we need to validate the reference fields

                    # check if level one field exists in the fields
                    validated_mutation_fields = validated_mutations[converted_value_definition_reference_type].get("fields")

                    # TODO can only check if field is actually returned on first level only 
                    if validated_mutation_fields is not None:
                        exists = False
                        index = 0
                        while not exists and index < len(validated_mutation_fields):
                            field = validated_mutation_fields[index]
                            # check if key name matches the selected field
                            if isinstance(field, dict):
                                exists = list(field.keys())[0] == converted_value_definition_reference_path[1]
                            else:
                                exists = field == converted_value_definition_reference_path[1]
                        if exists == False:
                            msg = (
                                f"Reference value {value} is not valid. " +
                                f"Field {value_definition_reference_path[1]} of type {value_definition_reference_type} is specified. " +
                                "However, this is not specified to be returned from the mutation sequence"
                            )
                            msg = self.__generate_uniqueness_err_message(msg, prefixes)
                            raise ValueError(msg)
                    # first get the reference type as the pointer 
                    # then loop over the paths each time making sure the field exists on the parent
                    if "Add" in value_definition_reference_type or "Remove" in value_definition_reference_type:
                        sgql_value_definition_reference_type = "_" + value_definition_reference_type + "Payload"
                    elif "Create" in value_definition_reference_type:
                        sgql_value_definition_reference_type = value_definition_reference_type.split("Create")[1]
                    elif "Update" in value_definition_reference_type:
                        sgql_value_definition_reference_type = value_definition_reference_type.split("Update")[1]
                    elif "Delete" in value_definition_reference_type:
                        sgql_value_definition_reference_type = value_definition_reference_type.split("Delete")[1] 
                    else:
                        sgql_value_definition_reference_type = value_definition_reference_type
                    field_pointer = getattr(graphql_schema, sgql_value_definition_reference_type)
                    for field_index in range(1,len(value_definition_reference_path)):
                        conveted_field = converted_value_definition_reference_path[field_index]
                        unconverted_field = value_definition_reference_path[field_index]
                        if not hasattr(field_pointer, conveted_field):
                            msg = (
                                f"reference value {value} is not valid. "+
                                f"field {unconverted_field} does not exist on reference type {value_definition_type}"
                            )
                            msg = self.__generate_uniqueness_err_message(msg, prefixes)
                            raise ValueError(msg)
                        # set pointer to new parent
                        field_pointer = getattr(field_pointer, conveted_field)
                    
                    # reference value is validated

                    converted_value_definition_reference = {
                        "reference": ".".join(converted_value_definition_reference_path)
                    }
                    
                    validated_values[converted_value_name] = converted_value_definition_reference
                else:
                    value_definition_type = value_definition.get("type")
                    value_definition_values = value_definition.get("values")

                    if value_definition_type is None or not isinstance(value_definition_type, str):
                        msg = f"Type for nested value in value {value} was not defined or is not a string"
                        msg = self.__generate_uniqueness_err_message(msg, prefixes)
                        raise ValueError(msg)
                    
                    # check if the type is a valid type 
                    try:
                        value_definition_type = getattr(graphql_schema, value_definition_type)
                    except AttributeError:
                        msg = f"Type {value_definition_type} for nested value in value {value} does not exist"
                        msg = self.__generate_uniqueness_err_message(msg, prefixes)
                        raise ValueError(msg)

                    if value_definition_values is None:
                        msg = f"Type for nested values in value {value} were specified but not the nested values"
                        msg = self.__generate_uniqueness_err_message(msg, prefixes)
                        raise ValueError(msg)
                    elif not isinstance(value_definition_values, dict):
                        type_name = type(value_definition_values).__name__
                        msg = f"Expected type dict for nested values on values {value}, found type {type_name}"
                        msg = self.__generate_uniqueness_err_message(msg, prefixes)
                        raise ValueError(msg)
                    # recurse on sub_value
                    new_prefixes = prefixes
                    new_prefixes.append(value)
                    converted_sub_values = self._validate_and_transform_values(
                        value_definition_values, 
                        value_definition_type, 
                        validated_mutations,
                        mutation_name,
                        new_prefixes
                    )
                    # create the converted value dictionary
                    converted_value = {
                        "type": value_definition_type,
                        "values": converted_sub_values
                    }
                    # add to the validated values
                    validated_values[converted_value_name] = converted_value
            else:
                type_name = type(value_definition).__name__
                msg = f"Value definition for value {value} is not valid, expected dict or str, recieved {type_name}"
        return validated_values
          
    def query(self, selected_fields, top_level_selectors = None, top_level_filters = None, filters_on_fields = None):
        """
        High level function to fetch data from graphql using sgql operations in a generic way.
        Sub-classes can use this function within their own query functions to allow for an easy
        way of implementing easily adaptable custom queries
        
        Parameters
        ----------
        selected_fields: dict
            A dictionary conatining the selected fields devided by GraphQL type
            i.e.
            [
                "uid",
                "uniqueName",
                {
                    "latest": {
                        "type": "SurveyTemplate",
                        "fields": [
                            "surveyMetrics" : {
                                "type": "SurveyMetrics",
                                "fields": [
                                    "uid"
                                ]
                            }
                        ]
                    }
                }
            ]
        top_level_selectors:  dict
           A dictionary containing the selectors for the top level query
           i.e.
           {
               "uid": "fdfsdfdsfsdfdsfdsf"
           }
           mutually exclusive to top_level_filters
        top_level_filters: 
           A dictionary containing the filters for the top level query
           i.e. 
           {
               "created_at_lt": {
                   "formatted" : "2019-08-21T23:54:39.868Z"
               }
           }
           mutually exclusive to top_level_selectors
        filters_on_fields: : dict, optional
            A dictionary of filters that can be applied on subfields of the query
            i.e.
            {
                "versions":{
                    "created_at_lt": {
                        "formatted": "2019-08-21T23:54:39.868Z"
                    }
                }
            }
        """
        if top_level_filters is not None and top_level_selectors is not None:
            raise ValueError("top_level_filters and top_level_selectots are mutually exclusive")

        validated_selected_fields = self._validate_and_transform_fields(
                                        selected_fields, type_ = self.model
                                    )

        query_op = Operation(Query)
        top_level_model_name = self._convert_from_graphql_to_sgql(self.model.__name__)
        top_level_query_obj = getattr(query_op, top_level_model_name)

        # if the selectors exist
        if top_level_selectors is not None:
            if not bool(top_level_selectors):
                raise ValueError("Empty dictionary provided for top_level_selectors, expecting at least one field")
            # get the query sub-type and destruct the parameters from the top_level_selectors
            top_level_query_obj(**top_level_selectors)
        
        # if the filters exist
        elif top_level_filters is not None:
            top_level_query_obj(filter = top_level_filters)

        self._build_query(top_level_query_obj, validated_selected_fields, filters_on_fields)

        print(query_op)
        data = self.endpoint.query(query_op)

        if data.get("exception") is not None:
            return GraphQLError(
                "An exception has occured while fetching data \n" +
                json.dumps(str(data))
            )
        else:
            return data["data"]
       
    
    def _build_query(self, operation, fields, filters = None):
        for field in fields:
            field_name = field
            if isinstance(field, dict):
                field_name = list(field.keys())[0]
            sub_operation = getattr(operation, field_name)
            if filters is not None and filters.get(field_name) is not None:
                sub_operation(filter = filters.get(field_name))
            else:
                sub_operation()
            if isinstance(field, dict):
                sub_field_fields = field[field_name]["fields"]
                self._build_query(sub_operation, sub_field_fields, filters) 

    def _convert_from_sgql_to_graphql(self, field, first_letter_capital = False):
        "helper function to convert from sgql field names to graphQL field names"
        if not isinstance(field, str):
            type_name = type(field).__name__
            raise TypeError(f"field must be of type str, found {type_name}")
        elif field == "" or field.strip(" ") == "":
            raise ValueError("field must not be empty string")
        # strip the last underscore, special fields like from_
        field = field.rstrip("_")
        field_list = field.split("_")
        if len(field_list) == 1:
            if field == "and_":
                return "AND"
            elif field == "or_":
                return "OR"
            return field_list[0]
        graphql_field_name = field_list[0]
        if first_letter_capital:
            graphql_field_name = graphql_field_name[0].upper() + graphql_field_name[1:]
        # start from the second index 
        for name_component in field_list[1:]:
            # first letter of each new name component after the first is capital
            graphql_field_name += name_component[0].upper() + name_component[1:]
        return graphql_field_name
    
    def _convert_from_graphql_to_sgql(self, field):
        "helper function to convert from graphQL field names to sgql field names"
        if not isinstance(field, str):
            type_name = type(field).__name__
            raise TypeError(f"field must be of type str, found {type_name}")
        elif field == "" or field.strip(" ") == "":
            raise ValueError("field must not be empty string")
        # split name by capital letters
        field_list = re.findall("[a-zA-Z][^A-Z]*", field)
        
        if len(field_list) == 1:
            # special case 
            if field == "from":
                return "from_"
            elif field == "AND":
                return "and_"
            elif field == "OR":
                return "or_"
            return field_list[0].lower()
        # each name component has an underscore between them 
        sgql_field_name = "_".join(field_list)
        return sgql_field_name.lower()

    
    def _validate_and_transform_fields(self, fields, type_,  prefixes = []):
        """
        Recursive helper function to ensure selected fields are unique when querying GraphQL type

        Parameters
        ----------
        fields: list
            the list of the selected fields
        type_: sgql.types.Type
            the sgql type
        prefixes: list
            used in the recursion to denote path 
        
        Raises
        -------
        ValueError:
           Either the structure the the fields list is not correct or there is a duplicated field
        """
        if not isinstance(fields, list):
            raise TypeError("fields must be a list")
        field_dict = {}
        count = 0
        new_fields_array = []
        for field in fields:
            # if there is a nested field which will be a dictionary
            if isinstance(field, dict):
                # validate that the dictionary only has two keys 
                number_of_items = len(list(field.keys()))
                if number_of_items != 1:
                    msg = self.__generate_uniqueness_err_message( 
                        f"Nested fields must be a dictionary with only 1 key {number_of_items}",
                        prefixes,
                        count
                    )
                    raise ValueError(msg)
                
                # get the key from the dictionary which is the field name 
                field_name = tuple(field.keys())[0]
                # get the field definition
                field_definition = field[field_name]
                # convert the field name into the sgql format
                converted_field_name = self._convert_from_graphql_to_sgql(field_name)

                if not hasattr(type_, converted_field_name):
                    msg = self.__generate_uniqueness_err_message(
                        f"field {field_name} does not exist on type {type_}",
                        prefixes,
                        count
                    )
                    raise ValueError(msg)
                # instatiate the deserialized field 
                converted_field = {converted_field_name: {}}
                
                if field_definition.get("type") is None:
                    msg = self.__generate_uniqueness_err_message(
                        f"Nested fields must have the two keys 'type' and 'fields'. 'type' is not present for field {field_name}",
                        prefixes,
                        count
                    )
                    raise ValueError(msg)
                # ensure that the type is a string
                elif not isinstance(field_definition["type"], str):
                    type_name = type(field_definition["type"]).__name__
                    msg = self.__generate_uniqueness_err_message(
                        f"value for type must be str, recieved {type_name} for field {field_name}",
                        prefixes,
                        count
                    )
                    raise ValueError(msg)
                # validate the type of the field
                elif not hasattr(graphql_schema, field_definition["type"]):
                    invalid_type = field_definition["type"]
                    msg = self.__generate_uniqueness_err_message(
                        f"type {invalid_type} is not a valid type, field {field_name}",
                        prefixes,
                        count
                    )
                # type is validated, add the type class to the converted field
                else:
                    converted_field[converted_field_name]["type"] = getattr(graphql_schema, field_definition["type"])


                if field_definition.get("fields") is None:
                    msg = self.__generate_uniqueness_err_message(
                        f"Nested fields must have the two keys 'type' and 'fields'. 'fields' is not present for field {field_name}",
                        prefixes,
                        count
                    )
                    raise ValueError(msg)
                # make sure fields is of type list
                elif not isinstance(field_definition["fields"], list):
                    type_name = type(field_definition["fields"]).__name__
                    msg = self.__generate_uniqueness_err_message(
                        f"value for fields must be a list, recieved {type_name} for field {field_name}",
                        prefixes,
                        count
                    )
                    raise ValueError(msg)

                # field must be unique
                if field_dict.get(field_name) is not None:
                    msg  = self.__generate_uniqueness_err_message(
                        f"Duplicate field {field_name} found",
                        prefixes,
                        count
                    )
                    raise ValueError(msg)
                # field is unique, add it to the dict
                else: 
                    field_dict[field_name] = 1
        
                # recurse on subfields and add to the parent 'fields' key on return
                new_prefix = prefixes
                new_prefix.append(field_name)
                converted_field[converted_field_name]["fields"] = self._validate_and_transform_fields( 
                    field_definition["fields"],
                    type_= converted_field[converted_field_name]["type"],
                    prefixes= new_prefix
                )

                new_fields_array.append(converted_field)

            else:
                # we have checked if the field is a dictionary which means it's nested 
                # hence if the field is not a string it must be invalid
                # lists are invalid because they will be contained in dictionaries (always one level deeper then the loop)
                if not isinstance(field, str):
                    type_name = type(field).__name__
                    msg = self.__generate_uniqueness_err_message(
                        f"All items must be of type string, dict found {type_name}",
                        prefixes,
                        count
                    )
                    raise ValueError

                # field must be unique 
                if field_dict.get(field) is not None:
                    msg = self.__generate_uniqueness_err_message(
                        f"Duplicate field {field} found",
                        prefixes,
                        count
                    )
                    raise ValueError(msg)

                if not hasattr(type_, field):
                    msg = self.__generate_uniqueness_err_message(
                        f"field {field} does not exist on type {type_}",
                        prefixes,
                        count
                    )
                new_fields_array.append(
                    self._convert_from_graphql_to_sgql(field)
                )
            count += 1
        return new_fields_array

    def __generate_uniqueness_err_message(self, msg, prefixes, count = None):
        """
        Helper function to append path or index for error messages from _validate_and_transform_fields
        """
        if len(prefixes) >= 1:
            msg += "  in path "
            msg += ".".join(prefixes)
            if count is not None:
                msg += f"[{count}]"
        elif count is not None:
            msg += f" at index {count}"
        return msg
