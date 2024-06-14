import re

def evaluate_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    results = []
    for expression in lines:
        print("Evaluating expression from file:", expression.strip())
        result = evaluate_expression(expression.strip())
        results.append(result)

    return results

def evaluate_expression(expression):
    # Usamos una expresión regular para identificar números, operadores y variables
    print("Intermediate expression:", expression)
    tokens = re.findall(r'[a-zA-Z_]+|\d+|[*/+-]', expression.replace(' ', ''))
    output = []
    temp_var_count = 1

    # Procesar la expresión original y realizar multiplicaciones y divisiones primero
    while '*' in tokens or '/' in tokens:
        for i, token in enumerate(tokens):
            if token in '*/':
                left = tokens[i-1]
                right = tokens[i+1]
                operator = token
                result = f"R{temp_var_count}"
                temp_var_count += 1
                output.append(f"{result} = {left} {operator} {right}")
                tokens[i] = result
                tokens.pop(i-1)
                tokens.pop(i)
                break
        print("Intermediate expression:", ' '.join(tokens))

    # Procesar sumas y restas
    while '+' in tokens or '-' in tokens:
        for i, token in enumerate(tokens):
            if token in '+-':
                left = tokens[i-1]
                right = tokens[i+1]
                operator = token
                result = f"R{temp_var_count}"
                temp_var_count += 1
                output.append(f"{result} = {left} {operator} {right}")
                tokens[i] = result
                tokens.pop(i-1)
                tokens.pop(i)
                break
        print("Intermediate expression:", ' '.join(tokens))

    # Imprimir todas las operaciones intermedias
    for line in output:
        print(line)

    return tokens[0]

# Uso de la función modificada
file_path = 'read.py'  # Asegúrate de que este archivo exista y tenga las expresiones adecuadas
results = evaluate_expression_from_file(file_path)
for idx, res in enumerate(results):
    print(f"Result of expression {idx+1}:", res)
