'''animales = ["perro", "gato", "conejo", "hamster"]

for a in animales:
    print(a)

numeros = [3, 7, 2, 9, 4]

for n in numeros:
    print(n * 2)

'''

'''colores = ["rojo", "verde", "azul", "amarillo"]

for c in colores:
    print(f'El color es {c}')
'''

'''mensaje = "Hola"

for m in mensaje:
    print(m)
'''
'''edades = [15, 22, 18, 30]

for e in edades:
    if e >= 18:
        print(e)

'''

'''dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]

for d in dias:
    print(d.upper())
'''
'''precios = [10, 20, 30]
cont = []

for p in precios:
    cont.append(p * 2)

print(cont)
'''

'''letras = ["a", "b", "c", "d"]

for l in range(len(letras)):
    print(f'Indice: {l} - Valor: {letras[l]}')

'''

'''palabras = ["sol", "luna", "estrella"]

for p in palabras:
    print(f'La palabra {p} tiene {len(p)} letras')
'''

'''for i in range(1, 6):
    print(i)
'''
#----------------------------------------------------------------------------------------------------------

'''numeros = [5, 8, 12, 3, 7]

for n in numeros:
    if n > 6:
        print(n)
'''

'''palabras = ["casa", "perro", "sol", "montaña"]

for p in palabras:
    if len(p) > 3:
        print(p)
'''
'''precios = [10, 20, 30, 40]
suma = 0

for pr in precios:
    suma += pr

print(suma)'''

'''for i in range(10, 21):
    print(i)
'''

'''frutas = ["Fresa", "Kiwi", "Melón"]
contador = 0

for i in range(len(frutas)):
    print(f'{i+1} - {frutas[i]}')
'''

'''nombres = ["ana", "juan", "maría"]

for n in nombres:
    print(n, end=',')

'''

'''for i in range(2, 11):
    if i % 2 == 0:
        print(i)
'''

'''longitudes = ["corto", "muy largo", "mediano", "extremadamente largo"]

for l in longitudes:
    if len(l) > 6:
        print(l)
 '''

'''numeros = [1, 2, 3, 4, 5]
nueva_lista = []

for n in numeros:
    nueva_lista.append(n ** 2)

print(nueva_lista)

'''

'''palabras = ["python", "java", "c"]

for p in palabras:
    print(f'La palabra {p.upper()} tiene {len(p)} letra')
'''
#-------------------------------------------------------------------------------------

# Ejercicio 1
# Dadas dos listas, imprime nombre y edad de cada persona
'''nombres = ["Ana", "Luis", "Marta"]
edades = [23, 34, 19]

for nombre, edad in zip(nombres, edades):
    print(f'Sujeto: {nombre} - Edad: {edad} años')
'''
# ------------------------------------

# Ejercicio 2
# Calcula e imprime la media de una lista de números
'''numeros = [4, 7, 2, 8, 5]
suma = 0

for n in numeros:
    suma += n

media = suma /len(numeros)
print(suma)
print(media)'''


# ------------------------------------

# Ejercicio 3
# Imprime solo las frutas que empiezan por la letra "m"
'''frutas = ["manzana", "pera", "kiwi", "fresa", "melon"]

for fruta in frutas:
    if fruta.startswith('m'):
        print(fruta)
'''

# ------------------------------------

# Ejercicio 4
# Cuenta cuántas temperaturas son >= 25

'''temperaturas = [22, 27, 19, 24, 30, 18]

for temp in temperaturas:
    if temp >= 25:
        print(temp)
'''
# ------------------------------------

# Ejercicio 5
# Crea una lista con palabras que tengan exactamente 3 letras
'''palabras = ["sol", "luna", "estrella", "cielo", "mar"]

for palabra in palabras:
    if len(palabra) == 3:
        print(palabra)
'''
# ------------------------------------

# Ejercicio 6
# Imprime cada palabra en mayúsculas
'''texto = "Python es un lenguaje de programación muy popular"

print(texto.upper())
'''
# ------------------------------------

# Ejercicio 7
# Crea una lista con números multiplicados por su índice
'''numeros = [1, 2, 3, 4, 5]
nueva_lista = []
for n in range(len(numeros)):
    nueva_lista.append(numeros[n] * n)

print(nueva_lista)'''
# ------------------------------------

# Ejercicio 8
# Encuentra el valor máximo sin usar max()
'''valores = [10, 25, 5, 30, 15]
maximo = valores[0]

for v in valores:
    if v > maximo:
        maximo = v

print(maximo)
'''

# ------------------------------------

# Ejercicio 9
# Imprime cada letra y su índice en una palabra
'''palabra = "programa"

for p in range(len(palabra)):
    print(f'Letra: {palabra[p]} - Indice: {p}')
'''
# ------------------------------------

# Ejercicio 10
# Cuenta cuántas notas son >= 7
'''notas = [6, 7, 5, 8, 9]
total = 0

for n in notas:
    if n >= 7:
        total += 1
print(total)
'''
#------------------------------------------------------------------------------


# Ejercicio 1
# Dadas dos listas con nombres y ciudades, imprime:
# "Nombre vive en Ciudad"
'''nombres = ["Carla", "Pablo", "Eva"]
ciudades = ["Madrid", "Sevilla", "Valencia"]

for nombre, ciudad in zip(nombres, ciudades):
    print(f'{nombre} vive en {ciudad}')
'''
# ------------------------------------

