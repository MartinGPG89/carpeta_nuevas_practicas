import math

# 1️⃣ Muestra cada número multiplicado por 2
'''numeros = [3, 7, 12, 5, 9]


for i in numeros:
    print(i*2, end=',')'''


# 2️⃣ Imprime solo los números mayores que 6
'''numeros = [3, 7, 12, 5, 9]

for i in numeros:
    if i > 6:
        print(i)
'''

# 3️⃣ Suma todos los números de la lista y muestra el resultado final
'''numeros = [3, 7, 12, 5, 9]
suma = 0

for i in numeros:
    suma += i

print(suma)
'''


# 4️⃣ Imprime la raíz cuadrada de cada número
'''numeros = [1, 4, 9, 16, 25]

for i in numeros:
    print(math.sqrt(i))

'''


# 5️⃣ Añade a la lista 'pares' solo los números pares de la lista dada
'''numeros = [2, 5, 8, 11, 14, 17]
pares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)

print(pares)'''

# 6️⃣ Imprime cada palabra en mayúsculas
'''palabras = ["python", "java", "c", "javascript"]

for i in palabras:
    print(i.upper(),end='  --  ')
'''

# 7️⃣ Imprime solo las palabras que tengan más de 3 letras
'''palabras = ["python", "java", "c", "javascript"]

for i in palabras:
    if len(i) >3:
        print(i)

'''

# 8️⃣ Imprime el número de caracteres de cada fruta
'''frutas = ["manzana", "pera", "kiwi", "plátano"]

for i in frutas:
    print(len(i))

'''

# 9️⃣ Añade a la lista 'con_a' solo las palabras que contengan la letra "a"
'''frutas = ["manzana", "pera", "kiwi", "plátano"]
con_a = []

for i in frutas:
    if 'a' in i:
        con_a.append(i)

print(con_a)

'''

# 🔟 Imprime cada nombre con la frase: "Hola, <nombre>!"
'''nombres = ["Ana", "Luis", "Carlos", "Eva"]

for i in nombres:
    print(f'Hola, {i}')
'''


#WHILE

# 1️⃣ Recorre la lista con while e imprime cada número
'''numeros = [4, 8, 15, 16, 23, 42]
pos = 0

while pos < len(numeros):
    print(numeros[pos])

    pos += 1
'''

# 2️⃣ Imprime solo los números mayores que 10 usando while
'''numeros = [3, 11, 7, 14, 2, 18]
pos = 0

while pos < len(numeros):
    if numeros[pos] > 10:
        print(numeros[pos])

    pos += 1
'''

# 3️⃣ Suma todos los números de la lista usando while y muestra el resultado
'''numeros = [5, 10, 15, 20]
pos = 0
suma = 0

while pos < len(numeros):
    suma += numeros[pos]

    pos += 1

print(suma)
'''

# 4️⃣ Crea una lista vacía 'pares' y añade solo los números pares de la lista original usando while
'''numeros = [9, 4, 7, 2, 6, 13]
pares = []
pos = 0

while pos < len(numeros):
    if numeros[pos] % 2 == 0:
        pares.append(numeros[pos])

    pos += 1

print(pares)
'''

# 5️⃣ Imprime cada número de la lista multiplicado por 3 usando while
'''numeros = [1, 2, 3, 4, 5]
pos = 0

while pos < len(numeros):
    print(numeros[pos] * 3)

    pos += 1
'''








