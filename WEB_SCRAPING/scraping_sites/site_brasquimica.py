import requests
from bs4 import BeautifulSoup

class SiteBrasquimica:
    def __init__(self, site):
        self.site = site
        self.produtos = []

    def update_produtos(self):
       if self.site.lower() == 'brasquimica':
           url = 'https://www.brasquimica.com.br/produtos'
           browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Wind64; x64) Applewebkit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

           # Fazendo a requisição do site
           page = requests.get(url, headers=browsers)

           # Salvando a resposta em uma variável
           resposta = page.text

           # Usando o Soup para zer um parset HTML e estrutura o conteudo com tags
           soup = BeautifulSoup(resposta, 'html.parser')

           tag_class1 = 'beefup__body'
           # Selecionando as tags que será realizado a rasparagem
           produtos = soup.find_all('div')
           self.produtos = produtos
           for produto in produtos:
               if tag_class1 in produto.get('class'):
                   print(produto.text)


if __name__ == '__main__':
    self = SiteBrasquimica('brasquimica')
    self.update_produtos()
    print(self.produtos)
