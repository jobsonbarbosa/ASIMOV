from pathlib import Path

item_remover = 'Passaer com o cachorro'

pasta_atual = Path(__file__).parent
print(pasta_atual)
with open(pasta_atual / '..'/ 'arquivos_desafio' / 'view_lista.html') as html:
    linhas_html = html.readlines()
    
novas_linhas_html = []
escrever_linha = True
for i, linha in enumerate(linhas_html):
    
    
    if i < len(linhas_html) - 3 and item_remover in linhas_html[i + 2]:
        escrever_linha = False
        
    if escrever_linha:
        novas_linhas_html.append(linha)
    
    if '</li>' in linha:
        escrever_linha = True

with open(pasta_atual / '..'/ 'arquivos_desafio' / 'view_lista_atualizada.html', 'w', encoding='utf-8') as html:
    html.writelines(novas_linhas_html)

#print(linhas_html)