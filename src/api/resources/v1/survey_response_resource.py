from flask_restful import Resource, reqparse
from src.api.utils.development_utils import raise_error
from src.api.utils.schemas.v1_schemas import SurveyResponseSchemaV1
from marshmallow import ValidationError
from src.utils.errors import DataLogicError, GraphQLError
from flask import request
import logging

survey_response_parser = reqparse.RequestParser(bundle_errors=True, trim=True)
survey_response_parser.add_argument("unique_name", type=str)
survey_response_parser.add_argument("version_number", type=int)
survey_response_parser.add_argument("survey_template_uid", type=str)
survey_response_parser.add_argument("uid", type=str)


class QuerySurveyResponseRessource(Resource):
    schema = SurveyResponseSchemaV1()
    def get(self, uid = None, version_number = None, survey_template_uid = None):
        args = survey_response_parser.parse_args()
        unique_name = args.get("unique_name")
        version_number = version_number or args.get("version_number")
        survey_template_uid = survey_template_uid or args.get("survey_template_uid")
        uid = uid or args.get("uid")

        response_request = {
            "survey": {
                "uid": uid,
                "uniqueName": unique_name
            }
        }
        if uid is None:
            del response_request["survey"]["uid"]
        if unique_name is None:
            del response_request["survey"]["uniqueName"] 

        if version_number is not None:
            response_request["surveyTemplateVersionNumber"] = version_number
        elif survey_template_uid is not None:
            response_request["surveyTemplateUID"] = survey_template_uid
        
        try:
            graphql = self.schema.load(response_request)
        except ValidationError as e:
            raise_error(e)
            return {
                "error": {
                    "message": "Failed to deserialize request",
                    "error": e.messages
                } 
            }, 500
        
        try:
            data = graphql.query_survey_responses()
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
        
        


class CreateSurveyResponseResource(Resource):
    schema = SurveyResponseSchemaV1()
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
            data = graphql.create_survey_response()
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
        
        
        
