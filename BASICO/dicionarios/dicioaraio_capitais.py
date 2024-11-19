capitais = {
    'Brasil': 'Brasilia',
    'França': 'Paris',
    'Japão': 'Tóquio',
}

print(capitais)

print(capitais['Brasil'])
print(capitais['Japão'])

#dicionarios são mutáveis podendo ser alterados os valores
# Os dicioário não podem ter valores respetidos.

capitais['Inglaterra'] = 'Londres'

print(capitais)

del capitais['Inglaterra']

print(capitais)

for pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')