# Ejercicio 2
# Calcula la suma de los números impares en la lista
'''numeros = [3, 8, 11, 4, 7, 10]
suma = 0

for n in numeros:
    if n % 2 != 0:
        suma += n
    
print(suma)'''


# ------------------------------------

# Ejercicio 3
# Imprime solo las palabras que terminan en vocal
'''palabras = ["sol", "cielo", "mar", "estrella", "flor"]

for palabra in palabras:
    if palabra.endswith(('a', 'e', 'i', 'o', 'u')):
        print(palabra)'''
# ------------------------------------

# Ejercicio 4
# Dada una frase, imprime cada palabra que tenga más de 5 letras
'''frase = "Estamos aprendiendo programación en Python y es muy divertido"
nueva_cadena = frase.split()

for i in nueva_cadena:
    if len(i) > 5:
        print(i)
'''

# ------------------------------------

# Ejercicio 5
# Imprime los primeros 10 números pares usando range()
'''
for i in range(0, 11):
    if i % 2 == 0:
        print(i)'''

# ------------------------------------

# Ejercicio 6
# Dada una lista de temperaturas, imprime "ALTA" si es mayor a 30,
# "MEDIA" si está entre 20 y 30 (inclusive),
# y "BAJA" si es menor a 20.
'''temperaturas = [18, 25, 32, 21, 19, 30, 35]

for temp in temperaturas:
    if temp > 30:
        print('ALTA')
    elif temp > 20 and temp < 30:
        print('MEDIA')
    else:
        print('BAJA')'''

# ------------------------------------

# Ejercicio 7
# Crea una nueva lista con los dobles de los números que sean menores a 10
'''numeros = [4, 12, 7, 15, 3, 9, 11]
nueva_lista = []

for numero in numeros:
    if numero < 10:
        nueva_lista.append(numero * 2)

print(nueva_lista)
'''

# ------------------------------------

# Ejercicio 8
# Cuenta cuántas palabras tienen la letra "e"
'''palabras = ["mesa", "silla", "ventana", "puerta", "lámpara"]
total = 0
for i in palabras:
    if 'e' in i:
        total += 1
print(total)
'''


# ------------------------------------

# Ejercicio 9
# Recorre esta lista y muestra los valores junto a su posición inversa:
# Por ejemplo: "Elemento: sol - Posición inversa: 2"
'''lista = ["sol", "luna", "estrella"]

for i in range(len(lista)):
    invert = len(lista) -1 -i
    print(f'{lista[i]} - ', invert)
'''
# ------------------------------------

# Ejercicio 10
# Recorre una cadena y cuenta cuántas veces aparece la letra "a"
'''texto = "La programación en Python es apasionante"
total = 0

for i in texto:
    if 'a' in i:
        total += 1
print(total)
'''

#-----------------------------------------------------------------------------------------------

'''precios = [100, 55, 32, 89, 150]
iva_precios = []

for i in precios:
    iva_precios.append(i * 1.21)

print(iva_precios)
'''


'''palabras = ["Hola", "casa", "Python", "Mundo", "sol", "Aprendizaje"]
nueva_lista = []

for i in palabras:
    if len(i) > 5 and i.startswith(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')):
        nueva_lista.append(i)

print(nueva_lista)
'''





''' Ejercicio sin resolver:

Dado el siguiente texto:

texto = "Hola Mundo, ESTAMOS aprendiendo PYTHON paso a Paso."

Crea un programa que cuente cuántas letras mayúsculas del abecedario contiene ese texto.
Pista leve: Puedes usar import string y string.ascii_uppercase para ayudarte.

import string

texto = "Hola Mundo, ESTAMOS aprendiendo PYTHON paso a Paso."
total = 0

for i in texto:
    if i in string.ascii_uppercase:
        total += 1
print(total)
'''

'''import string

texto = "Hola Mundo, ESTAMOS aprendiendo PYTHON paso a Paso."
total = 0

for i in texto:
    if i in string.ascii_lowercase:
        total += 1
print(total)

'''

#--------------------------------------------------------------------------------------------------------------

# Ejercicio 21
# Dada una lista de números, crea una nueva lista con los números impares multiplicados por 3
'''numeros = [1, 4, 7, 10, 13, 16]
nueva_lista = []

for i in numeros:
    if i % 2 != 0:
        nueva_lista.append(i * 3)

print(nueva_lista)
'''
# ------------------------------------

# Ejercicio 22
# Imprime las palabras que contienen la letra 'z' en una lista dada
'''palabras = ["azul", "rojo", "luz", "fuego", "pez"]

for i in palabras:
    if 'z' in i:
        print(i)
'''
# ------------------------------------

# Ejercicio 23
# Dada una lista de temperaturas, encuentra la temperatura mínima
'''temperaturas = [23, 17, 21, 19, 25, 18]
minimo = temperaturas[0]


for i in temperaturas:
    if i < minimo:
        minimo = i

print(minimo)
'''

# ------------------------------------

# Ejercicio 24
# Cuenta cuántas palabras tienen más de 4 letras en una lista
'''palabras = ["sol", "luna", "estrella", "mar", "cielo", "flor"]
total = 0

for i in palabras:
    if len(i) > 4:
        total += 1

print(total)
  '''      

# ------------------------------------

# Ejercicio 25
# Crea una nueva lista con el doble de cada número solo si el número es mayor que 5
numeros = [3, 6, 9, 2, 7]

new_list = []

for i in numeros:
    if i > 5:
        new_list.append(i * 2)

print(new_list)








































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































