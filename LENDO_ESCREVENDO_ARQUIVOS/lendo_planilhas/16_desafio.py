from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent

'''tabela_cliente_dict = pd.read_excel(pasta_atual / 'arquivos' / 'clientes.xlsx', sheet_name=None)

for nome_aba, tabela in tabela_cliente_dict.items():
    tabela.to_excel(pasta_atual / 'arquivos'/ 'planilhas_separadas' / f'{nome_aba}.xlsx', index=False)
print(tabela_cliente_dict)'''

# Planila consolidada

with pd.ExcelWriter(pasta_atual / 'arquivos' / 'planilha_consolidade' / 'clientes.xlsx') as consolidade:
    for arquivo in Path(pasta_atual / 'arquivos' / 'planilhas_separadas').glob('*.xlsx'):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidade, sheet_name=arquivo.stem, index=False)