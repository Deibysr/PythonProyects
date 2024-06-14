import re

def evaluate_expression(expression):
    # Usamos una expresión regular para identificar números, operadores y variables
    print("Intermediate expression: ",expression)
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

# Ejemplo de uso
final_result = evaluate_expression("c + d + f / g - H * U")
print("Final result:", final_result)
