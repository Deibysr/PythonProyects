# Detalle del Problema
Se te proporciona un número n, el cual indica cuántas palabras vas a recibir como entrada. Cada una de estas n palabras puede aparecer una o más veces en la lista. Tu tarea es determinar cuántas palabras distintas hay en total y cuántas veces aparece cada una de estas palabras, manteniendo el orden en que aparecieron por primera vez.

# Requerimientos de la Salida
La primera línea de la salida debe contener el número total de palabras distintas en la entrada.
La segunda línea debe contener el número de veces que cada palabra distinta aparece, siguiendo el orden en que cada palabra fue introducida por primera vez.

## Ejemplo 1
**Entrada:**
```Copy code
4
manzana
pera
manzana
naranja
```

**Salida:**
```Copy code
3
2 1 1
```

### Explicación:
- La palabra "manzana" aparece dos veces.
- La palabra "pera" aparece una vez.
- La palabra "naranja" aparece una vez.
- Hay tres palabras distintas: "manzana", "pera", "naranja". En la salida, el número 2 corresponde a "manzana" que aparece dos veces, el 1 siguiente corresponde a "pera", y el último 1 corresponde a "naranja".


## Ejemplo 2
**Entrada:**

```Copy code
5
sol
luna
sol
estrella
luna
```

**Salida:**
```Copy code
3
2 2 1
```

### Explicación:
"sol" aparece dos veces.
"luna" aparece dos veces.
"estrella" aparece una vez.
Hay tres palabras distintas, y el orden de su primera aparición determina el orden en la salida.
Ejemplo 3

**Entrada:**
```Copy code
3
café
café
café
```

**Salida:**
```Copy code
1
3
```

### Explicación:
"café" aparece tres veces.
Solo hay una palabra distinta, y aparece tres veces.