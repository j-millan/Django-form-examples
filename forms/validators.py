from django.core.exceptions import ValidationError

def validate_contains_only_letters(value):
    if not value.isalpha():
        raise ValidationError(
            ('This value can only contain letters.'),
            params={'value' : value}
        )

def validate_minimum_length(value):
    if len(value) < 2:
        raise ValidationError(
            ('This value must be at least 2 characters long.'),
            params={'value' : value}
        )