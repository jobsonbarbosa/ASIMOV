import streamlit as st

def pagina_chat():
    st.header("Seja bem vindo ao Jobs Oracle", divider=True)

    menssagens = st.session_state( 'mensagens')

def main():
    pagina_chat()

if __name__ == '__main__':
    main()