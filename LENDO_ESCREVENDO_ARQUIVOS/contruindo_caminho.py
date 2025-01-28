# iremos usarmo a lib padrão do python
from pathlib import Path

caminho = Path('primeira_pasta/segunda_pasta')

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)
    
    
#Descrindo a pagina home, é o diretório princial o usuaário
print(Path.home())