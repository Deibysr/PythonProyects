from PIL import Image


def comprimir_imagen(ruta_imagen_original, ruta_imagen_comprimida, calidad=85):
    # Abrir la imagen original
    imagen = Image.open(ruta_imagen_original)

    # Comprimir y guardar la imagen
    imagen.save(ruta_imagen_comprimida, 'PNG', quality=calidad)


# Ejemplo de uso
ruta_imagen_original = 'imagen_original.png'
ruta_imagen_comprimida = 'imagen_comprimida.jpg'
# Ajusta este valor según la compresión deseada (0 a 100). Un valor menor resulta en mayor compresión y menor calidad.
calidad = 100

comprimir_imagen(ruta_imagen_original, ruta_imagen_comprimida, calidad)
