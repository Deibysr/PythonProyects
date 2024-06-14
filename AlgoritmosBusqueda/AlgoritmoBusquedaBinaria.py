def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1

# Lista de libros ordenados alfabéticamente
libros = [
    "A Brief History of Time",
    "Brave New World",
    "Crime and Punishment",
    "Don Quixote",
    "Frankenstein",
    "Gone with the Wind",
    "Harry Potter and the Philosopher's Stone",
    "In Search of Lost Time",
    "Jane Eyre",
    "Les Misérables",
    "Moby-Dick",
    "Nineteen Eighty-Four",
    "Oliver Twist",
    "Pride and Prejudice",
    "Quiet: The Power of Introverts in a World That Can't Stop Talking",
    "Romeo and Juliet",
    "The Catcher in the Rye",
    "The Great Gatsby",
    "The Lord of the Rings",
    "Ulysses",
    "War and Peace"
]

# Libro que queremos encontrar
libro_buscado = "The Great Gatsby"

# Buscamos el libro en la lista
indice = busqueda_binaria(libros, libro_buscado)

if indice != -1:
    print(f"El libro '{libro_buscado}' se encontró en el índice {indice}.")
else:
    print(f"El libro '{libro_buscado}' no se encontró en la lista.")
