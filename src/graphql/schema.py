import sgqlc.types


schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String

class _AnswerOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('uid_asc', 'uid_desc', 'answer_asc', 'answer_desc', 'calculatedMetrics_asc', 'calculatedMetrics_desc', 'processedOn_asc', 'processedOn_desc', '_id_asc', '_id_desc')


class _QuestionOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('uid_asc', 'uid_desc', 'questionId_asc', 'questionId_desc', 'questionType_asc', 'questionType_desc', 'classifiedAs_asc', 'classifiedAs_desc', 'atOrder_asc', 'atOrder_desc', 'englishQuestionText_asc', 'englishQuestionText_desc', 'frenchQuestionText_asc', 'frenchQuestionText_desc', '_id_asc', '_id_desc')


class _RelationDirections(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('IN', 'OUT')


class _RespondentOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('uid_asc', 'uid_desc', 'userAgent_asc', 'userAgent_desc', 'surveyEntryMethod_asc', 'surveyEntryMethod_desc', 'responseLanguage_asc', 'responseLanguage_desc', 'department_asc', 'department_desc', 'classification_asc', 'classification_desc', 'location_asc', 'location_desc', 'additionalData_asc', 'additionalData_desc', '_id_asc', '_id_desc')


class _SurveyMetricsOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('uid_asc', 'uid_desc', 'metrics_asc', 'metrics_desc', 'processedOn_asc', 'processedOn_desc', '_id_asc', '_id_desc')


class _SurveyOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('uid_asc', 'uid_desc', 'uniqueName_asc', 'uniqueName_desc', 'createdAt_asc', 'createdAt_desc', 'versionsCount_asc', 'versionsCount_desc', '_id_asc', '_id_desc')


class _SurveyResponseOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('uid_asc', 'uid_desc', 'rawData_asc', 'rawData_desc', 'processedData_asc', 'processedData_desc', 'createdAt_asc', 'createdAt_desc', 'startedOn_asc', 'startedOn_desc', 'completedOn_asc', 'completedOn_desc', '_id_asc', '_id_desc')


class _SurveyTemplateOrdering(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('uid_asc', 'uid_desc', 'surveyTemplate_asc', 'surveyTemplate_desc', 'versionNumber_asc', 'versionNumber_desc', 'evalese_asc', 'evalese_desc', 'createdAt_asc', 'createdAt_desc', '_id_asc', '_id_desc')



########################################################################
# Input Objects
########################################################################
class _AnswerFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_AnswerFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_AnswerFilter')), graphql_name='OR')
    uid = sgqlc.types.Field(ID, graphql_name='uid')
    uid_not = sgqlc.types.Field(ID, graphql_name='uid_not')
    uid_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_in')
    uid_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_not_in')
    uid_contains = sgqlc.types.Field(ID, graphql_name='uid_contains')
    uid_not_contains = sgqlc.types.Field(ID, graphql_name='uid_not_contains')
    uid_starts_with = sgqlc.types.Field(ID, graphql_name='uid_starts_with')
    uid_not_starts_with = sgqlc.types.Field(ID, graphql_name='uid_not_starts_with')
    uid_ends_with = sgqlc.types.Field(ID, graphql_name='uid_ends_with')
    uid_not_ends_with = sgqlc.types.Field(ID, graphql_name='uid_not_ends_with')
    answer = sgqlc.types.Field(String, graphql_name='answer')
    answer_not = sgqlc.types.Field(String, graphql_name='answer_not')
    answer_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='answer_in')
    answer_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='answer_not_in')
    answer_contains = sgqlc.types.Field(String, graphql_name='answer_contains')
    answer_not_contains = sgqlc.types.Field(String, graphql_name='answer_not_contains')
    answer_starts_with = sgqlc.types.Field(String, graphql_name='answer_starts_with')
    answer_not_starts_with = sgqlc.types.Field(String, graphql_name='answer_not_starts_with')
    answer_ends_with = sgqlc.types.Field(String, graphql_name='answer_ends_with')
    answer_not_ends_with = sgqlc.types.Field(String, graphql_name='answer_not_ends_with')
    calculated_metrics = sgqlc.types.Field(String, graphql_name='calculatedMetrics')
    calculated_metrics_not = sgqlc.types.Field(String, graphql_name='calculatedMetrics_not')
    calculated_metrics_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='calculatedMetrics_in')
    calculated_metrics_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='calculatedMetrics_not_in')
    calculated_metrics_contains = sgqlc.types.Field(String, graphql_name='calculatedMetrics_contains')
    calculated_metrics_not_contains = sgqlc.types.Field(String, graphql_name='calculatedMetrics_not_contains')
    calculated_metrics_starts_with = sgqlc.types.Field(String, graphql_name='calculatedMetrics_starts_with')
    calculated_metrics_not_starts_with = sgqlc.types.Field(String, graphql_name='calculatedMetrics_not_starts_with')
    calculated_metrics_ends_with = sgqlc.types.Field(String, graphql_name='calculatedMetrics_ends_with')
    calculated_metrics_not_ends_with = sgqlc.types.Field(String, graphql_name='calculatedMetrics_not_ends_with')
    processed_on = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='processedOn')
    processed_on_not = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='processedOn_not')
    processed_on_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='processedOn_in')
    processed_on_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_Neo4jDateTimeInput')), graphql_name='processedOn_not_in')
    processed_on_lt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='processedOn_lt')
    processed_on_lte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='processedOn_lte')
    processed_on_gt = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='processedOn_gt')
    processed_on_gte = sgqlc.types.Field('_Neo4jDateTimeInput', graphql_name='processedOn_gte')
    question = sgqlc.types.Field('_QuestionFilter', graphql_name='question')
    question_not = sgqlc.types.Field('_QuestionFilter', graphql_name='question_not')
    question_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_QuestionFilter')), graphql_name='question_in')
    question_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_QuestionFilter')), graphql_name='question_not_in')


class _AnswerInput(sgqlc.types.Input):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')


