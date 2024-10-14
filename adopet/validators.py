import re


def invalid_name(value: str):
    pattern = r"^[A-Za-z\s]+$"
    return not re.match(pattern, value)


def invalid_age(value: str):
    number = value.split()
    if number[0] == "1":
        # Aceita apenas "1 dia", "1 mes" ou "1 ano" no singular
        pattern = r"^1\s+(dia|mes|ano)$"
    else:
        # Aceita apenas "X dias", "X meses" ou "X anos" no plural para X > 1
        pattern = r"^[2-9]\d*\s+(dias|meses|anos)$"
    return not re.match(pattern, value)
