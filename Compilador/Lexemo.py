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

    return {'Hay ': len(errors), 'Errores. Estos son': errors, 'Hay': len(corrects), 'Correctos. Estos son los correctos': corrects}

def analyze_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_number = 1
            for line in file:
                print(f"Línea {line_number}: {line.strip()}")
                result = validate_string(line)
                print(f"Resultado: {result}\n")
                line_number += 1
    except FileNotFoundError:
        print(f"No se encontró el archivo: {file_path}")

# Ruta al archivo que deseas analizar
file_path = "read.py"
analyze_file(file_path)