class _Neo4jDateInput(sgqlc.types.Input):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jDateTimeInput(sgqlc.types.Input):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalDateTimeInput(sgqlc.types.Input):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalTimeInput(sgqlc.types.Input):
    __schema__ = schema
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jTimeInput(sgqlc.types.Input):
    __schema__ = schema
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _QuestionFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_QuestionFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_QuestionFilter')), graphql_name='OR')
    uid = sgqlc.types.Field(ID, graphql_name='uid')
    uid_not = sgqlc.types.Field(ID, graphql_name='uid_not')
    uid_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_in')
    uid_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_not_in')
    uid_contains = sgqlc.types.Field(ID, graphql_name='uid_contains')
    uid_not_contains = sgqlc.types.Field(ID, graphql_name='uid_not_contains')
    uid_starts_with = sgqlc.types.Field(ID, graphql_name='uid_starts_with')
    uid_not_starts_with = sgqlc.types.Field(ID, graphql_name='uid_not_starts_with')
    uid_ends_with = sgqlc.types.Field(ID, graphql_name='uid_ends_with')
    uid_not_ends_with = sgqlc.types.Field(ID, graphql_name='uid_not_ends_with')
    question_id = sgqlc.types.Field(String, graphql_name='questionId')
    question_id_not = sgqlc.types.Field(String, graphql_name='questionId_not')
    question_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='questionId_in')
    question_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='questionId_not_in')
    question_id_contains = sgqlc.types.Field(String, graphql_name='questionId_contains')
    question_id_not_contains = sgqlc.types.Field(String, graphql_name='questionId_not_contains')
    question_id_starts_with = sgqlc.types.Field(String, graphql_name='questionId_starts_with')
    question_id_not_starts_with = sgqlc.types.Field(String, graphql_name='questionId_not_starts_with')
    question_id_ends_with = sgqlc.types.Field(String, graphql_name='questionId_ends_with')
    question_id_not_ends_with = sgqlc.types.Field(String, graphql_name='questionId_not_ends_with')
    question_type = sgqlc.types.Field(String, graphql_name='questionType')
    question_type_not = sgqlc.types.Field(String, graphql_name='questionType_not')
    question_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='questionType_in')
    question_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='questionType_not_in')
    question_type_contains = sgqlc.types.Field(String, graphql_name='questionType_contains')
    question_type_not_contains = sgqlc.types.Field(String, graphql_name='questionType_not_contains')
    question_type_starts_with = sgqlc.types.Field(String, graphql_name='questionType_starts_with')
    question_type_not_starts_with = sgqlc.types.Field(String, graphql_name='questionType_not_starts_with')
    question_type_ends_with = sgqlc.types.Field(String, graphql_name='questionType_ends_with')
    question_type_not_ends_with = sgqlc.types.Field(String, graphql_name='questionType_not_ends_with')
    classified_as = sgqlc.types.Field(String, graphql_name='classifiedAs')
    classified_as_not = sgqlc.types.Field(String, graphql_name='classifiedAs_not')
    classified_as_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='classifiedAs_in')
    classified_as_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='classifiedAs_not_in')
    classified_as_contains = sgqlc.types.Field(String, graphql_name='classifiedAs_contains')
    classified_as_not_contains = sgqlc.types.Field(String, graphql_name='classifiedAs_not_contains')
    classified_as_starts_with = sgqlc.types.Field(String, graphql_name='classifiedAs_starts_with')
    classified_as_not_starts_with = sgqlc.types.Field(String, graphql_name='classifiedAs_not_starts_with')
    classified_as_ends_with = sgqlc.types.Field(String, graphql_name='classifiedAs_ends_with')
    classified_as_not_ends_with = sgqlc.types.Field(String, graphql_name='classifiedAs_not_ends_with')
    at_order = sgqlc.types.Field(Int, graphql_name='atOrder')
    at_order_not = sgqlc.types.Field(Int, graphql_name='atOrder_not')
    at_order_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='atOrder_in')
    at_order_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='atOrder_not_in')
    at_order_lt = sgqlc.types.Field(Int, graphql_name='atOrder_lt')
    at_order_lte = sgqlc.types.Field(Int, graphql_name='atOrder_lte')
    at_order_gt = sgqlc.types.Field(Int, graphql_name='atOrder_gt')
    at_order_gte = sgqlc.types.Field(Int, graphql_name='atOrder_gte')
    english_question_text = sgqlc.types.Field(String, graphql_name='englishQuestionText')
    english_question_text_not = sgqlc.types.Field(String, graphql_name='englishQuestionText_not')
    english_question_text_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='englishQuestionText_in')
    english_question_text_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='englishQuestionText_not_in')
    english_question_text_contains = sgqlc.types.Field(String, graphql_name='englishQuestionText_contains')
    english_question_text_not_contains = sgqlc.types.Field(String, graphql_name='englishQuestionText_not_contains')
    english_question_text_starts_with = sgqlc.types.Field(String, graphql_name='englishQuestionText_starts_with')
    english_question_text_not_starts_with = sgqlc.types.Field(String, graphql_name='englishQuestionText_not_starts_with')
    english_question_text_ends_with = sgqlc.types.Field(String, graphql_name='englishQuestionText_ends_with')
    english_question_text_not_ends_with = sgqlc.types.Field(String, graphql_name='englishQuestionText_not_ends_with')
    french_question_text = sgqlc.types.Field(String, graphql_name='frenchQuestionText')
    french_question_text_not = sgqlc.types.Field(String, graphql_name='frenchQuestionText_not')
    french_question_text_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='frenchQuestionText_in')
    french_question_text_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='frenchQuestionText_not_in')
    french_question_text_contains = sgqlc.types.Field(String, graphql_name='frenchQuestionText_contains')
    french_question_text_not_contains = sgqlc.types.Field(String, graphql_name='frenchQuestionText_not_contains')
    french_question_text_starts_with = sgqlc.types.Field(String, graphql_name='frenchQuestionText_starts_with')
    french_question_text_not_starts_with = sgqlc.types.Field(String, graphql_name='frenchQuestionText_not_starts_with')
    french_question_text_ends_with = sgqlc.types.Field(String, graphql_name='frenchQuestionText_ends_with')
    french_question_text_not_ends_with = sgqlc.types.Field(String, graphql_name='frenchQuestionText_not_ends_with')
    survey_response = sgqlc.types.Field('_SurveyResponseFilter', graphql_name='surveyResponse')
    survey_response_not = sgqlc.types.Field('_SurveyResponseFilter', graphql_name='surveyResponse_not')
    survey_response_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyResponseFilter')), graphql_name='surveyResponse_in')
    survey_response_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyResponseFilter')), graphql_name='surveyResponse_not_in')
    answer = sgqlc.types.Field(_AnswerFilter, graphql_name='answer')
    answer_not = sgqlc.types.Field(_AnswerFilter, graphql_name='answer_not')
    answer_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_AnswerFilter)), graphql_name='answer_in')
    answer_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_AnswerFilter)), graphql_name='answer_not_in')


class _QuestionInput(sgqlc.types.Input):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')


