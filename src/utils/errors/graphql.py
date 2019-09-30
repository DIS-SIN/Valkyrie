class GraphQLError(Exception):
    "An exception has occured from the graphql server"
    pass

class DataLogicError(Exception):
    "The data is not what was expected to be"
    pass