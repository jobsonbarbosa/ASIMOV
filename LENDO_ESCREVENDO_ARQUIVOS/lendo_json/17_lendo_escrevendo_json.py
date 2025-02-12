import json
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

data_json = '''
{
    "assinantes": [
        {
            "nome": "Adriano Soares",
            "telefone": "71 997440022",
            "email": "jariandosoares@gmail.com",
            "em_dia": "true"
        },
        {
            "nome": "Rebeca Cardoso",
            "telefone": "71 9987676546",
            "email": "rebecacardoso@gmail.com",
            "em_dia": "false"
        }
        
    ],
    "data_estracao": "12/02/2025"
}
'''

# Converter json para dicionário
dado_convertido = json.loads(data_json)

''' --- Resolvido 
print(type(data_json))
print(type(dado_convertido))
print(dado_convertido)
'''
# Convertendo novamente para json
''' --- Resolvido ---
dado_desocnvertido = json.dumps(dado_convertido, ensure_ascii=False, indent=2)
print(type(dado_convertido))
print(type(dado_desocnvertido))
print(dado_desocnvertido)
'''

# Lendo arquivos Json
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'json' / 'assinantes.json' ) as f:
    dado_carregado = json.load(f)
# print(type(dado_carregado))
# print(dado_carregado)

print(dado_convertido['assinantes'])

# Escrevendo um arquivos Json
with open(pasta_atual / 'json' / 'assinantes_copia.json', 'w') as f:
    json.dump(dado_carregado, f, indent=2, ensure_ascii=False)