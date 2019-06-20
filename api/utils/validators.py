from marshmallow import ValidationError


def validate_empty_string(string):
    if string.strip() == "":
        raise ValidationError('Field must not be blank')
