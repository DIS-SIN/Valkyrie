from src.api.utils.decorators import register_api_version
from .survey_template_resource import QuerySurveyTemplateResource, CreateSurveyTemplateResource
from .survey_response_resource import QuerySurveyResponseRessource ,CreateSurveyResponseResource


@register_api_version
def register_v1_routes(api):
    api.add_resource(
        QuerySurveyTemplateResource, 
        "/survey/<string:uid>/version/<int:version_number>",
        "/survey/<string:uid>/version/<string:survey_template_uid>",
        "/survey/version",
        "/survey/<string:uid>",
        endpoint = "querySurveyTemplate"
    )
    api.add_resource(
        QuerySurveyResponseRessource,
        "/survey/<string:uid>/version/<int:version_number>/responses",
        "/survey/<string:uid>/version/<string:survey_template_uid>/responses",
        "/survey/responses",
        "/survey/<string:uid>/responses"
    )
    api.add_resource(
        CreateSurveyTemplateResource,
        "/survey",
        endpoint = "createSurveyTemplate"
    )
    api.add_resource(
        CreateSurveyResponseResource,
        "/survey/response",
        endpoint = "createSurveyResponse"
    )

