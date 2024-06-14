import re

def validate_string(s):
    match_all = re.findall(r"([a-zA-Z]+|\d+|[\+\=\-\*\/]+)", s)
    errors = []
    corrects = match_all

    rule_letters = re.findall(r"[a-zA-Z]{2,}", s)
    rule_operators = re.findall(r"[\+\=\-\*\/]{2,}", s)

    if rule_letters:
        errors.extend(rule_letters)
    if rule_operators:
        errors.extend(rule_operators)

    corrects = [c for c in corrects if c not in errors]

    return {'Hay ': len(errors), ' Errores. Estos son': errors, 'Hay': len(corrects), ' Correctos. Estos son los corrects': corrects}

lexema = input("Ingrese aqui su lexema: ")
print(validate_string(lexema))