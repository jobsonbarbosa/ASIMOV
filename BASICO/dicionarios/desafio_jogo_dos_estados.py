# - Crie um "Jogo dos estados". Neste jogo, o jogador precisa responder
# p nome da capital de cada Estado do Brasil, O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e chegar se o usuário
# respondeu de forma correta, Após cada pergunta, o usuário pode escolher
# parar o jogo, ou quanto todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

import random

estados_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapa': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasilia',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas',
}
### Solução Jobs
# # tamanho = len(estados_capitais)
# # print(tamanho)
# tentativas = 0
# continuar = False
# errou = 0
# acertou = 0

# while tentativas < 4:
    
#     estado, cidade = random.choice(list(estados_capitais.items()))
#     print(estado, cidade)
#     resposta = input(f'Qual a capital do estado {estado}?: ')
#     if resposta.lower() == cidade.lower():
#         print('Acertou miseravi, quem te ensisou!?')
#         acertou += 1
#     else:
#         print('Errrrooooou!')
#         errou += 1
        
#     tentativas += 1
#     continuar = input('Deseja continuar?\nS | N ?: ')
#     if continuar.lower() == 's':
#         continue
#     else:
#         break
 
# porcetagem = (acertou/tentativas) * 100
# print(f'Você acertou {porcetagem}%')

# Solução Asimovi

quer_continuar = True
rodadas = 0
acertos = 0

for estado, capital in estados_capitais.items():
    if not quer_continuar:
        break

    rodadas += 1
    
    print(f'\n -> Qual a capital do estado {estado}?')
    
    resposta = input('Sua resposta: ')
    if resposta.lower() == capital.lower():
        print('Resposta correta')
        acertos += 1
    else:
        print(f'Resposta errada! O correto seria {capital}')
    
    while True:
        opcao = input('Deseja continuar? (S/N)').lower()
        if opcao not in ['s', 'n']:
            print('Responda apenas com "s" para sim ou "n" para não.')
            continue
        elif opcao == 'n':
            quer_continuar = False
        break

porc = acertos / rodadas * 100

print(f'Você acertou {acertos} de {rodadas}')
print(f'Porcentagem de acertos: {porc:.2f}%')
            