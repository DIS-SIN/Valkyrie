# APPLICATION_NAME environment variable is used to generalize hardcoded environment variables 

APPLICATION_NAME = "VALKYRIE"


RESTFUL_JSON = {
    "ensure_ascii": False
}
SEND_FILE_MAX_AGE_DEFAULT = 0

# This is used by the application factory to ensure the nessecary variables are present for operation
VARIABLES= {
    "GRAPHQL_ENDPOINT": {
        "description": "The graphql endpoint the client should call",
        "required": True,
        "default": "http://localhost:4000/graphql"
    },
    "GRAPHQL_HEADERS":{
        "description": "HTTP Headers if any to be used for requests to the graphQL endpoint",
        "required": False
    },
    "SLACK_URL":{
        "description": "The slack webhook endpoint to post logs to according to configuration",
        "required": False
    },
    "ENABLE_NATURAL_LANGUAGE_PROCESSING":{
        "description": "Flag to enable or disable natural language processing",
        "required": True,
        "default": True 
    }
}