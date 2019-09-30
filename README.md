# Valkyrie 

## Summary

Valkeyrie is a python GraphQL client which serves as the evalhalla backend, providing simple REST routes to create, update and respond to surveys. If you are a curious on looker this repo is probably not as much valuable to you. Here is the Evalhalla application [repo](https://github.com/DIS-SIN/Evalhalla.git)

## Technologies used

In case you're interested. Valkyrie uses the following main components

- [Google Natural Language API](https://cloud.google.com/natural-language/docs/quickstarts): Used to get sentiment values for text
- [Flask](https://flask.palletsprojects.com/en/1.1.x/): Micro web framework for python
- [sgqlc](https://github.com/profusion/sgqlc): GraphQL client for python with schema introspection to generate native python object
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/): Utility to efficiently create API views

The GraphQL server is not included in this repo but the apollo server can be found in this [repo](https://github.com/DIS-SIN/Gungnir)

## Application Variables

Most variables can be set as either environment variables or variables in either [development.py](/src/config/development.py), [production.py](/src/config/production.py), or [default.py](/src/config/default.py) . As the names imply default.py applies for the development environment, production.py for the production environment and default.py for variables that exist across both environments. default.py variables will be overriden if the same variable exists in the development.py or the production.py in their respective environments.


### The Defaults


```APPLICATION_NAME```


**Explanation**: I am using a flask boilerplate that I created. So rather than hardcode the application name for some configs. I am using this config. This is also used as a means to ensure there are no environment variable naming collisions if I am running multiple applications on the same host. This name will be the pre-cursor to any environment variables i.e. ${APPLICATION_NAME}_WHATEVER_ENVIRONMENT_VARIABLE . This does not apply to the builtin Flask variables

**Value**: VALKYRIE

**Has Environment Variable**: No 

```RESTFUL_JSON```

**Explanation**: variable used to configure the Flask-RESTful utility such as enabling non ascii characters in the API.

**Value**: 
```json 
{
    "ensure_ascii": False
}
```

**Has Environment Variable**: No

```SEND_FILE_MAX_AGE_DEFAULT```

**Explanation**: builtin Flask variable which sets the caching time. 

**Value**: 0

**Has Environment Variable**: No


```VARIABLES```

**Explanation**: Rather than hard-coding the checks for different environment variables use JSON to dynamically check for requirements

**Value**:

```python
{
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
```


### Application Variables


**Note** : Variables with environment variables are in the form ${APPLICATION_NAME}_VARIABLE_NAME


```GRAPHQL_ENDPOINT```

**Explanation**: The graphql endpoint the client should call

**Required**: Yes

**Development Default**: http://localhost:4000/graphql

**Has Environment Variable**: Yes

```GRAPHQL_HEADERS```

**Explanation**: HTTP Headers if any to be used for requests to the graphQL endpoint

**Required**: No

**Has Environment Variable**: No

```SLACK_URL```

**Explanation**: The slack webhook used to post logs to custom slack bot according to the logging slack handler configuration

**Required**: Yes only if logging handler is defined and configured

**Has Environment Variable**: Yes

```ENABLE_NATURAL_LANGUAGE_PROCESSING```

**Explanation**: Flag to enable or disable natural language processing

**Required**: No

**Has Environment Variable**: Yes

```GOOGLE_APPLICATION_CREDENTIALS```

**ENVIRONMENT VARIABLE ONLY**

**Explanation**: The path to the JSON credentials file for the Google Natural Language API

**Required**: Yes, if ENABLE_NATURAL_LANGUAGE_PROCESSING is set to True





