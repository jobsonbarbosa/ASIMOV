from langchain_community.document_loaders import (WebBaseLoader,
                                                  YoutubeLoader,
                                                  CSVLoader,
                                                  PyPDFLoader,
                                                  TextLoader)

# ==== Arquivos da internet ==========
url = 'https://asimov.academy/'

def carrega_site():
    loader = WebBaseLoader(url)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

url_yt = 'hVOYFDXYG1U'

loader= YoutubeLoader(url_yt, add_video_info=False, language=['pt'])
lista_documentos_yt = loader.load()
documento_yt = '\n\n'.join([doc.page_content for doc in lista_documentos_yt])


print(documento_yt)