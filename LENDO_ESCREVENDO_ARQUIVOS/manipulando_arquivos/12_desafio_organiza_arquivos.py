# Organizar arquivos por formato
from pathlib import Path
import shutil
import os
import datetime

pasta_atual = Path(__file__).parent

# mapeando o caminho
pasta_arquivo_desafio = pasta_atual /'arquivos_desafio'
pasta_organizada = pasta_atual / 'organizada'
pasta_backups = pasta_atual / 'backups'

# criando pasta oraganizada
if pasta_organizada.exists():
    shutil.rmtree(pasta_organizada)
pasta_organizada.mkdir()

# criando pasta de backups
if not pasta_backups.exists():
    pasta_backups.mkdir()

# Cria pasta por extensão
for arquivo in pasta_arquivo_desafio.glob('**/*'):
    if arquivo.is_file():
        pasta_organizada_c_ext = pasta_organizada / arquivo.suffix.replace('.', '')
        if not pasta_organizada_c_ext.exists():
            pasta_organizada_c_ext.mkdir()
        shutil.copy(arquivo, pasta_organizada_c_ext)

# |Criando o backup
nome_backup = datetime.datetime.now().strftime('%Y_%m_%d')
shutil.make_archive(pasta_backups / nome_backup, 'zip', pasta_organizada)
