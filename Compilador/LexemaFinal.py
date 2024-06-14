import re

# Definimos las expresiones regulares para los diferentes tipos de tokens correctos
token_patterns = {
    'Palabras Clave': r'\b(?:def|if|else|return|class|for|while)\b',
    'Identificadores': r'\b[a-zA-Z_][a-zA-Z_0-9]*\b',
    'Literales': r'\b\d+\b',
    'Operadores': r'[+\-*/=<>!]{1,2}',
    'Símbolos de Puntuación': r'[;,.(){}[\]]',
    'Espacios en Blanco': r'\s+',
    'Comentarios': r'#.*'
}

# Definimos las expresiones regulares para patrones incorrectos
token_patterns_error = [
    r'\b\d+[a-zA-Z_][a-zA-Z0-9]*\b', # Identificadores que comienzan con un número
    r'[áéíóúÁÉÍÓÚñÑ]',              # Caracteres con tildes o acentos
    r'[+\-*/=<>!]{3,}',              # Más de dos signos de operación seguidos
    r'(?<!\b)[-+*/=<>!]\d+'          # Número precedido inmediatamente por un operador (excepto el menos si es negativo)
]

# Esta función verifica si el token es un error
def es_error(token):
    for pattern in token_patterns_error:
        if re.search(pattern, token):
            return True
    return False

# Esta función analiza una línea del archivo
def analizar_linea(linea, num_linea):
    resultados = []
    pos = 0
    while pos < len(linea):
        encontrado = False
        # Verificar primero si algún patrón de error se aplica
        for pattern in token_patterns_error:
            regex = re.compile(pattern)
            match = regex.match(linea, pos)
            if match:
                token = match.group(0)
                resultados.append(f'Línea {num_linea}: {token} - Token Erróneo')
                pos = match.end()
                encontrado = True
                break

        if not encontrado:
            # Buscar tokens correctos
            for tipo, pattern in token_patterns.items():
                regex = re.compile(pattern)
                match = regex.match(linea, pos)
                if match:
                    token = match.group(0)
                    if tipo != 'Espacios en Blanco':
                        resultados.append(f'Línea {num_linea}: {token} - {tipo}')
                    pos = match.end()
                    break
            else:
                pos += 1  # Incrementar la posición si no se encontró coincidencia

    return resultados

# Función principal que lee el archivo, analiza cada línea y escribe los resultados
def analizar_archivo(nombre_archivo_entrada, nombre_archivo_salida):
    with open(nombre_archivo_entrada, 'r') as archivo_entrada, open(nombre_archivo_salida, 'w') as archivo_salida:
        num_linea = 1
        for linea in archivo_entrada:
            resultados = analizar_linea(linea, num_linea)
            for resultado in resultados:
                archivo_salida.write(resultado + '\n')
            num_linea += 1

# Ejecutamos la función para analizar el archivo
analizar_archivo('read.py', 'LexicoResult.txt')
