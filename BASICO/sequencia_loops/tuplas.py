alunos = ['Jobson', 'Joelma', 'Carolina']

print(alunos[1])

alunos[1] = 'Maurina'

print(alunos)

# Tuplas não podem ser alteradas dinamicamente
valores = (1, 2, 3)

print(valores)

print(valores[1])

valores[1] = 5 # TypeError: 'tuple' object does not support item assignment

print(valores)