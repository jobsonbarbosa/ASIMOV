import os

carros = [
    ('Chevrolet Tracker', 120),
    ('Checrolet Onix', 90),
    ('Chevrolet Spin', 150),
    ('Hyundai HB20', 85),
    ('Hyundai Tucson', 120),
    ('Fiat Uno', 60),
    ('Fiat Mobi', 70),
    ('Fiat Pulse', 130),
    ('Ford KA', 120),
    ('Ford Focus', 150)
]

alugados = []

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print(f'[{i}] {car[0]} - R$ {car[1]} /dia.')

mostrar_lista_de_carros(carros)

while True:
    
    os.system('clear')
    
    print("====================")
    print('Bem vindo a Locadora Jobs Cars')
    print("====================")
    print('O que você deseja fazer?')
    print('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro')
    op = int(input())
    if op == 0:
        pass
    elif op == 1:
        pass
    elif op == 2:
        pass
    
    print('')
    print("====================")
    print('Digite 0 para CONTINUAR | 1 para SAIR')
    if int(input()) == 1:
        break