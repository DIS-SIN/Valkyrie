from flask_restful import Resource, reqparse
from src.api.utils.development_utils import raise_error
from src.api.utils.schemas.v1_schemas import SurveyTemplateSchemaV1
from marshmallow import ValidationError
from src.utils.errors import DataLogicError, GraphQLError
from flask import request
import logging

survey_template_parser = reqparse.RequestParser(bundle_errors=True, trim=True)
survey_template_parser.add_argument("unique_name", type=str)
survey_template_parser.add_argument("version_number", type=int)
survey_template_parser.add_argument("survey_template_uid", type=str)
survey_template_parser.add_argument("uid", type=str)

# TODO: add logging
class QuerySurveyTemplateResource(Resource):
    schema = SurveyTemplateSchemaV1()
    def get(self, uid = None, version_number = None, survey_template_uid = None):
        # right now this will only give the latest survey_template
        # TODO: filtering for any survey template
        args = survey_template_parser.parse_args()
        unique_name = args.get("unique_name")
        version_number = version_number or args.get("version_number")
        survey_template_uid = survey_template_uid or args.get("survey_template_uid")
        uid = uid or args.get("uid")
        survey_request = {
            "uid": uid,
            "uniqueName": unique_name
        }
        
        if uid is None:
            del survey_request["uid"]
        if unique_name is None:
            del survey_request["uniqueName"] 
        
        try:
            graphql = self.schema.load(survey_request)
        except ValidationError as e:
            raise_error(e)
            return {
                "error": {
                    "message": "Failed to deserialize request",
                    "error": e.messages
                } 
            }, 500
        try:
            if survey_template_uid is not None:
                print(survey_template_uid)
                data = graphql.query_survey_template_by_uid(survey_template_uid)
            elif version_number is not None:
                data = graphql.query_survey_template_by_version_number(version_number)
            else:
                data = graphql.query_latest_survey_template()
            if data is None:
                return "",201
            else:
                return data, 200
        except DataLogicError as e:
            raise_error(e)
            return {
                "error": {
                    "message": "The integrity of the data is compramised",
                    "error": str(e)
                }
            }, 500
        except GraphQLError as e:
            raise_error(e)
            return {
                "error": {
                    "message": "An GraphQL exception has occured",
                    "error": str(e)
                }
            }, 500
        except Exception as e:
            raise_error(e)
            return {
                "error": {
                    "message": "An unkown exception has occured",
                    "error": repr(e)
                }
            }, 500

class CreateSurveyTemplateResource(Resource):
    schema = SurveyTemplateSchemaV1()
    def post(self): 
        request_data = request.get_json()
        if request_data is None:
            return {
                "error": {
                    "message": "This request must include a payload",
                    "error": "Invalid Request"
                }
            }, 400
        try:
            graphql = self.schema.load(request_data)
        except ValidationError as e:
            raise_error(e)
            return {
                "error": {
                    "messages": "The request payload is invalid",
                    "error": e.messages
                }
            }, 400
        
        try:
            data = graphql.create_survey_template()
            return data, 200
        except ValueError as e:
            raise_error(e)
            return {
                "error": {
                    "messages": "The request payload is invalid",
                    "error": str(e)
                }
            }, 400 
        except DataLogicError as e:
            raise_error(e)
            return {
                "error": {
                    "message": "The integrity of the data is compramised",
                    "error": str(e)
                }
            }, 500
        except GraphQLError as e:
            raise_error(e)
            return {
                "error": {
                    "message": "A GraphQL exception has occured",
                    "error": str(e)
                }
            }, 500
        except Exception as e:
            raise_error(e)
            return {
                "error": {
                    "message": "An unkown exception has occured",
                    "error": repr(e)
                }
            }, 500
        



