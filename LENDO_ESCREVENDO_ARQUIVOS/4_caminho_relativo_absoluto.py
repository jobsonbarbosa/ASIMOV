# Caminho relativo

from pathlib import Path

print(Path("primeira_pasta").exists()) #True

# Saber onde o python esta sendo rodado
print(Path.cwd())