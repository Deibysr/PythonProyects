def busqueda_lineal_libros(libros, titulo_objetivo):
    for indice, libro in enumerate(libros):
        if libro['titulo'] == titulo_objetivo:
            return indice  # Libro encontrado
    return None  # Libro no encontrado

# Ejemplo de uso
mis_libros = [
    {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez'},
    {'titulo': 'La sombra del viento', 'autor': 'Carlos Ruiz Zafón'},
    {'titulo': 'El nombre del viento', 'autor': 'Patrick Rothfuss'},
    {'titulo': '1984', 'autor': 'George Orwell'}
]

titulo_objetivo = '1984'

resultado = busqueda_lineal_libros(mis_libros, titulo_objetivo)

if resultado is not None:
    print(f"El libro '{titulo_objetivo}' se encontró en el índice {resultado}.")
else:
    print(f"El libro '{titulo_objetivo}' no se encuentra en la colección.")
