from pathlib import Path
import shutil


''' --- Resolvido ---
# Criando pastas
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'primeira_pasta' / 'destino4'
caminho_pasta_destino.mkdir(exist_ok = True)

# A flag exist_ok=True valida de já temos uma pasta criada no diretório
'''

''' --- Resolvido --- 
# Criando pasta com todos as pastas anteiores necessárias
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'primeira_pasta' / 'destino5' / 'destino51'
caminho_pasta_destino.mkdir(parents=True)
# o paremetro parents=True permite criar descinos com subpasta que  ainda não existem.
'''


''' --- Resolvido 
# Copiando pastas
pasta_atual = Path(__file__).parent
shutil.copytree(pasta_atual / 'primeira_pasta' / 'destino5', pasta_atual /'primeira_pasta' / 'destino1' /'destino5')
#caminho_pasta_destino = pasta_atual / 'primeira_pasta' / 'destino5'

'''

''' --- Resolvido ---
# Deletando pastas vazias
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual /  'primeira_pasta' / 'destino5' /'destino51'
pasta_remover.rmdir()
'''

# para deletar pasta com conteudo é necessário usaremos o shutil
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'primeira_pasta' / 'destino1'
shutil.rmtree(pasta_remover)