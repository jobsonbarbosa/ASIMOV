from pathlib import Path

# Lendo um arquivo forma não recemendanda
pasta_atual = Path(__file__).parent
print(pasta_atual)

''' --- Forma não recomendada ---

lista_compras = open(pasta_atual / 'lista_compras.txt', 'r', encoding='utf-8')

print(lista_compras.read())

# importante sempre que abrir um arquivos, fecha-lo para não ficar com uma sessão aperta
lista_compras.close()

'''

'''--- Resolvido ---
# Lendo arquivo forma recomendada
# usando o with, quando a execução sair do escopo, automaticamente a sessão é encerrada, por isso é recomendo o uso deo with na aberta de arquivos.
with open(pasta_atual / 'lista_compras.txt', 'r', encoding='utf-8') as lista_compras:
    print(lista_compras.read())
'''

''' --- Resolvido ---
# Lendo linha a linha
with open(pasta_atual / 'lista_compras.txt', 'r', encoding='utf-8') as lista_compras:
    linha =  lista_compras.readline()
    while linha != '':
        print(linha, end='')
        linha =  lista_compras.readline()
    print(linha)
'''   

'''--- Resolvido ---
# Lendo todas as linha
with open(pasta_atual / 'lista_compras.txt', 'r', encoding='utf-8') as lista_compras:
    print(lista_compras.readlines())
'''

''' --- Resolvido ---
# Escrevendo arquivo
items_comprados = ['Feijão', 'Arroz', 'Macarrão']

with open(pasta_atual / 'lista_compras.txt', 'r', encoding='utf-8') as lista_compras:
    items_lista = lista_compras.readlines()

with open(pasta_atual / 'lista_compras_atualizada.txt', 'w', encoding='utf-8') as lista_atualizada:
    for item in items_lista:
        #print(item)
        if not item.replace('\n', '') in items_comprados:
            lista_atualizada.write(item)
'''

''' --- Resolvido ---
# Escrevendo linha a linha
items_ja_comprados = ['Feijão', 'Arroz', 'Macarrão']

with open(pasta_atual / 'lista_compras.txt', 'r', encoding='utf-8') as lista_compras:
    items_lista = lista_compras.readlines()
items_lista_atualizada = []
for item in items_lista:
    if not item.replace('\n', '') in items_ja_comprados:
        if
        items_lista_atualizada.append(item)
# print(items_lista)
# print(items_lista_atualizada)

with open('lista_de_compras_atualizada.txt', 'w', encoding='utf-8') as lista_atualizada:
    lista_atualizada.writelines(items_lista_atualizada)
'''


# Acrescentando valores
pasta_atual = Path(__file__).parent

novo_items = ['Jaca']

novo_items_c_quebra = []
for item in novo_items:
    novo_items_c_quebra.append(f'\n{item}')
with open('lista_compras.txt', 'w', encoding='utf-8') as lista_adicionada:
    lista_adicionada.writelines(novo_items_c_quebra)