class _RespondentFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_RespondentFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_RespondentFilter')), graphql_name='OR')
    uid = sgqlc.types.Field(ID, graphql_name='uid')
    uid_not = sgqlc.types.Field(ID, graphql_name='uid_not')
    uid_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_in')
    uid_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_not_in')
    uid_contains = sgqlc.types.Field(ID, graphql_name='uid_contains')
    uid_not_contains = sgqlc.types.Field(ID, graphql_name='uid_not_contains')
    uid_starts_with = sgqlc.types.Field(ID, graphql_name='uid_starts_with')
    uid_not_starts_with = sgqlc.types.Field(ID, graphql_name='uid_not_starts_with')
    uid_ends_with = sgqlc.types.Field(ID, graphql_name='uid_ends_with')
    uid_not_ends_with = sgqlc.types.Field(ID, graphql_name='uid_not_ends_with')
    user_agent = sgqlc.types.Field(String, graphql_name='userAgent')
    user_agent_not = sgqlc.types.Field(String, graphql_name='userAgent_not')
    user_agent_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userAgent_in')
    user_agent_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userAgent_not_in')
    user_agent_contains = sgqlc.types.Field(String, graphql_name='userAgent_contains')
    user_agent_not_contains = sgqlc.types.Field(String, graphql_name='userAgent_not_contains')
    user_agent_starts_with = sgqlc.types.Field(String, graphql_name='userAgent_starts_with')
    user_agent_not_starts_with = sgqlc.types.Field(String, graphql_name='userAgent_not_starts_with')
    user_agent_ends_with = sgqlc.types.Field(String, graphql_name='userAgent_ends_with')
    user_agent_not_ends_with = sgqlc.types.Field(String, graphql_name='userAgent_not_ends_with')
    survey_entry_method = sgqlc.types.Field(String, graphql_name='surveyEntryMethod')
    survey_entry_method_not = sgqlc.types.Field(String, graphql_name='surveyEntryMethod_not')
    survey_entry_method_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='surveyEntryMethod_in')
    survey_entry_method_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='surveyEntryMethod_not_in')
    survey_entry_method_contains = sgqlc.types.Field(String, graphql_name='surveyEntryMethod_contains')
    survey_entry_method_not_contains = sgqlc.types.Field(String, graphql_name='surveyEntryMethod_not_contains')
    survey_entry_method_starts_with = sgqlc.types.Field(String, graphql_name='surveyEntryMethod_starts_with')
    survey_entry_method_not_starts_with = sgqlc.types.Field(String, graphql_name='surveyEntryMethod_not_starts_with')
    survey_entry_method_ends_with = sgqlc.types.Field(String, graphql_name='surveyEntryMethod_ends_with')
    survey_entry_method_not_ends_with = sgqlc.types.Field(String, graphql_name='surveyEntryMethod_not_ends_with')
    response_language = sgqlc.types.Field(String, graphql_name='responseLanguage')
    response_language_not = sgqlc.types.Field(String, graphql_name='responseLanguage_not')
    response_language_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='responseLanguage_in')
    response_language_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='responseLanguage_not_in')
    response_language_contains = sgqlc.types.Field(String, graphql_name='responseLanguage_contains')
    response_language_not_contains = sgqlc.types.Field(String, graphql_name='responseLanguage_not_contains')
    response_language_starts_with = sgqlc.types.Field(String, graphql_name='responseLanguage_starts_with')
    response_language_not_starts_with = sgqlc.types.Field(String, graphql_name='responseLanguage_not_starts_with')
    response_language_ends_with = sgqlc.types.Field(String, graphql_name='responseLanguage_ends_with')
    response_language_not_ends_with = sgqlc.types.Field(String, graphql_name='responseLanguage_not_ends_with')
    department = sgqlc.types.Field(String, graphql_name='department')
    department_not = sgqlc.types.Field(String, graphql_name='department_not')
    department_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='department_in')
    department_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='department_not_in')
    department_contains = sgqlc.types.Field(String, graphql_name='department_contains')
    department_not_contains = sgqlc.types.Field(String, graphql_name='department_not_contains')
    department_starts_with = sgqlc.types.Field(String, graphql_name='department_starts_with')
    department_not_starts_with = sgqlc.types.Field(String, graphql_name='department_not_starts_with')
    department_ends_with = sgqlc.types.Field(String, graphql_name='department_ends_with')
    department_not_ends_with = sgqlc.types.Field(String, graphql_name='department_not_ends_with')
    classification = sgqlc.types.Field(String, graphql_name='classification')
    classification_not = sgqlc.types.Field(String, graphql_name='classification_not')
    classification_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='classification_in')
    classification_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='classification_not_in')
    classification_contains = sgqlc.types.Field(String, graphql_name='classification_contains')
    classification_not_contains = sgqlc.types.Field(String, graphql_name='classification_not_contains')
    classification_starts_with = sgqlc.types.Field(String, graphql_name='classification_starts_with')
    classification_not_starts_with = sgqlc.types.Field(String, graphql_name='classification_not_starts_with')
    classification_ends_with = sgqlc.types.Field(String, graphql_name='classification_ends_with')
    classification_not_ends_with = sgqlc.types.Field(String, graphql_name='classification_not_ends_with')
    location = sgqlc.types.Field(String, graphql_name='location')
    location_not = sgqlc.types.Field(String, graphql_name='location_not')
    location_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='location_in')
    location_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='location_not_in')
    location_contains = sgqlc.types.Field(String, graphql_name='location_contains')
    location_not_contains = sgqlc.types.Field(String, graphql_name='location_not_contains')
    location_starts_with = sgqlc.types.Field(String, graphql_name='location_starts_with')
    location_not_starts_with = sgqlc.types.Field(String, graphql_name='location_not_starts_with')
    location_ends_with = sgqlc.types.Field(String, graphql_name='location_ends_with')
    location_not_ends_with = sgqlc.types.Field(String, graphql_name='location_not_ends_with')
    additional_data = sgqlc.types.Field(String, graphql_name='additionalData')
    additional_data_not = sgqlc.types.Field(String, graphql_name='additionalData_not')
    additional_data_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='additionalData_in')
    additional_data_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='additionalData_not_in')
    additional_data_contains = sgqlc.types.Field(String, graphql_name='additionalData_contains')
    additional_data_not_contains = sgqlc.types.Field(String, graphql_name='additionalData_not_contains')
    additional_data_starts_with = sgqlc.types.Field(String, graphql_name='additionalData_starts_with')
    additional_data_not_starts_with = sgqlc.types.Field(String, graphql_name='additionalData_not_starts_with')
    additional_data_ends_with = sgqlc.types.Field(String, graphql_name='additionalData_ends_with')
    additional_data_not_ends_with = sgqlc.types.Field(String, graphql_name='additionalData_not_ends_with')
    survey_response = sgqlc.types.Field('_SurveyResponseFilter', graphql_name='surveyResponse')
    survey_response_not = sgqlc.types.Field('_SurveyResponseFilter', graphql_name='surveyResponse_not')
    survey_response_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyResponseFilter')), graphql_name='surveyResponse_in')
    survey_response_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyResponseFilter')), graphql_name='surveyResponse_not_in')


class _RespondentInput(sgqlc.types.Input):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')


class _SurveyFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyFilter')), graphql_name='OR')
    uid = sgqlc.types.Field(ID, graphql_name='uid')
    uid_not = sgqlc.types.Field(ID, graphql_name='uid_not')
    uid_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_in')
    uid_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_not_in')
    uid_contains = sgqlc.types.Field(ID, graphql_name='uid_contains')
    uid_not_contains = sgqlc.types.Field(ID, graphql_name='uid_not_contains')
    uid_starts_with = sgqlc.types.Field(ID, graphql_name='uid_starts_with')
    uid_not_starts_with = sgqlc.types.Field(ID, graphql_name='uid_not_starts_with')
    uid_ends_with = sgqlc.types.Field(ID, graphql_name='uid_ends_with')
    uid_not_ends_with = sgqlc.types.Field(ID, graphql_name='uid_not_ends_with')
    unique_name = sgqlc.types.Field(String, graphql_name='uniqueName')
    unique_name_not = sgqlc.types.Field(String, graphql_name='uniqueName_not')
    unique_name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uniqueName_in')
    unique_name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='uniqueName_not_in')
    unique_name_contains = sgqlc.types.Field(String, graphql_name='uniqueName_contains')
    unique_name_not_contains = sgqlc.types.Field(String, graphql_name='uniqueName_not_contains')
    unique_name_starts_with = sgqlc.types.Field(String, graphql_name='uniqueName_starts_with')
    unique_name_not_starts_with = sgqlc.types.Field(String, graphql_name='uniqueName_not_starts_with')
    unique_name_ends_with = sgqlc.types.Field(String, graphql_name='uniqueName_ends_with')
    unique_name_not_ends_with = sgqlc.types.Field(String, graphql_name='uniqueName_not_ends_with')
    created_at = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_not')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='createdAt_not_in')
    created_at_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_gte')
    latest = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='latest')
    latest_not = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='latest_not')
    latest_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='latest_in')
    latest_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='latest_not_in')
    versions = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='versions')
    versions_not = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='versions_not')
    versions_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='versions_in')
    versions_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='versions_not_in')
    versions_some = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='versions_some')
    versions_none = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='versions_none')
    versions_single = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='versions_single')
    versions_every = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='versions_every')


class _SurveyInput(sgqlc.types.Input):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')


