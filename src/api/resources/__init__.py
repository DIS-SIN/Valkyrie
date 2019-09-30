# pylint does not recognize decorator, disabled errors below 
# pylint: disable=unexpected-keyword-arg
# pylint: disable=too-many-function-args

from .v1 import register_v1_routes

def register_api_routes(app):
    register_v1_routes(app, "v1", current_version=True) 