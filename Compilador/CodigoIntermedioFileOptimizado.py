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
    print("Intermediate expression:", expression)
    tokens = re.findall(r'[a-zA-Z_]+|\d+|[*/+-]', expression.replace(' ', ''))
    output = []
    temp_var_count = 1

    def process_operators(tokens, operators):
        nonlocal temp_var_count
        new_tokens = []
        i = 0
        while i < len(tokens):
            if tokens[i] in operators:
                left = new_tokens.pop()  # take the last item in new_tokens
                right = tokens[i+1]
                operator = tokens[i]
                result = f"R{temp_var_count}"
                temp_var_count += 1
                output.append(f"{result} = {left} {operator} {right}")
                new_tokens.append(result)
                i += 2  # skip next token because it's already processed
            else:
                new_tokens.append(tokens[i])
                i += 1
        return new_tokens

    # Process '*' and '/'
    tokens = process_operators(tokens, '*/')
    print("After */ processing:", ' '.join(tokens))

    # Process '+' and '-'
    tokens = process_operators(tokens, '+-')
    print("After +- processing:", ' '.join(tokens))

    for line in output:
        print(line)

    return tokens[0]

# Uso de la función modificada
file_path = 'read.py'  # Asegúrate de que este archivo exista y tenga las expresiones adecuadas
results = evaluate_expression_from_file(file_path)
for idx, res in enumerate(results):
    print(f"Result of expression {idx+1}:", res)