class _SurveyMetricsFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyMetricsFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyMetricsFilter')), graphql_name='OR')
    uid = sgqlc.types.Field(ID, graphql_name='uid')
    uid_not = sgqlc.types.Field(ID, graphql_name='uid_not')
    uid_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_in')
    uid_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_not_in')
    uid_contains = sgqlc.types.Field(ID, graphql_name='uid_contains')
    uid_not_contains = sgqlc.types.Field(ID, graphql_name='uid_not_contains')
    uid_starts_with = sgqlc.types.Field(ID, graphql_name='uid_starts_with')
    uid_not_starts_with = sgqlc.types.Field(ID, graphql_name='uid_not_starts_with')
    uid_ends_with = sgqlc.types.Field(ID, graphql_name='uid_ends_with')
    uid_not_ends_with = sgqlc.types.Field(ID, graphql_name='uid_not_ends_with')
    metrics = sgqlc.types.Field(String, graphql_name='metrics')
    metrics_not = sgqlc.types.Field(String, graphql_name='metrics_not')
    metrics_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metrics_in')
    metrics_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metrics_not_in')
    metrics_contains = sgqlc.types.Field(String, graphql_name='metrics_contains')
    metrics_not_contains = sgqlc.types.Field(String, graphql_name='metrics_not_contains')
    metrics_starts_with = sgqlc.types.Field(String, graphql_name='metrics_starts_with')
    metrics_not_starts_with = sgqlc.types.Field(String, graphql_name='metrics_not_starts_with')
    metrics_ends_with = sgqlc.types.Field(String, graphql_name='metrics_ends_with')
    metrics_not_ends_with = sgqlc.types.Field(String, graphql_name='metrics_not_ends_with')
    processed_on = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='processedOn')
    processed_on_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='processedOn_not')
    processed_on_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='processedOn_in')
    processed_on_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='processedOn_not_in')
    processed_on_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='processedOn_lt')
    processed_on_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='processedOn_lte')
    processed_on_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='processedOn_gt')
    processed_on_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='processedOn_gte')
    survey_template = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='surveyTemplate')
    survey_template_not = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='surveyTemplate_not')
    survey_template_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='surveyTemplate_in')
    survey_template_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='surveyTemplate_not_in')


class _SurveyMetricsInput(sgqlc.types.Input):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')


class _SurveyResponseFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyResponseFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyResponseFilter')), graphql_name='OR')
    uid = sgqlc.types.Field(ID, graphql_name='uid')
    uid_not = sgqlc.types.Field(ID, graphql_name='uid_not')
    uid_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_in')
    uid_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_not_in')
    uid_contains = sgqlc.types.Field(ID, graphql_name='uid_contains')
    uid_not_contains = sgqlc.types.Field(ID, graphql_name='uid_not_contains')
    uid_starts_with = sgqlc.types.Field(ID, graphql_name='uid_starts_with')
    uid_not_starts_with = sgqlc.types.Field(ID, graphql_name='uid_not_starts_with')
    uid_ends_with = sgqlc.types.Field(ID, graphql_name='uid_ends_with')
    uid_not_ends_with = sgqlc.types.Field(ID, graphql_name='uid_not_ends_with')
    raw_data = sgqlc.types.Field(String, graphql_name='rawData')
    raw_data_not = sgqlc.types.Field(String, graphql_name='rawData_not')
    raw_data_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rawData_in')
    raw_data_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rawData_not_in')
    raw_data_contains = sgqlc.types.Field(String, graphql_name='rawData_contains')
    raw_data_not_contains = sgqlc.types.Field(String, graphql_name='rawData_not_contains')
    raw_data_starts_with = sgqlc.types.Field(String, graphql_name='rawData_starts_with')
    raw_data_not_starts_with = sgqlc.types.Field(String, graphql_name='rawData_not_starts_with')
    raw_data_ends_with = sgqlc.types.Field(String, graphql_name='rawData_ends_with')
    raw_data_not_ends_with = sgqlc.types.Field(String, graphql_name='rawData_not_ends_with')
    processed_data = sgqlc.types.Field(String, graphql_name='processedData')
    processed_data_not = sgqlc.types.Field(String, graphql_name='processedData_not')
    processed_data_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='processedData_in')
    processed_data_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='processedData_not_in')
    processed_data_contains = sgqlc.types.Field(String, graphql_name='processedData_contains')
    processed_data_not_contains = sgqlc.types.Field(String, graphql_name='processedData_not_contains')
    processed_data_starts_with = sgqlc.types.Field(String, graphql_name='processedData_starts_with')
    processed_data_not_starts_with = sgqlc.types.Field(String, graphql_name='processedData_not_starts_with')
    processed_data_ends_with = sgqlc.types.Field(String, graphql_name='processedData_ends_with')
    processed_data_not_ends_with = sgqlc.types.Field(String, graphql_name='processedData_not_ends_with')
    created_at = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_not')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='createdAt_not_in')
    created_at_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_gte')
    started_on = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn')
    started_on_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_not')
    started_on_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='startedOn_in')
    started_on_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='startedOn_not_in')
    started_on_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_lt')
    started_on_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_lte')
    started_on_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_gt')
    started_on_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='startedOn_gte')
    completed_on = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='completedOn')
    completed_on_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='completedOn_not')
    completed_on_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='completedOn_in')
    completed_on_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='completedOn_not_in')
    completed_on_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='completedOn_lt')
    completed_on_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='completedOn_lte')
    completed_on_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='completedOn_gt')
    completed_on_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='completedOn_gte')
    survey_template = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='surveyTemplate')
    survey_template_not = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='surveyTemplate_not')
    survey_template_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='surveyTemplate_in')
    survey_template_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='surveyTemplate_not_in')
    answered_questions = sgqlc.types.Field(_QuestionFilter, graphql_name='answeredQuestions')
    answered_questions_not = sgqlc.types.Field(_QuestionFilter, graphql_name='answeredQuestions_not')
    answered_questions_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_QuestionFilter)), graphql_name='answeredQuestions_in')
    answered_questions_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_QuestionFilter)), graphql_name='answeredQuestions_not_in')
    answered_questions_some = sgqlc.types.Field(_QuestionFilter, graphql_name='answeredQuestions_some')
    answered_questions_none = sgqlc.types.Field(_QuestionFilter, graphql_name='answeredQuestions_none')
    answered_questions_single = sgqlc.types.Field(_QuestionFilter, graphql_name='answeredQuestions_single')
    answered_questions_every = sgqlc.types.Field(_QuestionFilter, graphql_name='answeredQuestions_every')
    respondent = sgqlc.types.Field(_RespondentFilter, graphql_name='respondent')
    respondent_not = sgqlc.types.Field(_RespondentFilter, graphql_name='respondent_not')
    respondent_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_RespondentFilter)), graphql_name='respondent_in')
    respondent_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_RespondentFilter)), graphql_name='respondent_not_in')


class _SurveyResponseInput(sgqlc.types.Input):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')


