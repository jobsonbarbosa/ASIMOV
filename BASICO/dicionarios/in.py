# - Server para verificar se o valor esta dentro de uma sequência

capitais = {
    'Brasil': 'Brasilia',
    'França': 'Paris',
    'Japão': 'Tóquio',
}

print('Brasil' in capitais)

pais = 'Ingraterra'

if pais in capitais:
    print(f'A capital de {pais} é {capitais[pais]}')
else:
    print(f'Não há capital registrada apra o pais {pais}')