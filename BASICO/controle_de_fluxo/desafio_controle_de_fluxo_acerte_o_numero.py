# Desafio acerte o numero
# - Escolha um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
# se o número é mais alto ou mais baixo
# - Repete isso até 3 vezes!
# ===============================================
#import random
#numero_secreto = int(random.randint(0, 100))
#tentativas = 1
#print(numero_secreto)
#
#while(tentativas < 4):
#    chute = int(input('Descrubra o numero\nDigite um numero: '))
#    if chute == numero_secreto:
#        print('Voce acertou')
#    elif chute > numero_secreto:
#        print('Numero maior que o correto')
#    else:
#        print('Numero menor que o correto')
#    tentativas += 1
# ====================================================
# Resolução

numero_secreto = 10
descobriu = False
tentativas = 1
while(tentativas < 4):
    if not descobriu:
        chute = int(input(f'Descubra o número!\nVocê tem {tentativas}/3\nSeu chute: '))
        if chute < numero_secreto:
            print('Chute muito abaixo!\n')
        elif chute > numero_secreto:
            print('Chute muito alto!\n')
        else:
            print('Descobriu!')
            descobriu = True
        tentativas += 1

if descobriu:
    print('Parabéns, você ganhou.\n')
else:
    print(f'Que pena, você perdeu! O número secreto era {numero_secreto}')

