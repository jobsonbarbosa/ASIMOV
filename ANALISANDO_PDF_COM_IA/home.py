from pathlib import Path
import streamlit as st
import time

PASTA_ARQUIVOS = Path(__file__).parent/'arquivos'

def cria_chain_conversa():
    st.session_state['chain'] = True
    time.sleep(2)

def sidebar():
    # UPLOAD DE ARQUIVOS
    uploader_pdfs = st.file_uploader(
        'Adcione seus arquivos pdf', 
        type=['.pdf'], 
        accept_multiple_files=True
        )
    if not uploader_pdfs is None:
        for arquivo in PASTA_ARQUIVOS.glob('*.pdf'):
            arquivo.unlink()
        for pdf in uploader_pdfs:
            with open(PASTA_ARQUIVOS / pdf.name, 'wb') as f:
                f.write(pdf.read())

    # BOTÃO DE CARREGAR

    label_botao = 'Inicializar ChatBot'
    if 'chain' in st.session_state:
        label_botao = 'Atualizar ChaBot'
    if st.button(label_botao, use_container_width=True):
        if len(list(PASTA_ARQUIVOS.glob('*.pdf'))) == 0:
            st.error('Adicione arquivos .pdf apra iniciarliar o chatbot')
        else:
            st.success('Inicializando o chabot...')
            cria_chain_conversa()
            st.rerun()

def main():
    with st.sidebar:
        sidebar()

if __name__ == '__main__':
    main()