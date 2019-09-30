"Singleton pattern for GraphQL endpoint rather than using flask system and g"

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

class GraphQLEndpoint():
    class __GraphQLEndpoint():
        def __init__(self, url, headers):
            self.endpoint = HTTPEndpoint(url, headers)
        def query(self, *args, **kwargs):
            native_objects = None
            if "native_objects" in kwargs:
                native_objects = kwargs["native_objects"]
            data = self.endpoint(*args, **kwargs)
            if isinstance(args[0], Operation):
                if native_objects == True:
                    return (args[0] + data)
            return data
    
    instance = None
    def __init__(self, url = None, headers= None):
        if not GraphQLEndpoint.instance:
            if url is None:
                raise ValueError("parameter url must be provided for first time that endpoint is initialised")
            GraphQLEndpoint.instance = GraphQLEndpoint.__GraphQLEndpoint(url, headers)
    def __getattr__(self, name):
        return getattr(self.instance, name)


        