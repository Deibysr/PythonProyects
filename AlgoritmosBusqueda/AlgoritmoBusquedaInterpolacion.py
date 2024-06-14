def busqueda_por_interpolacion(arr, x):
    """
    Función de búsqueda por interpolación.
    
    :param arr: Arreglo ordenado donde se buscará el elemento.
    :param x: Elemento a buscar en el arreglo.
    :return: Índice del elemento en el arreglo o -1 si no se encuentra.
    """
    lo = 0
    hi = len(arr) - 1

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        # Calcula la posición probable de 'x' usando la fórmula de interpolación
        pos = lo + int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))

        # Si encontramos el elemento, retornamos la posición
        if arr[pos] == x:
            return pos

        # Si el elemento es mayor, x está en la parte superior
        if arr[pos] < x:
            lo = pos + 1
        # Si el elemento es menor, x está en la parte inferior
        else:
            hi = pos - 1

    return -1

# Arreglo ordenado para el ejemplo
arr = [2, 3, 4, 10, 14, 18, 21, 24, 30, 35]
x = 18  # Elemento que queremos buscar

# Llamamos a la función y mostramos el resultado
resultado = busqueda_por_interpolacion(arr, x)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado")