from pathlib import Path

# Desenvolva um script para encontrar um arquivo dentro da pasta home do usuário

caminho = Path.home()
# print(caminho)

# for arquivo in caminho.glob('**/*'):
#     if arquivo.is_file():
#         if arquivo.stem == 'arquivo1':
#             print(arquivo)

def encontra_arquivo(caminho, nome_arquivo):

    for arquivo in caminho.glob('**/*'):

        if arquivo.is_file():

            if arquivo.stem == nome_arquivo:

                print(arquivo)
                print('cheguei')

encontra_arquivo(Path.cwd(), 'arquivo1.txt')