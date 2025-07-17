# Ejercicio 1
# Imprime cada palabra de la lista en una línea diferente
'''palabras = ["hola", "mundo", "python", "programación"]

for i in palabras:
    print(i)'''

# Ejercicio 2
# Cuenta cuántas palabras contienen la letra "a"
'''palabras = ["casa", "sol", "lago", "nube", "ratón"]
total = 0

for i in palabras:
    if 'a' in i:
        total += 1

print(total)
'''
# Ejercicio 3
# Muestra solo las palabras que tienen más de 5 letras
'''palabras = ["elefante", "sol", "montaña", "mar", "tigre"]

for i in palabras:
    if len(i) > 5:
        print(i)
'''

# Ejercicio 4
# Imprime las palabras en mayúsculas
'''palabras = ["perro", "gato", "pez", "caballo"]

for i in palabras:
    print(i.upper())
'''

# Ejercicio 5
# Cuenta cuántas palabras terminan en vocal
'''palabras = ["mesa", "sillón", "televisión", "ventana", "puerta"]

for i in palabras:
    if i.endswith(('a', 'e', 'i', 'o', 'u')):
        print(i)
'''

# Ejercicio 6
# Muestra las palabras que comienzan con "p"
'''palabras = ["pantalla", "ratón", "piedra", "mesa", "papel"]

for i in palabras:
    if i.startswith('p'):
        print(i)
'''

# Ejercicio 7
# Imprime la longitud de cada palabra
'''palabras = ["cielo", "nube", "tormenta", "viento", "lluvia"]

for i in palabras:
    print(len(i))
'''

# Ejercicio 8
# Muestra las palabras que tienen exactamente 4 letras
'''palabras = ["luz", "sola", "vida", "mar", "azul"]

for i in palabras:
    if len(i) == 4:
        print(i)
'''

# Ejercicio 9
# Cuenta las palabras que contienen la letra "e"
'''palabras = ["tren", "avión", "barco", "coche", "moto"]

for i in palabras:
    if 'e' in i:
        print(i)
'''

# Ejercicio 10
# Imprime cada palabra en orden inverso de caracteres
'''palabras = ["python", "lista", "cadena", "bucle"]

for i in palabras:
    print(i[::-1])
'''

# Ejercicio 12
# Imprime las palabras que tienen una "r" en la segunda posición
'''palabras = ["brazo", "arena", "verde", "crema", "grano"]

for i in palabras:
    if 'r' in i[1]:
        print(i)
'''


# Ejercicio 13
# Muestra las palabras con número impar de letras
'''palabras = ["guitarra", "bajo", "piano", "voz", "flauta"]

for i in palabras:
    if len(i) % 2 != 0:
        print(i)
'''

# Ejercicio 14
# Cuenta cuántas palabras no contienen la letra "o"
'''palabras = ["piedra", "sol", "árbol", "tierra", "aire"]

for i in palabras:
    if 'o' not in i:
        print(i)
'''
import string

# Ejercicio 15
# Imprime las palabras que terminan en consonante
'''palabras = ["sol", "vida", "mujer", "flor", "estrella"]

for i in palabras:
    if not i.endswith(('a', 'e', 'i', 'o', 'u')):
        print(i)
'''

# Ejercicio 16
# Muestra todas las palabras en minúsculas (aunque ya lo estén)
'''palabras = ["UNO", "Dos", "TrEs", "CUATRO", "Cinco"]

for i in palabras:
    print(i.lower())
'''
# Ejercicio 17
# Muestra cuántas palabras tienen letras repetidas
'''palabras = ["luz", "goma", "olla", "cielo", "baba"]

for i in palabras:
    if len(i) != len(set(i)):
        print(i)'''

# Ejercicio 18
# Imprime solo las palabras que comienzan y terminan con la misma letra
'''palabras = ["revolver", "luz", "solos", "radar", "camión"]

for i in palabras: 
    if i.startswith(i[-1]) and i.endswith(i[0]):
        print(i)
'''
