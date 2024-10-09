import re

def invalid_name(value: str):
    pattern = r'^[A-Za-z\s]+$'
    return not re.match(pattern, value)

def invalid_age(value):
    pattern = r'^\d+\s+(dia|dias|mes|meses|ano|anos)$'
    return not re.match(pattern, value)
