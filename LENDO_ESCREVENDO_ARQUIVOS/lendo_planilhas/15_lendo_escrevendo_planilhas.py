import pandas as pd
from pathlib import Path
# Estamos usando a bib openpyxl

pasta_atual = Path(__file__).parent

''' --- Resolvido ---
# Lendo tabelas com DataFrame
tabela_cliente = pd.read_excel(pasta_atual / 'arquivos' / 'clientes.xlsx')

print(tabela_cliente.head(10))
'''

'''--- Resolvido --- 
# Lendo aba especifica
# Para usamos uma tabela especifica usamos o sheet_name = 'nome da aba'
tabela_cliente = pd.read_excel(pasta_atual / 'arquivos'/ 'clientes.xlsx', sheet_name='SC')
print(tabela_cliente.head(10))
'''

'''--- Resolvido ---
# Modificando o Header
tabela_cliente = pd.read_excel(pasta_atual / 'arquivos'/ 'clientes.xlsx', sheet_name='SC', header=1)
print(tabela_cliente.head(10))

'''

''' --- Resolvido ---
# Adicionando coluna de index
tabela_clientes = pd.read_excel(pasta_atual / 'arquivos'/ 'clientes.xlsx', sheet_name='SC', index_col=0)
print(tabela_clientes.head(10))
'''
''' --- Resolvido --- 
# Lendo colunas especificas
tabela_clientes = pd.read_excel(pasta_atual / 'arquivos' / 'clientes.xlsx', usecols=[0, 1])
print(tabela_clientes.head(10))
'''

'''--- Resolvido ---
# Decimal com .
tabela_clientes = pd.read_excel(pasta_atual / 'arquivos' / 'clientes.xlsx', decimal='.')
print(tabela_clientes.head(10))
'''
''' --- Resolvido ---
# Quebra de mulhares com ponto.
tabela_clientes = pd.read_excel(pasta_atual / 'arquivos' / 'clientes.xlsx', thousands='.')
print(tabela_clientes.head(10))

'''
''' --- Resilvido --- 
# Escrevendo planilha
tabela_cliente = pd.read_excel(pasta_atual / 'arquivos' / 'clientes.xlsx')
tabela_cliente.to_excel(pasta_atual / 'arquivos' / 'copia_clientes.xlsx')
'''

# Escrevendo diversas abas
tabela_clientes_rs = pd.read_excel(pasta_atual / 'arquivos' / 'clientes.xlsx', sheet_name='RS')
tabela_clientes_sc = pd.read_excel(pasta_atual / 'arquivos' / 'clientes.xlsx', sheet_name='SC')

with pd.ExcelWriter(pasta_atual / 'arquivos' / 'copia_clientes.xlsx') as nova_planilha:
    tabela_clientes_rs.to_excel(nova_planilha, sheet_name='RS', index=False)
    tabela_clientes_rs.to_excel(nova_planilha, sheet_name='SC', index=False)
