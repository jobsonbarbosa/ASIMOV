# Métodos

produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00
}

print(produtos)


print( 'Principais métodos')
print('=======================================')

print('\nClear')

print(produtos.clear())

print('\nGET')

produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00
}
print(produtos.get('banana'))
print(produtos.get('carne'))

print('\nSET')

produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00
}
print(produtos.setdefault('arroz', 100))

print('\nKEYS, VALUES, ITEMS')

produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00
}
for valor in produtos.keys():
    print(valor)

for produto in produtos.values():
    print(produto)
    
for par in produtos.items():
    print(par)
    

print('\nUPDATE')

produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00
}

novos_produtos = {
    'massa': 5.90,
    'banana': 4.70
}

print(produtos)
produtos.update(novos_produtos)

print(produtos)