class _SurveyTemplateFilter(sgqlc.types.Input):
    __schema__ = schema
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='OR')
    uid = sgqlc.types.Field(ID, graphql_name='uid')
    uid_not = sgqlc.types.Field(ID, graphql_name='uid_not')
    uid_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_in')
    uid_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='uid_not_in')
    uid_contains = sgqlc.types.Field(ID, graphql_name='uid_contains')
    uid_not_contains = sgqlc.types.Field(ID, graphql_name='uid_not_contains')
    uid_starts_with = sgqlc.types.Field(ID, graphql_name='uid_starts_with')
    uid_not_starts_with = sgqlc.types.Field(ID, graphql_name='uid_not_starts_with')
    uid_ends_with = sgqlc.types.Field(ID, graphql_name='uid_ends_with')
    uid_not_ends_with = sgqlc.types.Field(ID, graphql_name='uid_not_ends_with')
    survey_template = sgqlc.types.Field(String, graphql_name='surveyTemplate')
    survey_template_not = sgqlc.types.Field(String, graphql_name='surveyTemplate_not')
    survey_template_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='surveyTemplate_in')
    survey_template_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='surveyTemplate_not_in')
    survey_template_contains = sgqlc.types.Field(String, graphql_name='surveyTemplate_contains')
    survey_template_not_contains = sgqlc.types.Field(String, graphql_name='surveyTemplate_not_contains')
    survey_template_starts_with = sgqlc.types.Field(String, graphql_name='surveyTemplate_starts_with')
    survey_template_not_starts_with = sgqlc.types.Field(String, graphql_name='surveyTemplate_not_starts_with')
    survey_template_ends_with = sgqlc.types.Field(String, graphql_name='surveyTemplate_ends_with')
    survey_template_not_ends_with = sgqlc.types.Field(String, graphql_name='surveyTemplate_not_ends_with')
    version_number = sgqlc.types.Field(Int, graphql_name='versionNumber')
    version_number_not = sgqlc.types.Field(Int, graphql_name='versionNumber_not')
    version_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='versionNumber_in')
    version_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='versionNumber_not_in')
    version_number_lt = sgqlc.types.Field(Int, graphql_name='versionNumber_lt')
    version_number_lte = sgqlc.types.Field(Int, graphql_name='versionNumber_lte')
    version_number_gt = sgqlc.types.Field(Int, graphql_name='versionNumber_gt')
    version_number_gte = sgqlc.types.Field(Int, graphql_name='versionNumber_gte')
    evalese = sgqlc.types.Field(String, graphql_name='evalese')
    evalese_not = sgqlc.types.Field(String, graphql_name='evalese_not')
    evalese_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='evalese_in')
    evalese_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='evalese_not_in')
    evalese_contains = sgqlc.types.Field(String, graphql_name='evalese_contains')
    evalese_not_contains = sgqlc.types.Field(String, graphql_name='evalese_not_contains')
    evalese_starts_with = sgqlc.types.Field(String, graphql_name='evalese_starts_with')
    evalese_not_starts_with = sgqlc.types.Field(String, graphql_name='evalese_not_starts_with')
    evalese_ends_with = sgqlc.types.Field(String, graphql_name='evalese_ends_with')
    evalese_not_ends_with = sgqlc.types.Field(String, graphql_name='evalese_not_ends_with')
    created_at = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt')
    created_at_not = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_not')
    created_at_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='createdAt_in')
    created_at_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_Neo4jDateTimeInput)), graphql_name='createdAt_not_in')
    created_at_lt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_lt')
    created_at_lte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_lte')
    created_at_gt = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_gt')
    created_at_gte = sgqlc.types.Field(_Neo4jDateTimeInput, graphql_name='createdAt_gte')
    survey = sgqlc.types.Field(_SurveyFilter, graphql_name='survey')
    survey_not = sgqlc.types.Field(_SurveyFilter, graphql_name='survey_not')
    survey_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_SurveyFilter)), graphql_name='survey_in')
    survey_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_SurveyFilter)), graphql_name='survey_not_in')
    responses = sgqlc.types.Field(_SurveyResponseFilter, graphql_name='responses')
    responses_not = sgqlc.types.Field(_SurveyResponseFilter, graphql_name='responses_not')
    responses_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_SurveyResponseFilter)), graphql_name='responses_in')
    responses_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_SurveyResponseFilter)), graphql_name='responses_not_in')
    responses_some = sgqlc.types.Field(_SurveyResponseFilter, graphql_name='responses_some')
    responses_none = sgqlc.types.Field(_SurveyResponseFilter, graphql_name='responses_none')
    responses_single = sgqlc.types.Field(_SurveyResponseFilter, graphql_name='responses_single')
    responses_every = sgqlc.types.Field(_SurveyResponseFilter, graphql_name='responses_every')
    previous_version = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='previousVersion')
    previous_version_not = sgqlc.types.Field('_SurveyTemplateFilter', graphql_name='previousVersion_not')
    previous_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='previousVersion_in')
    previous_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('_SurveyTemplateFilter')), graphql_name='previousVersion_not_in')
    survey_metrics = sgqlc.types.Field(_SurveyMetricsFilter, graphql_name='surveyMetrics')
    survey_metrics_not = sgqlc.types.Field(_SurveyMetricsFilter, graphql_name='surveyMetrics_not')
    survey_metrics_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_SurveyMetricsFilter)), graphql_name='surveyMetrics_in')
    survey_metrics_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(_SurveyMetricsFilter)), graphql_name='surveyMetrics_not_in')


class _SurveyTemplateInput(sgqlc.types.Input):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')



