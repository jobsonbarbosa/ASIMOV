from time import sleep
import streamlit as st
from crud import le_todos_usuarios


def login():
    usuarios = le_todos_usuarios()
    #st.write(usuarios) # Isso é uma lista e vamos transforma-la em um dicionário.
    usuarios = {usuario.nome: usuario for usuario in usuarios}
    #st.write(usuarios)
    with st.container(border=True):
        st.markdown('Bem vindo ao AppFerias')
        
        nome_usuario = st.selectbox(
            'Selecione o seu usuário',
            usuarios.keys()
            )
        senha = st.text_input('Digite a sua senha', type='password')
        
        if st.button('Acessar'):
            usuario = usuarios[nome_usuario]
            if usuario.verifica_senha(senha):
                st.success('Login com sucesso')
                st.session_state['logado'] = True
                st.session_state['usuario'] = usuario
                sleep(1)
                st.rerun()
            else:
                st.error('Senha incorreta')

def tab_gestao_usuarios(): 
    tab_vis, tab_cria, tab_mod, tab_del = st.tabs(
        ['Visualiza', 'Criar', 'Modificar', 'Deletar']
    ) 


def pagina_calendario():
    st.title('Bem vindo ao AppFerias')
    
    st.divider()

    usuario = st.session_state['usuario']
    if usuario.acesso_gestor:
        cols = st.columns(2)
        with cols[0]:
            if st.button(
                'Acessar Gestão de Usuários', use_container_width=True):
                st.session_state['pag_gestao_usuarios'] = True
                st.rerun()
        with cols[1]:
            if st.button(
                'Acessar Calendário', 
                use_container_width=True):
                st.session_state['pag_gestao_usuarios'] = False
                st.rerun()
                    
    if st.session_state['pag_gestao_usuarios']:
        st.markdown('Pagina gestão de usuários')
        # with st.sidebar:
        #     tab_gestao_usuarios()
        
    else:
        st.markdown('Calendário')
                  
    
def main():
    
    if not 'logado' in st.session_state:
        st.session_state['logado'] = False
    if not 'pag_gestao_usuario' in st.session_state:
        st.session_state['pag_gestao_usuarios'] = False
        
    if not st.session_state['logado']:
        login()
    else:
        pagina_calendario()
    
if __name__ == '__main__':
    main()