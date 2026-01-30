from rest_framework.validators import ValidationError

def no_number(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Name should not contain numbers')