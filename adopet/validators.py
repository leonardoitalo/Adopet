import re
from django.core.exceptions import ValidationError

def validate_age(value):
    pattern = r'^\d+\s+(dias|meses|anos)$'
    if not re.match(pattern, value):
        raise ValidationError(
            'A idade deve estar no formato "X dias", "X meses" ou "X anos", onde X é um número.'
        )
