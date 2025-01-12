import requests
from bs4 import BeautifulSoup

# Informando a URL que será realizado o scraping
url = 'https://www.globo.com'

#Salvando o restorno da requisição do site em uma variável
page = requests.get(url)

# Se a resposta for <Response [200]> a requisição foi respondida
print(page)

# Salvador apenas os texto da página
resposta = page.text

# Usando o Soup para zer um parset HTML e estrutura o conteudo com tags
soup =  BeautifulSoup(resposta, 'html.parser')

# Selecionando as tags que será realizado a rasparagem
noticias = soup.find_all('h2', {'class':'post__title'})

# Fazendo a interação em cada noticias da estrutura que foi retornado da lista e printando apenas os titulos
for i in range(len(noticias)):
    print(noticias[i].text)