# -*- coding: utf-8 -*-
from src.models.v1 import SurveyTemplateGraphQLV1
from src.api.utils.schemas.utils.validators.datetime_validator import validate_isodatetime_string_has_timezone
from marshmallow import fields, Schema, post_load, validates_schema, ValidationError, validate, INCLUDE
import pytz
import datetime


class SurveyTemplateQuestionData(Schema):
    en = fields.String()
    fr = fields.String()

class SurveyTemplateValidFromTo(Schema):
    from_ = fields.DateTime(
        format="iso",
        data_key="from",
        validate= validate_isodatetime_string_has_timezone
    )
    to = fields.DateTime( 
        format="iso",
        data_key= "to",
        validate = validate_isodatetime_string_has_timezone
    )
    @validates_schema
    def from_less_than_to(self, data, **kwargs):
        if data.get("from_") is not None and data.get("to") is not None:
            if data["from_"] >= data["to"]:
                raise ValidationError("from datetime must be less than to")
    @post_load
    def set_time_zones_to_utc(self, data: dict, **kwargs):
        # convert datetimes to UTC
        from_ = data.pop("from_", None)
        to = data.get("to")
        if from_ is not None:    
            if from_.tzinfo != datetime.timezone.utc:
                data["from"] = from_.astimezone(pytz.utc).isoformat()
            else:
                data["from"] = from_.isoformat()
        if to is not None:
            if to.tzinfo != datetime.timezone.utc:
                data["to"] = to.astimezone(pytz.utc).isoformat()
            else:
                data["to"] = to.isoformat()
        return data

class SurveyTemplateQuestions(Schema):
    class Meta:
        unknown = INCLUDE
    uid = fields.String(required=True)
    atOrder = fields.String(required=True)
    cortexQuestionType = fields.String()
    classifiedAs = fields.String()

    @post_load
    def load_questions(self, data, **kwargs):
        cortex_data = {}
        question_data = data.get("question")
        # if the question field is a dictionary then try to extract the english and french question text
        if isinstance(question_data, dict):
            question_data_schema = SurveyTemplateQuestionData()
            question_info = question_data_schema.load(
                question_data
            )
            if question_info.get("en") is not None:
                cortex_data["englishQuestionText"] = question_info["en"]
            if question_info.get("fr") is not None:
                cortex_data["frenchQuestionText"] = question_info["fr"]
        cortex_data["questionId"] = data.get("uid")
        cortex_data["questionType"] = data.get("cortexQuestionType")
        cortex_data["classifiedAs"] = data.get("classifiedAs")
        cortex_data["atOrder"] = data.get("atOrder")
        data["cortexQuestionInfo"] = cortex_data
        return data
    

class SurveyTemplateDataSchemaV1(Schema):
    # not going to define all fields, just the ones I need
    class Meta:
        unknown = INCLUDE
    questions = fields.List(
        fields.Nested(SurveyTemplateQuestions),
        required = True
    )
    valid  = fields.Nested(
        SurveyTemplateValidFromTo
    )

class SurveyTemplateSchemaV1(Schema):
    uid = fields.String(validate = validate.Length(
        min=5, 
        error="uid {input} is not valid, must be atleast {min} characters"
        )
    )
    uniqueName = fields.String(
        validate = validate.Length(
            min = 2,
            error = "uniqueName must have atleast {min} characters"
        )
    )
    createdAt = fields.String(dump_only= True)
    surveyTemplate = fields.Nested(SurveyTemplateDataSchemaV1)
    evalese = fields.String()
    
    @validates_schema
    def validate_survey_schema(self, data, **kwargs):
        if data.get("uid") is None  and data.get("uniqueName") is None:
            raise ValidationError("To query or add a SurveyTemplate either the uid or the uniqueName of the survey must be provided")
    @post_load
    def load_graphql_obj(self, data, **kwargs):
        return SurveyTemplateGraphQLV1(**data)


