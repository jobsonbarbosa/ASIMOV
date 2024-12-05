import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

TIPOS_ARQUIVOS_VALIDOS = [
    'Site', 'Youtube', 'PDF', 'CSV', 'TXT'
]

CONFIG_MODELOS = {
    'Groq':
        {'modelos': ['llama-3.1-70b-versatile','gemma2-9b-it', 'mixtral-8x7b-32768'], 'chat': ChatGroq},        
    'OpenIA': 
        {'modelos': ['gpt-4o-mini', 'gpt-4o', 'gpt-4-turbo', 'gpt-3.5-turbo-1106'], 'chat': ChatOpenAI}}
# Usando memorias do LangChain
MEMORIA = ConversationBufferMemory()


def carrega_modelo(provedor, modelo, api_key):
    chat = CONFIG_MODELOS[provedor]['chat'](model=modelo, api_key=api_key)
    st.session_state['chat'] = chat

# Adicionando memoria pre-definidas
#==== Usado apenas para teste ====== #
# MEMORIA.chat_memory.add_user_message('Oi IA')
# MEMORIA.chat_memory.add_ai_message('Oi Humano! Sou o Jobs Oracle, em que posso lhe ajudar!?')

#==== Não iremos usar mais esse lista, pois iremos usar o memoria do LangChain
# MENSAGEM_EXEMPLO = [
#     ('user', "Olá Jobs"),
#     ("assistant", "Tudo bem!?"),
#     ("user", "Tudo ótimo!")
# ]

def pagina_chat():
    st.header("Seja bem vindo ao Jobs Oracle", divider=True)
    
    chat_model = st.session_state.get('chat')
    
    # Guardar na memoria as mesangem na sessão, se não houver retornar uma dicionário vazio.
    memoria = st.session_state.get('memoria', MEMORIA)
    
    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    input_usuario = st.chat_input('Fale com o Oráculo')
    if input_usuario:
        memoria.chat_memory.add_user_message(input_usuario)
        chat = st.chat_message('human')
        chat.markdown(input_usuario)
        
        
        chat = st.chat_message('ai')
        resposta = chat.write_stream(chat_model.stream(input_usuario))
        # resposta = chat_model.invoke(input_usuario).content
        memoria.chat_memory.add_ai_message(resposta)
        
        st.session_state['memoria'] = memoria
        
        # st.rerun()


def sidebar():
    tabs = st.tabs(['Upload de arquivos', 'Seleção de Modelos'])
    
    # Seleciona o tipo de arquivo
    with tabs[0]:
        tipo_arquivo = st.selectbox('Seleciona o tipo de arquivo', TIPOS_ARQUIVOS_VALIDOS)
        
        # Condição para cada tipo de arquivo
        if tipo_arquivo == 'Site':
            arquivo = st.text_input('Digite a URL do site')
        if tipo_arquivo == 'Youtube':
            arquivo = st.text_input('Digite a URL do video')
        if tipo_arquivo == 'PDF':
            arquivo = st.file_uploader('Faça o upload do arquivo PDF', type=['.pdf'])
        if tipo_arquivo == 'CSV':
            arquivo = st.file_uploader('Faça o upload do arquivo CSV', type=['.csv'])
        if tipo_arquivo == 'TXT':
            arquivo = st.file_uploader('Faça o upload do arquivo TXT', type=['.txt'])
            
    # Selecção de Modelos
    with tabs[1]:
        provedor =  st.selectbox('Seleciona o provedor dos modelos', CONFIG_MODELOS.keys())
        
        modelo = st.selectbox('Selecione o modelo', CONFIG_MODELOS[provedor]['modelos'])

        # API KEYs
        api_key = st.text_input(f'Adicione a api key para o provedor {provedor}', value=st.session_state.get(f'api_key_{provedor}'))
        
        st.session_state[f'api_key_{provedor}'] = api_key
    
    #Botão para iniciar a IA
    if st.button('Inicializar o Jobs Oracle', use_container_width=True):
        carrega_modelo(provedor, modelo, api_key)

def main():
    pagina_chat()
    with st.sidebar:
        sidebar()

if __name__ == '__main__':
    main()