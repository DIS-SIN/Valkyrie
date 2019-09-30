from .base_dao import BaseGraphQL
from flask import current_app
from src.utils.nlp.google import GoogleNaturalLanguageAPIClient


class ResponseQuestionGraphQL(BaseGraphQL):

    def __init__(self, **kwargs):
        answer = kwargs.pop("answer", None)
        self.answer = answer
    
        surveyResponseUID = kwargs.pop("surveyResponseUID", None)
        self.surveyResponseUID = surveyResponseUID
        
        super().__init__(model= "Question", **kwargs)

    def create_response_question(self, surveyResponseUID = None):
        if self.surveyResponseUID is None and surveyResponseUID is not None and surveyResponseUID != "":
            self.surveyResponseUID = surveyResponseUID
        # pylint: disable=no-member
        if not hasattr(self, "questionId") or self.questionId is None:
            raise ValueError("questionId is required to create a question")
        if not hasattr(self, "surveyResponseUID") or self.surveyResponseUID is None or self.surveyResponseUID == "":
            raise ValueError("surveyResponseUID is required ro create a question")
        if not hasattr(self, "answer") or self.answer is None:
            raise ValueError("answer is required to create question response")
        
        # define the mutations
        question_mutation = {
            "CreateQuestion":{
                "values":{
                    "questionId": self.questionId,
                    "englishQuestionText": getattr(self,"englishQuestionText", ""),
                    "frenchQuestionText": getattr(self, "frenchQuestionText", ""),
                    "atOrder": getattr(self, "atOrder", ""),
                    "classifiedAs": getattr(self, "classifiedAs", ""),
                    "questionType": getattr(self, "questionType", "")
                },
                "fields" : [
                    "uid"
                ]
            }
        }

        answer_mutation = {
            "CreateAnswer": {
                "values": {
                    "answer": self.answer
                },
                "fields": [
                    "uid"
                ]
            }
        }

        question_answer_mutation = {
            "AddAnswerQuestion":{
                "values": {
                    "from": {
                        "type": "_QuestionInput",
                        "values": {
                            "uid": {
                                "reference": "CreateQuestion.uid"
                            }
                        }
                    },
                    "to": {
                        "type": "_AnswerInput",
                        "values": {
                            "uid": {
                                "reference": "CreateAnswer.uid"
                            }
                        }
                    }
                },
                "fields": [
                    {
                        "from": {
                            "type": "_QuestionInput",
                            "fields": [
                                "uid"
                            ]
                        }
                    },
                    {
                        "to": {
                            "type": "_AnswerInput",
                            "fields": [
                                "uid"
                            ]
                        }
                    }
                ]
            }
        }

        survey_response_question_mutation = {
            "AddQuestionSurveyResponse":{
                "values": {
                    "from": {
                        "type": "_SurveyResponseInput",
                        "values": {
                            "uid": self.surveyResponseUID
                        }
                    },
                    "to": {
                        "type": "_QuestionInput",
                        "values": {
                            "uid": {
                                "reference": "CreateQuestion.uid"
                            }
                        }
                    }
                }

            }
        }

        mutation_sequence = [
            question_mutation,
            answer_mutation,
            survey_response_question_mutation,
            question_answer_mutation
        ]

        data = super().mutate(mutation_sequence)

        return data["CreateQuestion"]["uid"]



