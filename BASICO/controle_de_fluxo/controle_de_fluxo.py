# programa informa ser é maior de idado com base na idade que informar

idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Você é menor de idade')
    print('Você não pode dirigir um carro')
elif idade == 18:
    print('Você tem exatamento 18 anos!')
else:
    print('Você é maior de idade')
