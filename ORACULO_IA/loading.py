import os
from time import sleep
import streamlit as st
from langchain_community.document_loaders import (WebBaseLoader,
                                                  YoutubeLoader,
                                                  CSVLoader,
                                                  PyPDFLoader,
                                                  TextLoader)

from fake_useragent import UserAgent

# ==== Arquivos da internet ==========
# url = 'https://asimov.academy/'

def carrega_site(url):
    documento = ''
    for i in range(5):
        try:
            os.environ['USER_AGENT'] = UserAgent().random
            loader = WebBaseLoader(url, raise_for_status=True)
            lista_documentos = loader.load()
            documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
            break
        except:
            print(f'Erro ao tentar carregar o site {i+1}')
            sleep(3)
    if documento == '':
        st.error('Não foi possivel carregar o site')
        st.stop()

    return documento

url_yt = 'v=mnfPby1GbQg'
def carrega_youtube(video_id):
    loader= YoutubeLoader(video_id, add_video_info=False, language=['pt'])
    lista_documentos_yt = loader.load()
    documento_yt = '\n\n'.join([doc.page_content for doc in lista_documentos_yt])
    return documento_yt

caminho = 'arquivos\knowledge_base.csv'
def carrega_csv(caminho):
    loader= CSVLoader(caminho)
    lista_documentos_csv = loader.load()
    documento_csv = '\n\n'.join([doc.page_content for doc in lista_documentos_csv])
    return documento_csv

caminho_pdf = 'arquivos\RoteiroViagemEgito.pdf'
def carrega_pdf(caminho):
    loader = PyPDFLoader(caminho_pdf)
    lista_documentos_pdf = loader.load()
    documento_pdf = '\n\n'.join([doc.page_content for doc in lista_documentos_pdf])
    return documento_pdf

caminho_txt = 'arquivos\knowledge_base.txt'
def carrega_txt(caminho):
    loader = TextLoader(caminho_txt)
    lista_documentos_txt = loader.load()
    documento_txt = '\n\n'.join([doc.page_content for doc in lista_documentos_txt])
    return documento_txt
 
documento = carrega_txt(caminho_txt)
# print(documento)