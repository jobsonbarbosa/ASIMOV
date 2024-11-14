# Strings são considerados sequecias

nome = "Jobson"

print(nome[0])

print(tuple(nome))

# o Python por padrão vai tentar transformar uma sequencia em bool

#seq = [1, 2, 3] # teste 1

seq = [] # teste 2

if seq:
    print('Sequência não esta vazia')
else:
    print('Sequência está vazia')