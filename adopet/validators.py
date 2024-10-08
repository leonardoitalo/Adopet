import re

def invalid_name(name: str):
    return not name.isalpha()

def invalid_age(value):
    pattern = r'^\d+\s+(dias|meses|anos)$'
    return not re.match(pattern, value)
