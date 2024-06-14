Claro, aquí tienes el problema en español:

**Problema:**

Dada una cadena \( S \) que contiene solo dígitos del 0 al 9, queremos comprimir las ocurrencias consecutivas de cada carácter. Si un carácter 'c' aparece consecutivamente \( X \) veces en la cadena, debemos reemplazar estas ocurrencias consecutivas con \( (X, c) \).

**Formato de Entrada:**

Una línea de entrada que consiste en la cadena \( S \).

**Formato de Salida:**

Una línea de salida que consiste en la cadena modificada.

**Restricciones:**

- Todos los caracteres de \( S \) son dígitos entre 0 y 9.
- \( 1 \leq |S| \leq 10^4 \).

**Ejemplo:**

**Entrada:**
1222311


**Salida:**
(1, 1) (3, 2) (1, 3) (2, 1)


**Explicación:**

Primero, el carácter 1 ocurre solo una vez y se reemplaza por \( (1, 1) \). Luego, el carácter 2 ocurre tres veces y se reemplaza por \( (3, 2) \). Posteriormente, el carácter 3 ocurre solo una vez y se reemplaza por \( (1, 3) \). Finalmente, el carácter 1 ocurre dos veces y se reemplaza por \( (2, 1) \).

Además, nota que hay un espacio simple entre cada paréntesis y entre las compresiones.