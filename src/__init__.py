from flask import Flask
from .api import register_api_routes
from .utils.sgql_utils import GraphQLEndpoint
from .utils.nlp.google import GoogleNaturalLanguageAPIClient
from flask_cors import CORS
import os
import logging
import logging.config


def create_app(environment = "production"):
    # initialising application
    app = Flask(__name__)

    # enabling cors for the application
    CORS(app)

    # loading default configs, this must be present
    from src.config import defaut
    app.config.from_object(defaut)
    
    # check if APPLICATION_NAME was specified
    if app.config.get("APPLICATION_NAME") is None:
        raise ValueError("APPLICATION_NAME variable must be specified with the application name")
    else:
        # exporting application name with its pid as its prefix so that distint parts of the application that need to access this info without being able to directly access app configs
        os.environ[str(os.getpid()) + "_APPLICATION_NAME"] = app.config.get("APPLICATION_NAME")
    
    application_name = app.config["APPLICATION_NAME"]

    if environment == "production":
        # try loading production configs
        try:
            from src.config import production
            app.config.from_object(production)
        except ModuleNotFoundError:
            pass

        # try configuring logger if configuration is present
        if app.config.get("LOGGING_CONFIG") is not None:
            logging.config.dictConfig(app.config.get("LOGGING_CONFIG"))
            app.config["LOGGING_ENABLED"] = True
        else:
            app.config["LOGGING_ENABLED"] = False


    else:
        # try loading development configs
        try:
            from src.config import development
            app.config.from_object(development)
        except ModuleNotFoundError:
            pass

        # try configuring logger if configuration is present
        if app.config.get("LOGGING_CONFIG") is not None:
            logging.config.dictConfig(app.config.get("LOGGING_CONFIG"))
            app.config["LOGGING_ENABLED"] = True
        else:
            app.config["LOGGING_ENABLED"] = False
        
        # warn the user that the environment was not explicitly set to development
        if environment != "development":
            msg = (
                "Environment is development however this was not explicitely set. " +
                "Environment should be set as either production or development." +
                f"Environment is currently set as {environment}" 
            )
            if app.config["LOGGING_ENABLED"] == True:
                logging.warn(
                    msg
                )
            else:
                print(
                    "WARNING: " + msg
                )
        
    # use variables config to ensure all variables are present to run application

    if app.config.get("VARIABLES") is not None:
        for variable in app.config.get("VARIABLES"):
            variable_dict = app.config["VARIABLES"][variable]
            # variable is specified but does not exist
            if app.config.get(variable) is None:
                # check if value is in environment variable
                # environment variables are in the for, {APPLICATION_NAME}_{VARIABLE_NAME}
                env_name = application_name + "_" + variable
                env_val = os.environ.get(application_name + "_" + variable)
                # if the environment variable also does not exist 
                if env_val is None:
                    if variable_dict.get("required") == True:
                        # if the environment is in development load the default 
                        if environment != "production":
                            default = variable_dict.get("default")
                            # the application in this case will fail to start
                            # the variable was specified as required however does not exist as configuration varible in the py files or environment variables
                            # no default was also specified
                            if default is None:
                                raise ValueError(
                                    "Application failed to start\n" + 
                                    f"The variable {variable} was specified as required however " +
                                    "it does not exist as a configuration value in py configuration files " +
                                    f"and does not exist as its environment variable {env_name}. " +
                                    "No default was specified in the VARIABLE configuration. " +
                                    "Please revise your configuration for this variable" 
                                )
                            # set to default specified in the variable configuration dict
                            else:
                                app.config[variable] = variable_dict["default"]
                        # production environments behaviour is to fail if variable is required and does not exist as config value or environment variable
                        else:
                            raise ValueError(
                               "Application failed to start\n" + 
                               f"The variable {variable} was specified as required however " +
                               "it does not exist as a configuration value in py configuration files " +
                               f"and does not exist as its environment variable {env_name}. " +
                               "Please revise your configuration for this variable"
                            )
                    # variable is not required
                    else:
                        default = variable_dict.get("default")
                        
                        if environment != "production" and default is not None:
                            app.config[variable] = variable_dict["default"]
                else:
                    app.config[variable] = env_val
    
    # any other additional configurations go here

    # register api routes with application
    register_api_routes(app)

    # initialise endpoint singleton
    GraphQLEndpoint(app.config["GRAPHQL_ENDPOINT"], app.config.get("GRAPHQL_HEADERS"))

    if app.config.get("ENABLE_NATURAL_LANGUAGE_PROCESSING") == True:
        GoogleNaturalLanguageAPIClient()
    else:
        app.config["ENABLE_NATURAL_LANGUAGE_PROCESSING"] = False
    return app