import streamlit as st



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

def main():
    pagina_chat()

if __name__ == '__main__':
    main()