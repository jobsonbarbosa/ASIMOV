from pathlib import Path
import streamlit as st
import time
from langchain.memory import ConversationBufferMemory

from utils import cria_chain_conversa, PASTA_ARQUIVOS

# def cria_chain_conversa():
#     st.session_state['chain'] = True
#     memory = ConversationBufferMemory(return_messages=True)
#     memory.chat_memory.add_user_message('Oi')
#     memory.chat_memory.add_ai_message('Oi, eu sou uma LLM')
#     st.session_state['memory'] = memory
#     time.sleep(2)

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

def chat_window():
    st.header('Bem vindo ao chat com PDF da Job Solution IT')
    
    if not 'chain' in st.session_state:
        st.error('Faça o upload de PDFs para começar')
        st.stop()
        
    chain = st.session_state['chain']
    memory = chain.memory
    
    # memory = st.session_state['memory']
    
    mensagens = memory.load_memory_variables({})['chat_history']
    
    container = st.container()
    
    for mensagem in mensagens:
        chat = container.chat_message(mensagem.type)
        chat.markdown(mensagem.content)
     
    nova_mensagem = st.chat_input('Converse com seus documentos...')
    if nova_mensagem:
        chat = container.chat_message('human')
        chat.markdown(nova_mensagem)
        chat = container.chat_message('ia')
        chat.markdown('Gerando responsta')
        
        # Geração de resposta
        chain.invoke({'question': nova_mensagem})
        # time.sleep(2)
        # memory.chat_memory.add_user_message(nova_mensagem)
        # memory.chat_memory.add_ai_message('Oi, é a LLM aqui de novo!')
        st.rerun()
     


def main():
    with st.sidebar:
        sidebar()
    chat_window()

if __name__ == '__main__':
    main()