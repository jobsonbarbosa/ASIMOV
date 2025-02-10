from pathlib import Path
import os

# Listando arquivos
#print(os.listdir(Path.cwd()))

# Listando os arquivos sem usar o OS, usnaod extensão
# print(list(Path.cwd().glob('*')))
# print("======================")
# print(list(Path.cwd().glob('*.py')))

# Lista tudo dentro de uma pasta
# print(list(Path.cwd().glob('**/*.txt')))

# Validando caminhos
# print(Path.home().exists())

# nao_exist = Path.home() / 'nao_exite'
# print(nao_exist.exists())

# Verificando se é arquivo ou pasta
print(Path(__file__).parent)
print(Path(__file__).is_file())

print(Path(__file__).parent)
print(Path(__file__).is_dir())