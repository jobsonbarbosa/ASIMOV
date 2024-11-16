# Dado dua lista, printe tod so s valores que aparecem 
# dublicados nas duas listas.
print('Desafio 01\n==============================\n')
lista1 = [1, 3, 5, 6, 7, 9]
lista2 = [0,2,4,5,6,8,9]

for n in lista1:
    for m in lista2:
        if n == m:
            print(f'Os valores duplicados é {n}')
    

# Dado duas lista, printe, uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.
print('\n\n')
print('Desafio 02\n==============================\n\n')

# lista1 = [1, 3, 5, 6, 7, 9]
# lista2 = [0,2,4,8]
# for n in lista1:
#     for m in lista2:
#         if n == m:
#             print(f'Exite elementeo comum')
#             break
#     break
# print('Não existe elementos comum')

lista1 = [1, 3, 5, 6, 7, 9]
lista2 = [0,2,4,8]

elemento_em_comum = False

for n in lista1:
    if elemento_em_comum:
        break
    for m in lista2:
        if n == m:
            elemento_em_comum = True
            break
        

if elemento_em_comum:
    print(f'As lista {lista1} e {lista2} possuem elementos em comum')
else:
    print(f'As listas {lista1} e {lista2} NÃO possuem elementos em comum')