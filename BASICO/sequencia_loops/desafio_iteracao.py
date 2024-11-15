# - Dado uma sequeência de números, cacule a soma e média dos numéros.
#Atenção não vale usar a função sum()

# seq1 = list(range(1,11))
# tam = len(seq1)
# # print(tam)
# soma = 0
# for n in seq1:
#     print(n)
#     print(f'{soma} + {n}')
#     soma += n

# print(soma/tam)
#===========================================================
# - Dado uma sequência de números, calcule o maior valor de sequência.
# Atenção não vale usar a função max()

# import random
# tamanho = 10
# min = 1
# max = 100

# seq2 = [
#     random.randint(min,max) 
#     for _ in range(tamanho)
# ]
# print(seq2)
# num_max = 0
# for n in seq2:
    
#     if n > num_max:
#         num_max = n

# print(f'O maior numero foi {num_max}')

# ============================================================
# - Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

palavras = ('Telefone', 'Microfone', 'Cadeira', 'Arvore')

print(palavras)

for _ in palavras:
    ...