########################################################################
# Output Objects and Interfaces
########################################################################
class Answer(sgqlc.types.Type):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')
    answer = sgqlc.types.Field(String, graphql_name='answer')
    calculated_metrics = sgqlc.types.Field(String, graphql_name='calculatedMetrics')
    processed_on = sgqlc.types.Field('_Neo4jDateTime', graphql_name='processedOn')
    question = sgqlc.types.Field('Question', graphql_name='question', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_QuestionFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    create_survey = sgqlc.types.Field('Survey', graphql_name='CreateSurvey', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('unique_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uniqueName', default=None)),
        ('created_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='createdAt', default=None)),
))
    )
    update_survey = sgqlc.types.Field('Survey', graphql_name='UpdateSurvey', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
        ('unique_name', sgqlc.types.Arg(String, graphql_name='uniqueName', default=None)),
        ('created_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='createdAt', default=None)),
))
    )
    delete_survey = sgqlc.types.Field('Survey', graphql_name='DeleteSurvey', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
))
    )
    add_survey_latest = sgqlc.types.Field('_AddSurveyLatestPayload', graphql_name='AddSurveyLatest', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='to', default=None)),
))
    )
    remove_survey_latest = sgqlc.types.Field('_RemoveSurveyLatestPayload', graphql_name='RemoveSurveyLatest', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='to', default=None)),
))
    )
    add_survey_versions = sgqlc.types.Field('_AddSurveyVersionsPayload', graphql_name='AddSurveyVersions', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='to', default=None)),
))
    )
    remove_survey_versions = sgqlc.types.Field('_RemoveSurveyVersionsPayload', graphql_name='RemoveSurveyVersions', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='to', default=None)),
))
    )
    create_survey_template = sgqlc.types.Field('SurveyTemplate', graphql_name='CreateSurveyTemplate', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('survey_template', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='surveyTemplate', default=None)),
        ('version_number', sgqlc.types.Arg(Int, graphql_name='versionNumber', default=None)),
        ('evalese', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='evalese', default=None)),
        ('created_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='createdAt', default=None)),
))
    )
    update_survey_template = sgqlc.types.Field('SurveyTemplate', graphql_name='UpdateSurveyTemplate', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
        ('survey_template', sgqlc.types.Arg(String, graphql_name='surveyTemplate', default=None)),
        ('version_number', sgqlc.types.Arg(Int, graphql_name='versionNumber', default=None)),
        ('evalese', sgqlc.types.Arg(String, graphql_name='evalese', default=None)),
        ('created_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='createdAt', default=None)),
))
    )
    delete_survey_template = sgqlc.types.Field('SurveyTemplate', graphql_name='DeleteSurveyTemplate', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
))
    )
    add_survey_template_survey = sgqlc.types.Field('_AddSurveyTemplateSurveyPayload', graphql_name='AddSurveyTemplateSurvey', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='to', default=None)),
))
    )
    remove_survey_template_survey = sgqlc.types.Field('_RemoveSurveyTemplateSurveyPayload', graphql_name='RemoveSurveyTemplateSurvey', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='to', default=None)),
))
    )
    add_survey_template_responses = sgqlc.types.Field('_AddSurveyTemplateResponsesPayload', graphql_name='AddSurveyTemplateResponses', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='to', default=None)),
))
    )
    remove_survey_template_responses = sgqlc.types.Field('_RemoveSurveyTemplateResponsesPayload', graphql_name='RemoveSurveyTemplateResponses', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='to', default=None)),
))
    )
    add_survey_template_previous_version = sgqlc.types.Field('_AddSurveyTemplatePreviousVersionPayload', graphql_name='AddSurveyTemplatePreviousVersion', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='to', default=None)),
))
    )
    remove_survey_template_previous_version = sgqlc.types.Field('_RemoveSurveyTemplatePreviousVersionPayload', graphql_name='RemoveSurveyTemplatePreviousVersion', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='to', default=None)),
))
    )
    add_survey_template_survey_metrics = sgqlc.types.Field('_AddSurveyTemplateSurveyMetricsPayload', graphql_name='AddSurveyTemplateSurveyMetrics', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyMetricsInput), graphql_name='to', default=None)),
))
    )
    remove_survey_template_survey_metrics = sgqlc.types.Field('_RemoveSurveyTemplateSurveyMetricsPayload', graphql_name='RemoveSurveyTemplateSurveyMetrics', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyMetricsInput), graphql_name='to', default=None)),
))
    )
    create_survey_metrics = sgqlc.types.Field('SurveyMetrics', graphql_name='CreateSurveyMetrics', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('metrics', sgqlc.types.Arg(String, graphql_name='metrics', default=None)),
        ('processed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='processedOn', default=None)),
))
    )
    update_survey_metrics = sgqlc.types.Field('SurveyMetrics', graphql_name='UpdateSurveyMetrics', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
        ('metrics', sgqlc.types.Arg(String, graphql_name='metrics', default=None)),
        ('processed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='processedOn', default=None)),
))
    )
    delete_survey_metrics = sgqlc.types.Field('SurveyMetrics', graphql_name='DeleteSurveyMetrics', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
))
    )
    add_survey_metrics_survey_template = sgqlc.types.Field('_AddSurveyMetricsSurveyTemplatePayload', graphql_name='AddSurveyMetricsSurveyTemplate', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyMetricsInput), graphql_name='to', default=None)),
))
    )
    remove_survey_metrics_survey_template = sgqlc.types.Field('_RemoveSurveyMetricsSurveyTemplatePayload', graphql_name='RemoveSurveyMetricsSurveyTemplate', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyMetricsInput), graphql_name='to', default=None)),
))
    )
    create_survey_response = sgqlc.types.Field('SurveyResponse', graphql_name='CreateSurveyResponse', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('raw_data', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='rawData', default=None)),
        ('processed_data', sgqlc.types.Arg(String, graphql_name='processedData', default=None)),
        ('created_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='createdAt', default=None)),
        ('started_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startedOn', default=None)),
        ('completed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='completedOn', default=None)),
))
    )
    update_survey_response = sgqlc.types.Field('SurveyResponse', graphql_name='UpdateSurveyResponse', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
        ('raw_data', sgqlc.types.Arg(String, graphql_name='rawData', default=None)),
        ('processed_data', sgqlc.types.Arg(String, graphql_name='processedData', default=None)),
        ('created_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='createdAt', default=None)),
        ('started_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startedOn', default=None)),
        ('completed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='completedOn', default=None)),
))
    )
    delete_survey_response = sgqlc.types.Field('SurveyResponse', graphql_name='DeleteSurveyResponse', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
))
    )
    add_survey_response_survey_template = sgqlc.types.Field('_AddSurveyResponseSurveyTemplatePayload', graphql_name='AddSurveyResponseSurveyTemplate', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='to', default=None)),
))
    )
    remove_survey_response_survey_template = sgqlc.types.Field('_RemoveSurveyResponseSurveyTemplatePayload', graphql_name='RemoveSurveyResponseSurveyTemplate', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyTemplateInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='to', default=None)),
))
    )
    add_survey_response_answered_questions = sgqlc.types.Field('_AddSurveyResponseAnsweredQuestionsPayload', graphql_name='AddSurveyResponseAnsweredQuestions', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_QuestionInput), graphql_name='to', default=None)),
))
    )
    remove_survey_response_answered_questions = sgqlc.types.Field('_RemoveSurveyResponseAnsweredQuestionsPayload', graphql_name='RemoveSurveyResponseAnsweredQuestions', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_QuestionInput), graphql_name='to', default=None)),
))
    )
    add_survey_response_respondent = sgqlc.types.Field('_AddSurveyResponseRespondentPayload', graphql_name='AddSurveyResponseRespondent', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_RespondentInput), graphql_name='to', default=None)),
))
    )
    remove_survey_response_respondent = sgqlc.types.Field('_RemoveSurveyResponseRespondentPayload', graphql_name='RemoveSurveyResponseRespondent', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_RespondentInput), graphql_name='to', default=None)),
))
    )
    create_respondent = sgqlc.types.Field('Respondent', graphql_name='CreateRespondent', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('user_agent', sgqlc.types.Arg(String, graphql_name='userAgent', default=None)),
        ('survey_entry_method', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='surveyEntryMethod', default=None)),
        ('response_language', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='responseLanguage', default=None)),
        ('department', sgqlc.types.Arg(String, graphql_name='department', default=None)),
        ('classification', sgqlc.types.Arg(String, graphql_name='classification', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('additional_data', sgqlc.types.Arg(String, graphql_name='additionalData', default=None)),
))
    )
    update_respondent = sgqlc.types.Field('Respondent', graphql_name='UpdateRespondent', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
        ('user_agent', sgqlc.types.Arg(String, graphql_name='userAgent', default=None)),
        ('survey_entry_method', sgqlc.types.Arg(String, graphql_name='surveyEntryMethod', default=None)),
        ('response_language', sgqlc.types.Arg(String, graphql_name='responseLanguage', default=None)),
        ('department', sgqlc.types.Arg(String, graphql_name='department', default=None)),
        ('classification', sgqlc.types.Arg(String, graphql_name='classification', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('additional_data', sgqlc.types.Arg(String, graphql_name='additionalData', default=None)),
))
    )
    delete_respondent = sgqlc.types.Field('Respondent', graphql_name='DeleteRespondent', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
))
    )
    add_respondent_survey_response = sgqlc.types.Field('_AddRespondentSurveyResponsePayload', graphql_name='AddRespondentSurveyResponse', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_RespondentInput), graphql_name='to', default=None)),
))
    )
    remove_respondent_survey_response = sgqlc.types.Field('_RemoveRespondentSurveyResponsePayload', graphql_name='RemoveRespondentSurveyResponse', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_RespondentInput), graphql_name='to', default=None)),
))
    )
    create_question = sgqlc.types.Field('Question', graphql_name='CreateQuestion', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('question_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='questionId', default=None)),
        ('question_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='questionType', default=None)),
        ('classified_as', sgqlc.types.Arg(String, graphql_name='classifiedAs', default=None)),
        ('at_order', sgqlc.types.Arg(Int, graphql_name='atOrder', default=None)),
        ('english_question_text', sgqlc.types.Arg(String, graphql_name='englishQuestionText', default=None)),
        ('french_question_text', sgqlc.types.Arg(String, graphql_name='frenchQuestionText', default=None)),
))
    )
    update_question = sgqlc.types.Field('Question', graphql_name='UpdateQuestion', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
        ('question_id', sgqlc.types.Arg(String, graphql_name='questionId', default=None)),
        ('question_type', sgqlc.types.Arg(String, graphql_name='questionType', default=None)),
        ('classified_as', sgqlc.types.Arg(String, graphql_name='classifiedAs', default=None)),
        ('at_order', sgqlc.types.Arg(Int, graphql_name='atOrder', default=None)),
        ('english_question_text', sgqlc.types.Arg(String, graphql_name='englishQuestionText', default=None)),
        ('french_question_text', sgqlc.types.Arg(String, graphql_name='frenchQuestionText', default=None)),
))
    )
    delete_question = sgqlc.types.Field('Question', graphql_name='DeleteQuestion', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
))
    )
    add_question_survey_response = sgqlc.types.Field('_AddQuestionSurveyResponsePayload', graphql_name='AddQuestionSurveyResponse', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_QuestionInput), graphql_name='to', default=None)),
))
    )
    remove_question_survey_response = sgqlc.types.Field('_RemoveQuestionSurveyResponsePayload', graphql_name='RemoveQuestionSurveyResponse', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_SurveyResponseInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_QuestionInput), graphql_name='to', default=None)),
))
    )
    add_question_answer = sgqlc.types.Field('_AddQuestionAnswerPayload', graphql_name='AddQuestionAnswer', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_QuestionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_AnswerInput), graphql_name='to', default=None)),
))
    )
    remove_question_answer = sgqlc.types.Field('_RemoveQuestionAnswerPayload', graphql_name='RemoveQuestionAnswer', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_QuestionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_AnswerInput), graphql_name='to', default=None)),
))
    )
    create_answer = sgqlc.types.Field(Answer, graphql_name='CreateAnswer', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('answer', sgqlc.types.Arg(String, graphql_name='answer', default=None)),
        ('calculated_metrics', sgqlc.types.Arg(String, graphql_name='calculatedMetrics', default=None)),
        ('processed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='processedOn', default=None)),
))
    )
    update_answer = sgqlc.types.Field(Answer, graphql_name='UpdateAnswer', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
        ('answer', sgqlc.types.Arg(String, graphql_name='answer', default=None)),
        ('calculated_metrics', sgqlc.types.Arg(String, graphql_name='calculatedMetrics', default=None)),
        ('processed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='processedOn', default=None)),
))
    )
    delete_answer = sgqlc.types.Field(Answer, graphql_name='DeleteAnswer', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='uid', default=None)),
))
    )
    add_answer_question = sgqlc.types.Field('_AddAnswerQuestionPayload', graphql_name='AddAnswerQuestion', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_QuestionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_AnswerInput), graphql_name='to', default=None)),
))
    )
    remove_answer_question = sgqlc.types.Field('_RemoveAnswerQuestionPayload', graphql_name='RemoveAnswerQuestion', args=sgqlc.types.ArgDict((
        ('from_', sgqlc.types.Arg(sgqlc.types.non_null(_QuestionInput), graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(sgqlc.types.non_null(_AnswerInput), graphql_name='to', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = schema
    survey = sgqlc.types.Field(sgqlc.types.list_of('Survey'), graphql_name='Survey', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('unique_name', sgqlc.types.Arg(String, graphql_name='uniqueName', default=None)),
        ('created_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='createdAt', default=None)),
        ('versions_count', sgqlc.types.Arg(Int, graphql_name='versionsCount', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SurveyOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SurveyFilter, graphql_name='filter', default=None)),
))
    )
    survey_template = sgqlc.types.Field(sgqlc.types.list_of('SurveyTemplate'), graphql_name='SurveyTemplate', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('survey_template', sgqlc.types.Arg(String, graphql_name='surveyTemplate', default=None)),
        ('version_number', sgqlc.types.Arg(Int, graphql_name='versionNumber', default=None)),
        ('evalese', sgqlc.types.Arg(String, graphql_name='evalese', default=None)),
        ('created_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='createdAt', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SurveyTemplateOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SurveyTemplateFilter, graphql_name='filter', default=None)),
))
    )
    survey_metrics = sgqlc.types.Field(sgqlc.types.list_of('SurveyMetrics'), graphql_name='SurveyMetrics', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('metrics', sgqlc.types.Arg(String, graphql_name='metrics', default=None)),
        ('processed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='processedOn', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SurveyMetricsOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SurveyMetricsFilter, graphql_name='filter', default=None)),
))
    )
    survey_response = sgqlc.types.Field(sgqlc.types.list_of('SurveyResponse'), graphql_name='SurveyResponse', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('raw_data', sgqlc.types.Arg(String, graphql_name='rawData', default=None)),
        ('processed_data', sgqlc.types.Arg(String, graphql_name='processedData', default=None)),
        ('created_at', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='createdAt', default=None)),
        ('started_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='startedOn', default=None)),
        ('completed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='completedOn', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SurveyResponseOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SurveyResponseFilter, graphql_name='filter', default=None)),
))
    )
    respondent = sgqlc.types.Field(sgqlc.types.list_of('Respondent'), graphql_name='Respondent', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('user_agent', sgqlc.types.Arg(String, graphql_name='userAgent', default=None)),
        ('survey_entry_method', sgqlc.types.Arg(String, graphql_name='surveyEntryMethod', default=None)),
        ('response_language', sgqlc.types.Arg(String, graphql_name='responseLanguage', default=None)),
        ('department', sgqlc.types.Arg(String, graphql_name='department', default=None)),
        ('classification', sgqlc.types.Arg(String, graphql_name='classification', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('additional_data', sgqlc.types.Arg(String, graphql_name='additionalData', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_RespondentOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_RespondentFilter, graphql_name='filter', default=None)),
))
    )
    question = sgqlc.types.Field(sgqlc.types.list_of('Question'), graphql_name='Question', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('question_id', sgqlc.types.Arg(String, graphql_name='questionId', default=None)),
        ('question_type', sgqlc.types.Arg(String, graphql_name='questionType', default=None)),
        ('classified_as', sgqlc.types.Arg(String, graphql_name='classifiedAs', default=None)),
        ('at_order', sgqlc.types.Arg(Int, graphql_name='atOrder', default=None)),
        ('english_question_text', sgqlc.types.Arg(String, graphql_name='englishQuestionText', default=None)),
        ('french_question_text', sgqlc.types.Arg(String, graphql_name='frenchQuestionText', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_QuestionOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_QuestionFilter, graphql_name='filter', default=None)),
))
    )
    answer = sgqlc.types.Field(sgqlc.types.list_of(Answer), graphql_name='Answer', args=sgqlc.types.ArgDict((
        ('uid', sgqlc.types.Arg(ID, graphql_name='uid', default=None)),
        ('answer', sgqlc.types.Arg(String, graphql_name='answer', default=None)),
        ('calculated_metrics', sgqlc.types.Arg(String, graphql_name='calculatedMetrics', default=None)),
        ('processed_on', sgqlc.types.Arg(_Neo4jDateTimeInput, graphql_name='processedOn', default=None)),
        ('_id', sgqlc.types.Arg(String, graphql_name='_id', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_AnswerOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_AnswerFilter, graphql_name='filter', default=None)),
))
    )


