import requests
from bs4 import BeautifulSoup
import pandas as pd

# Neste projeto usaremos o pandas para estruturar melhor as informações da extração.

# IBGE | Url: https://www.ibge.gov.br/
# Iremos buscasa as cidades e estados do site do IBGE

def straping_uf(uf: str):
    uf_url = f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html'

    # Código usado para simular que a conexão é realizada por um nagedaor e não via script, o que poderia retornar um erro 404
    browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Wind64; x64) Applewebkit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
    page = requests.get(uf_url, headers=browsers)
    soup = BeautifulSoup(page.content, 'html.parser')
    indicadores = soup.select('.indicador')

    # Estruturando
    uf_dist = {
        dado.select('.ind-label')[0].text: dado.select('.ind-value')[0].text
        for dado in indicadores
    }
    return uf_dist

estado = straping_uf('ba')

# Limpando o dados extraidos
# remover os caracter especiais que esta sendo raspados junto com as informações
for indicador in estado:
    if ']' in estado[indicador]:
        estado[indicador] = estado[indicador].split(']')[0][:-8]   
    else:
        estado[indicador] =  estado[indicador]


# Estruturando com o pandas

df = pd.DataFrame(estado.values(), index=estado.keys())

print(df)

# Testando a conexão
# uf_url = f'https://www.ibge.gov.br/cidades-e-estados/ba.html'
# browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Wind64; x64) Applewebkit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
# page = requests.get(uf_url, headers=browsers)
# print(page) # Terminal: Response [200]

