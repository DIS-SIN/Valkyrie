import os
import requests
import json
from logging import Handler, Formatter, NOTSET

class SlackHandler(Handler):
    def __init__(self, level=NOTSET, slack_url=None):
        super().__init__()
        if slack_url is None:
            application_name = os.environ.get(str(os.getpid()) + "_APPLICATION_NAME")
            if not application_name is None:
                self.slack_url = os.environ[application_name + "_SLACK_URL"]
        else:
            self.slack_url = slack_url
    def emit(self, record):
        formatted_log = self.format(record)
        requests.post(
            self.slack_url, 
            json.dumps({"text": formatted_log }), 
            headers={"Content-Type": "application/json"})