tup = [0, 0, 1, 2, 4, 54, 67]

# print(tup.index(2))

# print(tup.count(0))

# for n in range(5):
#     tup.append(n * 2)

# print(tup)

import random

valores = []

for _ in range(10):
    x = random.randint(0, 100)
    if x > 2:
        valores.append(x)
print(valores)

numeros = [1,2,3]
numeros.append([4, 5, 6])

print(numeros)

numeros = [1, 2, 3]

numeros.extend([4, 5, 6])
print(numeros)

vogais = ['a', 'i', 'o', 'u']
vogais.insert(1, 'e') # determinar o local onde será inserido a string
print(vogais)


valores = [10, 20, 43, 65, 77, 90]

valores_removidos = valores.pop()
print(valores)
print(valores_removidos)