class Question(sgqlc.types.Type):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')
    question_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='questionId')
    question_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='questionType')
    classified_as = sgqlc.types.Field(String, graphql_name='classifiedAs')
    at_order = sgqlc.types.Field(Int, graphql_name='atOrder')
    english_question_text = sgqlc.types.Field(String, graphql_name='englishQuestionText')
    french_question_text = sgqlc.types.Field(String, graphql_name='frenchQuestionText')
    survey_response = sgqlc.types.Field('SurveyResponse', graphql_name='surveyResponse', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_SurveyResponseFilter, graphql_name='filter', default=None)),
))
    )
    answer = sgqlc.types.Field(Answer, graphql_name='answer', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_AnswerFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Respondent(sgqlc.types.Type):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')
    user_agent = sgqlc.types.Field(String, graphql_name='userAgent')
    survey_entry_method = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='surveyEntryMethod')
    response_language = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='responseLanguage')
    department = sgqlc.types.Field(String, graphql_name='department')
    classification = sgqlc.types.Field(String, graphql_name='classification')
    location = sgqlc.types.Field(String, graphql_name='location')
    additional_data = sgqlc.types.Field(String, graphql_name='additionalData')
    survey_response = sgqlc.types.Field('SurveyResponse', graphql_name='surveyResponse', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_SurveyResponseFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class Survey(sgqlc.types.Type):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')
    unique_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uniqueName')
    created_at = sgqlc.types.Field('_Neo4jDateTime', graphql_name='createdAt')
    latest = sgqlc.types.Field('SurveyTemplate', graphql_name='latest', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_SurveyTemplateFilter, graphql_name='filter', default=None)),
))
    )
    versions = sgqlc.types.Field(sgqlc.types.list_of('SurveyTemplate'), graphql_name='versions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SurveyTemplateOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SurveyTemplateFilter, graphql_name='filter', default=None)),
))
    )
    versions_count = sgqlc.types.Field(Int, graphql_name='versionsCount')
    _id = sgqlc.types.Field(String, graphql_name='_id')


