from google.cloud import language
from google.cloud.language import enums 
from google.cloud.language import types


class GoogleNaturalLanguageAPIClient:
    client = None
    def __init__(self):
        if GoogleNaturalLanguageAPIClient.client is None:
            GoogleNaturalLanguageAPIClient.client = language.LanguageServiceClient()

    def analyze_tex_sentiment(self, text: str):
        # pylint: disable=no-member
        text_to_analyze = text.encode("utf-8")
        document = language.types.Document(
            content = text_to_analyze,
            type = "PLAIN_TEXT"
        )
        response = self.client.analyze_sentiment(
            document=  document,
            encoding_type = "UTF8"
        )
        return {
            "text": text_to_analyze.decode("utf-8"),
            "sentimentScore": response.document_sentiment.score,
            "magnitudeScore": response.document_sentiment.magnitude
        }
