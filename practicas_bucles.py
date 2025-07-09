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
nombres = ["Ana", "Luis", "Carlos", "Eva"]

for i in nombres:
    print(f'Hola, {i}')



































