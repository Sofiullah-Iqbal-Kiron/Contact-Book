from django.core.exceptions import ValidationError


def phone_number_validator(number: str):
    if not number.isnumeric:
        raise ValidationError("Numbers must be numeric!")
