from marshmallow import Schema, fields, validates_schema, post_load, ValidationError, validate
from .survey_template_schema import SurveyTemplateSchemaV1
from  src.models.v1 import SurveyResponseGraphQLV1
from  src.api.utils.schemas.utils.validators import validate_isodatetime_string_has_timezone
import datetime
import pytz


class SurveyRespondantSchemaV1(Schema):
    userAgent = fields.String(required = True)
    surveyEntryMethod = fields.String(required= True)
    responseLanguage = fields.String(
        required = True, 
        validate= validate.OneOf(("en", "fr"),
        error= "{input} for the response language is not one of the supported {choices}")
    )
    department = fields.String()
    location = fields.String()
    classification = fields.String()

class SurveyResponseCreatedSchemaV1(Schema):
    started = fields.DateTime(
        format="iso", required=True,
        validate = validate_isodatetime_string_has_timezone
    )
    completed = fields.DateTime( 
        format = "iso", required = True,
        validate= validate_isodatetime_string_has_timezone
    )
    @validates_schema
    def started_less_than_completd(self, data, **kwargs):
        if data.get("started") > data.get("completed"):
            raise ValidationError("started datetime is greater than completed datetime")
    @post_load
    def set_time_zones_to_utc(self, data, **kwargs):
        # convert datetimes to UTC 
        if data["started"].tzinfo != datetime.timezone.utc:
            data["started"] = data["started"].astimezone(pytz.utc)
        if data["completed"].tzinfo != datetime.timezone.utc:
            data["completed"] = data["completed"].astimezone(pytz.utc)
        return data

class SurveyResponseSchemaV1(Schema):
    survey = fields.Nested(SurveyTemplateSchemaV1, required=True)
    surveyTemplateUID = fields.String()
    surveyTemplateVersionNumber = fields.Int()
    data = fields.Dict(keys = fields.Str(), values= fields.Str())
    respondent = fields.Nested(SurveyRespondantSchemaV1)
    created = fields.Nested(SurveyResponseCreatedSchemaV1)
    @post_load
    def load_graphql_obj(self, data, **kwargs):
        return SurveyResponseGraphQLV1(**data)

        
     




