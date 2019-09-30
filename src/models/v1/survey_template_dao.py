
from src.utils.errors import GraphQLError, DataLogicError
from sgqlc.operation import Operation
from .base_dao import BaseGraphQL
import json

class SurveyTemplateGraphQLV1(BaseGraphQL):
    
    def __init__(self, **kwargs):
        super().__init__("Survey", **kwargs)

    def _generate_survey_selectors(self):
        # pylint: disable=no-member
        selectors = {}
        if hasattr(self,"uid"):
            selectors["uid"] = self.uid
            msg_addon = f"uid {self.uid}"
        elif hasattr(self, "uniqueName"):
            selectors["unique_name"] = self.uniqueName
            msg_addon = f"uniqueName {self.uniqueName}"
        
        return selectors, msg_addon
    
    def query_survey_responses(self, surveyTemplateUID):
        selectors, _ = self._generate_survey_selectors()
        selected_fields = [
            {
                "versions": {
                    "type": "SurveyTemplate",
                    "fields": [
                        {
                            "responses": {
                                "type": "SurveyResponse",
                                "fields": [
                                    "processedData"
                                ]
                            }
                        }
                    ]
                }
            }
        ]

        filters = {
            "versions": {
                "uid": surveyTemplateUID
            }
        }

        data = super().query(selected_fields, selectors, filters_on_fields=filters)
        if len(data["Survey"]) == 0:
            raise ValueError( 
                f"survey with selectors {selectors} does not exist"
        )

        survey_data = data["Survey"][0]

        if len(survey_data["versions"]) == 0:
            raise ValueError(
                f"survey template with uid {surveyTemplateUID} for survey with selectors {selectors}"
        )

        responses = survey_data["versions"][0]["responses"]
        return responses
    def query_survey_template_by_uid(self, uid):
        selectors, msg_addon = self._generate_survey_selectors()
        selected_fields = [
            "uid",
            "uniqueName",
            { 
                "createdAt": {
                    "type": "_Neo4jDateTimeInput",
                    "fields":[
                        "formatted"
                    ]
                }
            },
            {
                "versions":{
                    "type": "SurveyTemplate",
                    "fields": [
                        "uid",
                        "versionNumber",
                        "surveyTemplate",
                        "evalese",
                        { 
                            "createdAt": {
                                "type": "_Neo4jDateTimeInput",
                                "fields":[
                                    "formatted"
                                ]
                            }
                        }
                    ]
                } 
            }
        ]

        filters = {
            "versions": {
                "uid": uid
            }
        }

        data = super().query(selected_fields, selectors, filters_on_fields=filters)
        if len(data["Survey"]) == 0:
            return None
        elif len(data["Survey"]) > 1:
            msg = ( 
                "Mutple surveys were found for survey " +
                msg_addon + " when there should only be one"
            )
            raise DataLogicError(msg)
        
        data = data["Survey"][0]
        if len(data.get("versions")) < 1:
            return None

        return_data = {
            "surveyUID": data["uid"],
            "surveyUniqueName": data["uniqueName"],
            "surveyCreatedAt": data["createdAt"]["formatted"]
        }
        return_data["versionNumber"] = data["versions"][0]["versionNumber"]
        return_data["surveyTemplateCreatedAt"] = data["versions"][0]["createdAt"]["formatted"] 
        return_data["surveyTemplate"] = json.loads(data["versions"][0]["surveyTemplate"])
        return_data["evalese"] = data["versions"][0]["evalese"]
        return return_data
    
    def query_survey_template_by_version_number(self, version_number = 1):
        selectors, msg_addon = self._generate_survey_selectors()
        selected_fields = [
            "uid",
            "uniqueName",
            { 
                "createdAt": {
                    "type": "_Neo4jDateTimeInput",
                    "fields":[
                        "formatted"
                    ]
                }
            },
            {
                "versions":{
                    "type": "SurveyTemplate",
                    "fields": [
                        "uid",
                        "versionNumber",
                        "surveyTemplate",
                        "evalese",
                        { 
                            "createdAt": {
                                "type": "_Neo4jDateTimeInput",
                                "fields":[
                                    "formatted"
                                ]
                            }
                        }
                    ]
                } 
            }

        ]
        
        filters = {
            "versions":{
                "version_number": version_number
            }
        }

        data = super().query(selected_fields, selectors, filters_on_fields=filters)
        if len(data["Survey"]) == 0:
            return None
        elif len(data["Survey"]) > 1:
            msg = ( 
                "Mutple surveys were found for survey " +
                msg_addon + " when there should only be one"
            )
            raise DataLogicError(msg)
        data = data["Survey"][0]
        if len(data.get("versions")) < 1:
            return None
        return_data = {
            "surveyUID": data["uid"],
            "surveyUniqueName": data["uniqueName"],
            "surveyCreatedAt": data["createdAt"]["formatted"]
        }
        # TODO
        # should be refactored out to a schema so that fields are garunteed to be the same across returned data
        return_data["surveyTemplateUID"] = data["versions"][0]["uid"]
        return_data["versionNumber"] = data["versions"][0]["versionNumber"]
        return_data["surveyTemplateCreatedAt"] = data["versions"][0]["createdAt"]["formatted"] 
        return_data["surveyTemplate"] = json.loads(data["versions"][0]["surveyTemplate"])
        return_data["evalese"] = data["versions"][0]["evalese"]
        return return_data
    
    def query_latest_survey_template(self):
        selectors, msg_addon = self._generate_survey_selectors()
        selected_fields = [
            "uid",
            "uniqueName",
            { 
                "createdAt": {
                    "type": "_Neo4jDateTimeInput",
                    "fields":[
                        "formatted"
                    ]
                }
            },
            {
                "latest": {
                    "type": "SurveyTemplate",
                    "fields":[
                        "uid",
                        "versionNumber",
                        "surveyTemplate",
                        "evalese",
                        { 
                            "createdAt": {
                                "type": "_Neo4jDateTimeInput",
                                "fields":[
                                    "formatted"
                                ]
                            }
                        }
                    ]
                }
            }
        ]
        
        data = super().query(selected_fields, selectors)

        if len(data["Survey"]) == 0:
            return None
        elif len(data["Survey"]) > 1:
            msg = ( 
                "Mutple surveys were found for survey " +
                msg_addon + " when there should only be one"
            )
            raise DataLogicError(msg)
        
        data = data["Survey"][0]
        data_returned = {
            "surveyUID": data["uid"],
            "surveyUniqueName": data["uniqueName"],
            "surveyCreatedAt": data["createdAt"]["formatted"]
        }
        if data.get("latest") is not None:
            data_returned["surveyTemplateUID"] = data["latest"]["uid"]
            data_returned["versionNumber"] = data["latest"]["versionNumber"]
            data_returned["surveyTemplateCreatedAt"] = data["latest"]["createdAt"]["formatted"]
            data_returned["surveyTemplate"] = json.loads(data["latest"]["surveyTemplate"])
            data_returned["evalese"] = data["latest"]["evalese"]
        else:
            data_returned["surveyTemplate"] = None
        
        return data_returned
    
    def survey_exists(self):
        selectors, msg_addon = self._generate_survey_selectors()
        selected_fields = [
            "uid",
            "versionsCount",
            {
                "createdAt": {
                    "type": "_Neo4jDateTimeInput",
                    "fields": [
                        "formatted"
                    ]

                }
            },
            {
                "latest": {
                    "type": "SurveyTemplate",
                    "fields": [
                        "uid"
                    ]
                }
            }
        ]
        
        data = super().query(selected_fields, selectors)

        print(data)

        if len(data["Survey"]) == 0:
            return False, None, None, None, None
        elif len(data["Survey"]) > 1:
            msg = ( 
                "Mutple surveys were found for survey " +
                msg_addon + " when there should only be one"
            )
            raise DataLogicError(msg)
        return True, data["Survey"][0]["uid"], data["Survey"][0]["latest"]["uid"], data["Survey"][0]["versionsCount"], data["Survey"][0]["createdAt"]["formatted"]
    
    def create_survey_template(self):
        # pylint: disable=no-member
        if not hasattr(self, "evalese") or not hasattr(self, "surveyTemplate"):
            raise ValueError(
               "fields evalese and surveyTemplate are required to create the survey template"
            ) 
        mutations = []
        exists, survey_uid, last_template_uid, version_number, createdAt = self.survey_exists()
        if not exists:
            if not hasattr(self, "uniqueName"):
                raise ValueError(
                   "uniqueName is required to create the survey template"
                )
            mutations.append(
                {
                    "CreateSurvey": {
                        "values": {
                            "uniqueName": self.uniqueName
                        },
                        "fields":[
                            "uid",
                            "versionsCount",
                            {
                                "createdAt": {
                                    "type": "_Neo4jDateTimeInput",
                                    "fields": [
                                        "formatted"
                                    ]
                                }
                            }
                        ]
                    }
                }
            )
            mutations.append(
                {
                    "CreateSurveyTemplate": {
                        "values": {
                            "surveyTemplate": json.dumps(self.surveyTemplate),
                            "evalese": self.evalese,
                            "versionNumber": 1
                        },
                        "fields": [
                            "uid",
                            "versionNumber",
                            {
                                "createdAt": {
                                    "type": "_Neo4jDateTimeInput",
                                    "fields": [
                                        "formatted"
                                    ]
                                }
                            }
                        ]
                    }
                }
            )

            mutations.append(
                {
                    "AddSurveyLatest": {
                        "values": {
                            "from":{
                                "type": "_SurveyInput",
                                "values": {
                                    "uid": {
                                        "reference": "CreateSurvey.uid"
                                    }
                                }
                            },
                            "to": {
                                "type": "_SurveyTemplateInput",
                                "values": {
                                    "uid": {
                                        "reference": "CreateSurveyTemplate.uid"
                                    }
                                }
                            }
                        },
                        "fields":[
                            {
                                "from": {
                                    "type": "_SurveyInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            },
                            {
                                "to": {
                                    "type": "_SurveyTemplateInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            }
                        ]
                    }
                }
            )
            mutations.append(
                {
                    "AddSurveyVersions": {
                        "values": {
                            "from": {
                                "type": "_SurveyInput",
                                "values": {
                                    "uid": {
                                        "reference": "CreateSurvey.uid"
                                    }
                                }
                            },
                            "to": {
                                "type": "_SurveyTemplateInput",
                                "values": {
                                    "uid": {
                                        "reference": "CreateSurveyTemplate.uid"
                                    }
                                }
                            }
                        },
                        "fields":[
                            {
                                "from": {
                                    "type": "_SurveyInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            },
                            {
                                "to": {
                                    "type": "_SurveyTemplateInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            }
                        ]
                    }
                }
            )
        else:
            # delete the LATEST_VERSION relationship
            mutations.append(
                {
                    "RemoveSurveyLatest": {
                        "values": {
                            "from": {
                                "type": "_SurveyInput",
                                "values": {
                                    "uid": survey_uid
                                }
                            },
                            "to": {
                                "type": "_SurveyTemplateInput",
                                "values": {
                                    "uid": last_template_uid
                                }
                            }
                        },
                        "fields":[
                            {
                                "from": {
                                    "type": "_SurveyInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            },
                            {
                                "to": {
                                    "type": "_SurveyTemplateInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            }
                        ]
                    }
                }
            )

            mutations.append(
                {
                    "CreateSurveyTemplate": {
                        "values": {
                            "versionNumber": version_number + 1,
                            "surveyTemplate": json.dumps(self.surveyTemplate),
                            "evalese": self.evalese
                        },
                        "fields": [
                            "uid",
                            "versionNumber",
                            {
                                "createdAt": {
                                    "type": "_Neo4jDateTimeInput",
                                    "fields": [
                                        "formatted"
                                    ]
                                }
                            }
                        ]
                    }
                }
            )

            # add the survey relationships
            mutations.append(
                {
                    "AddSurveyLatest": {
                        "values": {
                            "from":{
                                "type": "_SurveyInput",
                                "values": {
                                    "uid": survey_uid
                                }
                            },
                            "to": {
                                "type": "_SurveyTemplateInput",
                                "values": {
                                    "uid": {
                                        "reference": "CreateSurveyTemplate.uid"
                                    }
                                }
                            }
                        },
                        "fields":[
                            {
                                "from": {
                                    "type": "_SurveyInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            },
                            {
                                "to": {
                                    "type": "_SurveyTemplateInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            }
                        ]
                    }
                }
            )

            mutations.append(
                {
                    "AddSurveyTemplatePreviousVersion":{
                        "values": {
                            "from": {
                                "type": "_SurveyTemplateInput",
                                "values": {
                                    "uid": {
                                        "reference": "CreateSurveyTemplate.uid"
                                    }
                                }
                            },
                            "to": {
                                "type": "_SurveyTemplateInput",
                                "values": {
                                    "uid": last_template_uid
                                }
                            }
                        },
                        "fields":[
                            {
                                "from": {
                                    "type": "_SurveyTemplateInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            },
                            {
                                "to": {
                                    "type": "_SurveyTemplateInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            }
                        ]
                    }
                }
            )

            mutations.append(
                {
                    "AddSurveyVersions": {
                        "values": {
                            "from": {
                                "type": "_SurveyInput",
                                "values": {
                                    "uid": survey_uid
                                }
                            },
                            "to": {
                                "type": "_SurveyTemplateInput",
                                "values": {
                                    "uid": {
                                        "reference": "CreateSurveyTemplate.uid"
                                    }
                                }
                            }
                        },
                        "fields":[
                            {
                                "from": {
                                    "type": "_SurveyInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            },
                            {
                                "to": {
                                    "type": "_SurveyTemplateInput",
                                    "fields": [
                                        "uid"
                                    ]
                                }
                            }
                        ]
                    }
                }
            )

        data = super().mutate(mutations)
        data_return = {
            "surveyUID": data["AddSurveyLatest"]["from"]["uid"]
        }
        if exists:
            data_return["previousSurveyTemplateUID"] = last_template_uid
            data_return["surveyCreatedAt"] = createdAt
        else:
            data_return["surveyCreatedAt"] = data["CreateSurvey"]["createdAt"]["formatted"]
        
        data_return["surveyTemplateUID"] = data["CreateSurveyTemplate"]["uid"]
        data_return["surveyTemplateCreatedAt"] = data["CreateSurveyTemplate"]["createdAt"]["formatted"]
        data_return["versionNumber"] = data["CreateSurveyTemplate"]["versionNumber"]
        return data_return



        







       
                