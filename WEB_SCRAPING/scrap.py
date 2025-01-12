from bs4 import BeautifulSoup


with open('jobssolutions_exemplo.html', 'r') as file:
    conteudo = file.read()

ex = BeautifulSoup(conteudo, 'lxml')


p = ex.find_all('p')

print(p)