from pathlib import Path
import shutil
import os


''' ---- Resolvido ----
# Copiando arquivos com copyfile
pasta_atual = Path(__file__).parent # Mostra a pasta atual
caminho_arquivo = pasta_atual / 'texto.txt' # incluindo o nome do arquico que iremos copiar.
caminho_arquivo_destino = pasta_atual /'primeira_pasta'/'destino1'/'textocopy.txt'

shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)

# Obs.: O copyfile, não copiar as permissões do arquivo.
'''

''' ---- Resolvido ----
# Copiando arquivos com o copy
pasta_atual = Path(__file__).parent # Mostra a pasta atual
caminho_arquivo = pasta_atual / 'texto.txt' # incluindo o nome do arquico que iremos copiar.
caminho_pasta_destino = pasta_atual /'primeira_pasta'/'destino2'

shutil.copy(caminho_arquivo, caminho_pasta_destino)

Obs.: O copy leva as permissões
'''

''' ---- Resolvido ----
# Copiando arquivos com copy2
# No copy2 alem das permissões são copiados os metadados do arquivo.
pasta_atual = Path(__file__).parent # Mostra a pasta atual
caminho_arquivo = pasta_atual / 'texto.txt' # incluindo o nome do arquico que iremos copiar.
caminho_pasta_destino = pasta_atual /'primeira_pasta'/'destino3'

shutil.copy2(caminho_arquivo, caminho_pasta_destino)
'''

'''
 #---- Resolvido ---- 
# Movendo arquivos
pasta_atual = Path(__file__).parent # Mosta a pasta atual
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'primeira_pasta' / 'destino1'

#shutil.move(caminho_arquivo, caminho_pasta_destino)
# com o move podemos fazer informando o caminho do destino quando a pasta de destino.

shutil.move(caminho_pasta_destino, pasta_atual)
'''

# Deletando arquivo

# tarega: mover o arquivos (texto.txt) para o destino3 depois de copiado apagar o original.

pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_arquivo = pasta_atual / 'primeira_pasta' / 'destino3'

# copiando o arquivo para a pasta destino
shutil.copy(caminho_arquivo, caminho_pasta_arquivo)

# deletando o arquivo da pasta atual
# validamos se o arquivo exite colocando uma condicional.
if caminho_arquivo.exists():
    os.remove(caminho_arquivo)



