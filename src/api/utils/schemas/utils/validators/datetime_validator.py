from marshmallow import ValidationError
import re
import datetime


def validate_isodatetime_string_has_timezone(datetime_value):
    """
    Function to validate whether or not a iso format datetime string contains datetime information.
    Raises a validation error if this is not the case. 

    Paramters
    ---------
    datetime_string: str
        datetime string in ISO format 
    """

    if datetime_value is not None and datetime_value.tzinfo is None:
        raise ValidationError("DateTime must be timezone aware")  

