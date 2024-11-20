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
        mostrar_lista_de_carros(carros)
    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("====================")
        print('Escolha o código do carro: ')
        cod_carro = int(input())
        print('Por quantos dias você deseja alugar esse carro?')
        dias = int(input())
        os.system('cls')
        
        print(f'Você escolheu {carros[cod_carro][0]} por {dias} dias')
        print(f'O aluguel totalizaria R$ {dias * carros[cod_carro][1]}. Deseja alugar?')
        
        print('0 - SIM | 1 - NÃO')
        conf = int(input())
        if conf == 0:
            print(f'Parabéns você alugou o {carros[cod_carro][0]} por {dias} dias. ')
            alugados.append(carros.pop(cod_carro))
            
    elif op == 2:
        if len(alugados) == 0:
            print('Não há carros para devolver.')
        else:
            print('Segue a lista de carros alugados. Qual você deseja devovler?')
            mostrar_lista_de_carros(alugados)
            print("")
            print('Escolha o código do carro que deseja devolver: ')
            cod = int(input())
            if conf == 0:
                print(f'Obrigado por devolver o carro {alugados[cod][0]}')
                carros.append(alugados.pop(cod))
    
    print('')
    print("====================")
    print('Digite 0 para CONTINUAR | 1 para SAIR')
    if int(input()) == 1:
        break