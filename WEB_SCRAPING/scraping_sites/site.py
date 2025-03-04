import requests
from bs4 import BeautifulSoup

class Site:
    def __init__(self, site):
        self.site = site
        self.news = []
        
    # Função para atualizar as noticias
    def update_news(self):
        if self.site.lower() == 'globo':
            url = 'https://www.globo.com/'
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Wind64; x64) Applewebkit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

            # Fazendo a requisição do site
            page = requests.get(url, headers=browsers)

            # Salvando a resposta em uma variável
            resposta = page.text

            # Usando o Soup para zer um parset HTML e estrutura o conteudo com tags
            soup = BeautifulSoup(resposta, 'html.parser')

            # Selecionando as tags que será realizado a rasparagem
            noticias = soup.find_all('a')

            # Selecionando as classes que será realizado a rasparagem
            tg_class1 = 'post__title'
            # Selecionando as classes que será realizado a rasparagem
            tg_class2 = 'post-multicontent__link--title__text'

            # Criando um dicionário para armazenar as noticias
            news_dict_globo = {}
            for noticia in noticias:
                if noticia.h2 != None:
                    if tg_class1 in noticia.h2.get('class') or tg_class2 in noticia.h2.get('class'):
                        news_dict_globo[noticia.h2.text] = noticia.get('href')
            self.news = news_dict_globo
            print(news_dict_globo)

if __name__ == '__main__':
    self = Site('globo')
    self.update_news()
    print(self.news)
