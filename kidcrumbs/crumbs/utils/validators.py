from django.core.exceptions import ValidationError
import re
def validate_location(value):
    '''
        This Method validates an input string representing the
        latitude and longitude of an area.
        The input string contains 2 floats seperated by a comma.
        It raises an error if these conditions are not met.
    '''
    try:
        latitude,longitude = value.split(',')
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        raise ValidationError('Please put in a latitude followed by a comma and then a longitude')