class ResponseQuestionsGraphQL:
    """
    Wrapper class for ResponseQuestionGraphQL which will instatiate them based on the data in the template
    and response

    Parameters
    ----------
    surveyUID: str
        The UID of the survey
    surveyTemplateUID: str
        The UID of the template
    surveyTemplate: dict
        The survey template 
    data: dict
        The response data

    Note
    -----

    If the template is invalid the constructor for this class will raise a ValueError
    """
    def __init__(self, surveyUID, surveyTemplateUID, surveyTemplate, data, surveyResponseUID = None):
        self.surveyUID = surveyUID
        self.surveyTemplateUID = surveyTemplateUID
        self.surveyTemplate = surveyTemplate
        self.data = data
        self.surveyResponseUID = surveyResponseUID

    @property
    def processedQuestions(self):
        if not hasattr(self, "_processedQuestions"):
            self._processedQuestions = None
        return self._processedQuestions 
    
    @property
    def surveyTemplate(self):
        if not hasattr(self, "_surveyTemplate"):
            self._surveyTemplate = None
        return self._surveyTemplate
    
    @surveyTemplate.setter
    def surveyTemplate(self, surveyTemplate):
        if not isinstance(surveyTemplate, dict):
            type_name = type(surveyTemplate).__name__ 
            raise TypeError( 
                f"surveyTemplate must be of type dict, found {type_name}"
            )
        
        template_questions = surveyTemplate.get("questions")
        if template_questions is None:
            raise ValueError("surveyTemplate does not contain any questions")

        # create a dictionary of questions with the keys being their id's for easy access
        template_questions_filtered = {}
   
        for question in template_questions:
            # get the dict where all the valid keys are stuffed
            cortex_question_info = question.get("cortexQuestionInfo")
            if cortex_question_info is not None:     
                question_id = cortex_question_info.get("questionId")
                if question_id is not None and question_id != "none" and question_id.strip(" ") != "":
                    template_questions_filtered[question_id] = cortex_question_info
            
        self._processedQuestions = template_questions_filtered

        # if the data is not None then the template has been re -et and in this case the data setter should be recalled
        if self.data is not None:
            self.data = self.data

    @property
    def answerdQuestions(self):
        if not hasattr(self, "_answerdQuestions"):
            self._answerdQuestions = None
        return self._answerdQuestions
    
    @property
    def data(self):
        if not hasattr(self, "_data"):
            self._data = None
        return self._data
    
    @data.setter
    def data(self, data):
        # getting the survey template questions
        processed_questions = self.processedQuestions
        answerdQuestions = {}
        if processed_questions is None:
            raise ValueError( 
                "Survey Template has not been set. Survey Template must be added " +
                "before the data is set"
            )
        
        if not isinstance(data, dict):
            type_name = type(data).__name__
            raise TypeError(
                f"data must be of type dict, found type {type_name}"
            )
        # go through the question dict and append the answer to the dict
        for question in data:
            question_data = processed_questions.get(question)
            if question_data is None:
                raise ValueError( 
                    f"question {question} does not exist in template {self.surveyTemplateUID} " +
                    f"for survey {self.surveyUID}. "
                )
            answerdQuestions[question] = {**question_data, "answer": data[question]}
        
        self._answerdQuestions = answerdQuestions

        if self.surveyResponseUID is not None:
            self.surveyResponseUID = self.surveyResponseUID
    
    @property
    def questionsGraphQL(self):
        if not hasattr(self, "_questionsGraphQL"):
            self._questionsGraphQL = None
        return self._questionsGraphQL
    @property
    def surveyResponseUID(self):
        if not hasattr(self, "_surveyResponseUID"):
            self._surveyResponseUID = None
        return self._surveyResponseUID
    
    @surveyResponseUID.setter
    def surveyResponseUID(self, surveyResponseUID):
        if surveyResponseUID is None:
            return
        elif not isinstance(surveyResponseUID, str):
            type_name = type(surveyResponseUID).__name__
            raise TypeError( 
                f"surveyResponseUID must be of type str, recieved type {type_name}"
            )
        # get the processed questions
        answered_questions = self.answerdQuestions
        if answered_questions is None:
            raise ValueError(
               "survey template and response data must be set first before setting the surveyResponseUID"
            )
        
        questionsGraphQL = []

        # append the Question DAO objects
        for question in answered_questions:
            questionsGraphQL.append(
               ResponseQuestionGraphQL(
                   **answered_questions[question], 
                   surveyResponseUID = surveyResponseUID)
            )
        
        self._questionsGraphQL = questionsGraphQL

    def create_response_questions(self, surveyResponseUID = None):
        
        if surveyResponseUID is not None and self.surveyResponseUID != surveyResponseUID:
            self.surveyResponseUID = surveyResponseUID

        questionsGraphQL = self.questionsGraphQL

        question_data = []
        for question in questionsGraphQL:
            question_uid = question.create_response_question(surveyResponseUID)
            question_data.append(question_uid)
        
        return question_data
    
    def calculate_sentiment(self):
        if current_app.config.get("ENABLE_NATURAL_LANGUAGE_PROCESSING") == True:
            client = GoogleNaturalLanguageAPIClient()
            answered_questions = self.answerdQuestions
            sentiment_dict = {}
            for question in answered_questions:
                question_info  = answered_questions[question]
                question_classification = question_info.get("questionType")
                if question_classification == "FREE_TEXT":
                    question_answer = question_info.get("answer")
                    if question_answer is not None and question_answer != "":
                        scores = client.analyze_tex_sentiment(
                            question_answer
                        )
                        sentiment_dict[question + "_sentimentScore"] = scores.get("sentimentScore")
                        sentiment_dict[question + "_magnitudeScore"] = scores.get("magnitudeScore")
            return sentiment_dict
        return {}









        
        

    
            
            
            
        




    

    
