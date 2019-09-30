from flask.blueprints import Blueprint
from flask_restful import Api

def register_api_version(routes_func):
    
    def exec_register_api_routes(app, version, current_version=False):
        if current_version:
            api_bp = Blueprint(name="current_api", import_name = __name__)
            api = Api(api_bp)
        else:
            api_bp = Blueprint(name=version, import_name = __name__)
            api = Api(api_bp, prefix= "/" + version)
        routes_func(api)
        app.register_blueprint(api_bp)
    
    return exec_register_api_routes


