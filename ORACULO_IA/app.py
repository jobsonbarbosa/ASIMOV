import streamlit as st

TIPOS_ARQUIVOS_VALIDOS = [
    'Site', 'Youtube', 'PDF', 'CSV', 'TXT'
]

CONFIG_MODELOS = {'Groq': {'modelos': ['llama-3.1-70b-versatile','gemma2-9b-it', 'mixtral-8x7b-32768']},
                  
                  'OpenIA': {'modelos': ['gpt-4o-mini', 'gpt-4o', 'gpt-4-turbo', 'gpt-3.5-turbo-1106']}}

MENSAGEM_EXEMPLO = [
    ('user', "Olá Jobs"),
    ("assistant", "Tudo bem!?"),
    ("user", "Tudo ótimo!")
]

def pagina_chat():
    st.header("Seja bem vindo ao Jobs Oracle", divider=True)
    
    # Guarda as messangem na sessão, se não houver retornar uma dicionário vazio.
    mensagens = st.session_state.get('mensagens', MENSAGEM_EXEMPLO)
    
    for mensagem in mensagens:
        chat = st.chat_message(mensagem[0])
        chat.markdown(mensagem[1])

    input_usuario = st.chat_input('Fale com o Oráculo')
    if input_usuario:
        mensagens.append(("user", input_usuario))
        st.session_state['mensagens'] = mensagens
        
        st.rerun()


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

def main():
    pagina_chat()
    with st.sidebar:
        sidebar()

if __name__ == '__main__':
    main()