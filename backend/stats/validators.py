from django.core.exceptions import ValidationError
import re
def validate_height(value):
    if not re.match(r'^\d{1,2}\'\d{1,2}"$', value):
        raise ValidationError('Height must be in the format X\'Y"')