class SurveyMetrics(sgqlc.types.Type):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')
    metrics = sgqlc.types.Field(String, graphql_name='metrics')
    processed_on = sgqlc.types.Field('_Neo4jDateTime', graphql_name='processedOn')
    survey_template = sgqlc.types.Field('SurveyTemplate', graphql_name='surveyTemplate', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_SurveyTemplateFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class SurveyResponse(sgqlc.types.Type):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')
    raw_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rawData')
    processed_data = sgqlc.types.Field(String, graphql_name='processedData')
    created_at = sgqlc.types.Field('_Neo4jDateTime', graphql_name='createdAt')
    started_on = sgqlc.types.Field('_Neo4jDateTime', graphql_name='startedOn')
    completed_on = sgqlc.types.Field('_Neo4jDateTime', graphql_name='completedOn')
    survey_template = sgqlc.types.Field('SurveyTemplate', graphql_name='surveyTemplate', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_SurveyTemplateFilter, graphql_name='filter', default=None)),
))
    )
    answered_questions = sgqlc.types.Field(sgqlc.types.list_of(Question), graphql_name='answeredQuestions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_QuestionOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_QuestionFilter, graphql_name='filter', default=None)),
))
    )
    respondent = sgqlc.types.Field(Respondent, graphql_name='respondent', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_RespondentFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class SurveyTemplate(sgqlc.types.Type):
    __schema__ = schema
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uid')
    survey_template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='surveyTemplate')
    version_number = sgqlc.types.Field(Int, graphql_name='versionNumber')
    evalese = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='evalese')
    created_at = sgqlc.types.Field('_Neo4jDateTime', graphql_name='createdAt')
    survey = sgqlc.types.Field(Survey, graphql_name='survey', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_SurveyFilter, graphql_name='filter', default=None)),
))
    )
    responses = sgqlc.types.Field(sgqlc.types.list_of(SurveyResponse), graphql_name='responses', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(_SurveyResponseOrdering), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(_SurveyResponseFilter, graphql_name='filter', default=None)),
))
    )
    previous_version = sgqlc.types.Field('SurveyTemplate', graphql_name='previousVersion', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_SurveyTemplateFilter, graphql_name='filter', default=None)),
))
    )
    survey_metrics = sgqlc.types.Field(SurveyMetrics, graphql_name='surveyMetrics', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(_SurveyMetricsFilter, graphql_name='filter', default=None)),
))
    )
    _id = sgqlc.types.Field(String, graphql_name='_id')


class _AddAnswerQuestionPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Question, graphql_name='from')
    to = sgqlc.types.Field(Answer, graphql_name='to')


class _AddQuestionAnswerPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Question, graphql_name='from')
    to = sgqlc.types.Field(Answer, graphql_name='to')


class _AddQuestionSurveyResponsePayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyResponse, graphql_name='from')
    to = sgqlc.types.Field(Question, graphql_name='to')


class _AddRespondentSurveyResponsePayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyResponse, graphql_name='from')
    to = sgqlc.types.Field(Respondent, graphql_name='to')


class _AddSurveyLatestPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Survey, graphql_name='from')
    to = sgqlc.types.Field(SurveyTemplate, graphql_name='to')


class _AddSurveyMetricsSurveyTemplatePayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyMetrics, graphql_name='to')


class _AddSurveyResponseAnsweredQuestionsPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyResponse, graphql_name='from')
    to = sgqlc.types.Field(Question, graphql_name='to')


class _AddSurveyResponseRespondentPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyResponse, graphql_name='from')
    to = sgqlc.types.Field(Respondent, graphql_name='to')


class _AddSurveyResponseSurveyTemplatePayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyResponse, graphql_name='to')


class _AddSurveyTemplatePreviousVersionPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyTemplate, graphql_name='to')


class _AddSurveyTemplateResponsesPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyResponse, graphql_name='to')


class _AddSurveyTemplateSurveyMetricsPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyMetrics, graphql_name='to')


class _AddSurveyTemplateSurveyPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Survey, graphql_name='from')
    to = sgqlc.types.Field(SurveyTemplate, graphql_name='to')


class _AddSurveyVersionsPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Survey, graphql_name='from')
    to = sgqlc.types.Field(SurveyTemplate, graphql_name='to')


class _Neo4jDate(sgqlc.types.Type):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jDateTime(sgqlc.types.Type):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalDateTime(sgqlc.types.Type):
    __schema__ = schema
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jLocalTime(sgqlc.types.Type):
    __schema__ = schema
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _Neo4jTime(sgqlc.types.Type):
    __schema__ = schema
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    second = sgqlc.types.Field(Int, graphql_name='second')
    millisecond = sgqlc.types.Field(Int, graphql_name='millisecond')
    microsecond = sgqlc.types.Field(Int, graphql_name='microsecond')
    nanosecond = sgqlc.types.Field(Int, graphql_name='nanosecond')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    formatted = sgqlc.types.Field(String, graphql_name='formatted')


class _RemoveAnswerQuestionPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Question, graphql_name='from')
    to = sgqlc.types.Field(Answer, graphql_name='to')


class _RemoveQuestionAnswerPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Question, graphql_name='from')
    to = sgqlc.types.Field(Answer, graphql_name='to')


class _RemoveQuestionSurveyResponsePayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyResponse, graphql_name='from')
    to = sgqlc.types.Field(Question, graphql_name='to')


class _RemoveRespondentSurveyResponsePayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyResponse, graphql_name='from')
    to = sgqlc.types.Field(Respondent, graphql_name='to')


class _RemoveSurveyLatestPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Survey, graphql_name='from')
    to = sgqlc.types.Field(SurveyTemplate, graphql_name='to')


class _RemoveSurveyMetricsSurveyTemplatePayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyMetrics, graphql_name='to')


class _RemoveSurveyResponseAnsweredQuestionsPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyResponse, graphql_name='from')
    to = sgqlc.types.Field(Question, graphql_name='to')


class _RemoveSurveyResponseRespondentPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyResponse, graphql_name='from')
    to = sgqlc.types.Field(Respondent, graphql_name='to')


class _RemoveSurveyResponseSurveyTemplatePayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyResponse, graphql_name='to')


class _RemoveSurveyTemplatePreviousVersionPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyTemplate, graphql_name='to')


class _RemoveSurveyTemplateResponsesPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyResponse, graphql_name='to')


class _RemoveSurveyTemplateSurveyMetricsPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(SurveyTemplate, graphql_name='from')
    to = sgqlc.types.Field(SurveyMetrics, graphql_name='to')


class _RemoveSurveyTemplateSurveyPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Survey, graphql_name='from')
    to = sgqlc.types.Field(SurveyTemplate, graphql_name='to')


class _RemoveSurveyVersionsPayload(sgqlc.types.Type):
    __schema__ = schema
    from_ = sgqlc.types.Field(Survey, graphql_name='from')
    to = sgqlc.types.Field(SurveyTemplate, graphql_name='to')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

