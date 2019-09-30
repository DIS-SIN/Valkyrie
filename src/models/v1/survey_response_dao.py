from .base_dao import BaseGraphQL
from .response_questions_dao import ResponseQuestionsGraphQL
from flask import current_app
import json
import datetime
import copy


class SurveyResponseGraphQLV1(BaseGraphQL):

    def __init__(self, **kwargs):
       super().__init__(model="SurveyResponse", **kwargs)

    def _get_survey_identifier(self):
        # pylint: disable=no-member
        if hasattr(self.survey, "uid"):
            return self.survey.uid
        elif hasattr(self.survey, "uniqueName"):
            return self.survey.uniqueName
    
    def _get_template_identifier(self):
        # pylint: disable=no-member
        if hasattr(self, "surveyTemplateUID"):
            return self.surveyTemplateUID
        elif hasattr(self, "surveyTemplateVersionNumber"):
            return self.surveyTemplateVersionNumber
    
    def query_survey_responses(self):
        # pylint: disable=no-member
        exists = self.survey.survey_exists()

        if not exists[0]:
            survey_identifier = self._get_survey_identifier()
            raise ValueError(f"Survey with identifier {survey_identifier} does not exist")

        if hasattr(self, "surveyTemplateUID"):
           data = self.survey.query_survey_template_by_uid(self.surveyTemplateUID) 
        elif hasattr(self, "surveyTemplateVersionNumber"):
           data =self.survey.query_survey_template_by_version_number(self.surveyTemplateVersionNumber)
        else:
           data = self.survey.query_latest_survey_template()
        
        if data is None:
            template_identifier = self._get_template_identifier()
            survey_identifier = self._get_survey_identifier()
            raise ValueError(
               f"Survey template version with identifier {template_identifier} for survey with identifier {survey_identifier}"
            )
        
        surveyUID = data["surveyUID"]
        surveyUniqueName = data["surveyUniqueName"]
        surveyTemplateUID = data["surveyTemplateUID"]

        data = self.survey.query_survey_responses(surveyTemplateUID)


        return_data = {
            "surveyUID": surveyUID,
            "surveyUniqueName": surveyUniqueName,
            "surveyTemplateUID": surveyTemplateUID
        }
        if len(data) == 0:
            return_data["responses"] = []
            return return_data
        
        survey_response_data = []

        for response in data:
            processed_data = response.get("processedData")
            if isinstance(processed_data, str):
                try:
                    survey_response_data.append(
                        json.loads(processed_data)
                    )
                except Exception:
                    pass
        return_data["responses"] = survey_response_data
        return return_data

            
    
    def create_survey_response(self):
         # pylint: disable=no-member
        if not hasattr(self, "survey"):
            raise ValueError(
               "Survey must be provided in order to create response"
            )
        # either get the survery template by uid if that is provided 
        # or get it by the version number
        # or get the latest template version
        exists = self.survey.survey_exists()

        if not exists[0]:
            survey_identifier = self._get_survey_identifier()
            raise ValueError(f"Survey with identifier {survey_identifier} does not exist")
             
        if hasattr(self, "surveyTemplateUID"):
           data = self.survey.query_survey_template_by_uid(self.surveyTemplateUID) 
        elif hasattr(self, "surveyTemplateVersionNumber"):
           data =self.survey.query_survey_template_by_version_number(self.surveyTemplateVersionNumber)
        else:
           data = self.survey.query_latest_survey_template()
        
        if data is None:
            template_identifier = self._get_template_identifier()
            survey_identifier = self._get_survey_identifier()
            raise ValueError(
               f"Survey template version with identifier {template_identifier} for survey with identifier {survey_identifier}"
            )
        
        surveyUID = data["surveyUID"]
        surveyUniqueName = data["surveyUniqueName"]
        surveyTemplateUID = data["surveyTemplateUID"]
        surveyTemplate = data["surveyTemplate"]

        # check if survey is within the valid time frame
        validity_range = surveyTemplate.get("valid")
        from_ = None
        from_iso = ""
        to = None
        to_iso = ""
        # get the ISO datetime strings for the  created fields
        completed_iso = self.created["completed"].isoformat()
        started_iso = self.created["started"].isoformat()
        if validity_range is not None:
            from_ = validity_range.get("from")
            to = validity_range.get("to")
        
        if from_ is not None:
            from_ = datetime.datetime.fromisoformat(from_)
            from_iso = from_.isoformat()
            if self.created["completed"] < from_:
               raise ValueError(
                  f"completed date for response {completed_iso} " +
                  f"is before the valid date of the template {from_iso} with UID {surveyTemplateUID}"     
               )
            elif self.created["started"] < from_:
                raise ValueError( 
                   f"suvey was started {started_iso} " +
                   f"before the tamplate became valid on {from_iso} with UID {surveyTemplateUID}"
                )
        if to is not None:
            to = datetime.datetime.fromisoformat(to)
            to_iso = to.isoformat()

            if self.created["completed"] > to:
                raise ValueError(
                  f"template with UID {surveyTemplateUID} has expired on {to_iso} " +
                  f"response was completed on {completed_iso}"  
            )

        # generate the question mutations
        # generate the response mutation
        # execute the mutation and then return the UID of the response

        create_survey_response_mutation = {
            "CreateSurveyResponse": {
                "values": {
                    "rawData": json.dumps(self.data),
                    "startedOn": {
                        "type": "_Neo4jDateTimeInput",
                        "values": {
                            "formatted": self.created["started"].isoformat()
                        }
                    },
                    "completedOn": {
                        "type": "_Neo4jDateTimeInput",
                        "values": {
                            "formatted": self.created["completed"].isoformat()
                        }
                    }
                },
                "fields": [
                    "uid",
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

        create_respondent_mutation = {
            "CreateRespondent" : {
                "values": {
                    "userAgent": self.respondent["userAgent"],
                    "surveyEntryMethod": self.respondent["surveyEntryMethod"],
                    "responseLanguage": self.respondent["responseLanguage"],
                    "department": self.respondent.get("department") or "",
                    "location": self.respondent.get("location") or "",
                    "classification": self.respondent.get("classification") or ""
                },
                "fields": [
                    "uid"
                ]
            }
        }

        add_survey_response_respondent = {
            "AddSurveyResponseRespondent": {
                "values": {
                    "from": {
                        "type": "_SurveyResponseInput",
                        "values":{
                            "uid": {
                                "reference": "CreateSurveyResponse.uid"
                            }
                        }
                    },
                    "to": {
                        "type": "_RespondentInput",
                        "values": {
                            "uid": {
                                "reference": "CreateRespondent.uid"
                            }
                        }
                    }
                },
                "fields": [
                    {
                        "from": {
                            "type": "_SurveyResponseInput",
                            "fields": [
                                "uid"
                            ]
                        }
                    },
                    {
                        "to": {
                            "type": "_RespondentInput",
                            "fields": [
                                "uid"
                            ]
                        }
                    }
                ]
            }
        }

        add_survey_template_response = {
            "AddSurveyTemplateResponses":{
                "values": {
                    "from": {
                        "type": "_SurveyTemplateInput",
                        "values": {
                            "uid": surveyTemplateUID
                        }
                    },
                    "to": {
                        "type": "_SurveyResponseInput",
                        "values": {
                            "uid": {
                                "reference": "CreateSurveyResponse.uid"
                            }
                        }
                    }
                },
                "fields": [
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
                            "type": "_SurveyResponseInput",
                            "fields": [
                                "uid"
                            ]
                        }
                    }
                ]
            }
        }

        mutation_sequence = [
            create_survey_response_mutation,
            create_respondent_mutation,
            add_survey_template_response,
            add_survey_response_respondent
        ]
        question_mutator = ResponseQuestionsGraphQL(
            surveyUID,
            surveyTemplateUID,
            surveyTemplate,
            self.data
        )

        calculated_sentiment = question_mutator.calculate_sentiment()

        if calculated_sentiment:
            processed_data = {**self.data, **calculated_sentiment}
        else:
            processed_data = self.data
        
        processed_data["tombstone_city"] = self.respondent.get("location") or ""
        processed_data["tombstone_language"] = self.respondent.get("responseLanguage") or ""
        processed_data["tombstone_department"] = self.respondent.get("department") or ""
        processed_data["tombstone_classification"] = self.respondent.get("classification") or ""
        processed_data["meta_submission_startedAt"] = self.created["started"].isoformat()
        processed_data["meta_submission_completedAt"] = self.created["completed"].isoformat()
        processed_data["meta_evalhalla_sur"] = surveyUniqueName

        create_survey_response_mutation["CreateSurveyResponse"]["values"]["processedData"] = json.dumps(processed_data)
        
        data = super().mutate(mutation_sequence)

        surveyResponseUID = data["CreateSurveyResponse"]["uid"]
        surveyResponseCreatedAt = data["CreateSurveyResponse"]["createdAt"]["formatted"]

        question_data = question_mutator.create_response_questions(surveyResponseUID)


        return {
            "surveyUID": surveyUID,
            "surveyUniqueName": surveyUniqueName,
            "surveyTemplateUID": surveyTemplateUID,
            "surveyResponseUID": surveyResponseUID,
            "surveyResponseCreatedAt": surveyResponseCreatedAt,
            "surveyProcessedData": processed_data,
            "questions": question_data
        }



        
        


