import re

def invalid_name(name: str):
    return not name.isalpha()

def invalid_age(value):
    pattern = r'^\d+\s+(dia|dias|mes|meses|ano|anos)$'
    return not re.match(pattern, value)
