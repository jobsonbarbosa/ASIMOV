from time import sleep
import streamlit as st
from crud import (le_todos_usuarios, cria_usuario, modifica_usuario, deleta_usuario)
import pandas as pd
from streamlit_calendar import calendar
import json


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
                st.success('Login efetuado com sucesso')
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
    # Visualiação de usuário =============
    usuarios = le_todos_usuarios()
    with tab_vis:
        data_usuarios = [{
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'acesso_gestor': usuario.acesso_gestor,
            'inicio_na_empresa': usuario.inicio_na_empresa,
        } for usuario in usuarios]    

        st.dataframe(pd.DataFrame(data_usuarios).set_index('id'))
        
    # Criação de novos usuários =========
    with tab_cria:
        nome = st.text_input('Nome do Usuário')
        senha = st.text_input('Senha do usuário')
        email = st.text_input('Email do usuário')
        acesso_gestor = st.checkbox('Tem acesso de gestor?', value=False)
        inicio_na_empresa = st.text_input('Data de inicio da empresa (formato AAAA-MM-DD)')
        
        if st.button('Criar'):
            cria_usuario(
                nome=nome,
                senha=senha,
                email=email,
                acesso_gestor = acesso_gestor,
                inicio_na_empresa = inicio_na_empresa,
            )
            st.rerun()
    # Modificar ================
    with tab_mod:
        usuarios_dict = {usuario.nome: usuario for usuario in usuarios} 
        nome_usuario = st.selectbox(
            'Selecione o usuário para modificar', 
            usuarios_dict.keys())
        
        usuario = usuarios_dict[nome_usuario]
        nome = st.text_input('Nome do Usuário para modificar', value=usuario.nome)
        senha = st.text_input('Senha do usuário para modificar', value='xxxxxxx')
        email = st.text_input('Email do usuário para modificar', value=usuario.email)
        acesso_gestor = st.checkbox('Modificar acesso de gestor?', value=usuario.acesso_gestor)
        inicio_na_empresa = st.text_input('Data de inicio da empresa (formato AAAA-MM-DD)', value=usuario.inicio_na_empresa)
        
        if st.button('Modificar'):
            if senha == 'xxxxxxx':
                modifica_usuario(
                    id=usuario.id,
                    nome=nome,
                    senha=senha,
                    email=email,
                    acesso_gestor = acesso_gestor,
                    inicio_na_empresa = inicio_na_empresa,
                ) 
            else:
                modifica_usuario(
                    id=usuario.id,
                    nome=nome,
                    senha=senha,
                    email=email,
                    acesso_gestor = acesso_gestor,
                    inicio_na_empresa = inicio_na_empresa, 
                )
            st.rerun()
    
    # Deletar ==========
    
    with tab_del:
        usuarios_dict = {usuario.nome: usuario for usuario in usuarios} 
        nome_usuario = st.selectbox(
            'Selecione o usuário para deletar', 
            usuarios_dict.keys())
        usuario = usuarios_dict[nome_usuario]
        
        if st.button('Deletar'):
            deleta_usuario(usuario.id)
            st.rerun()

def limpar_datas():
    del st.session_state['data_inicio']
    del st.session_state['data_final']

def pagina_calendario():

    with open('calendar_options.json') as f:
        calendar_options = json.load(f)

    usuarios = le_todos_usuarios()
    
    calendar_events = []
    for usuario in usuarios:
        calendar_events.extend(usuario.lista_ferias())

    usuario = st.session_state['usuario']
 
    # calendar_events = [
    #     {
    #         "title": "Férias do Jobs",
    #         "start": "2025-05-19T08:30:00",
    #         "end": "2025-06-17T10:30:00",
    #         "resourceId": "a",
    #     },
    # ]

    calendar_widget = calendar(events=calendar_events, options=calendar_options)

    if ('callback' in calendar_widget 
        and calendar_widget['callback'] ==  'dateClick'):
    
        raw_date = calendar_widget['dateClick']['date']
        if raw_date != st.session_state['ultimo_clique']:

            st.session_state['ultimo_clique'] = raw_date
            
            date = calendar_widget['dateClick']['date'].split('T')[0]
            st.write(date)
            if not 'data_inicio' in st.session_state:
                st.session_state['data_inicio'] =  date
                st.warning(f'Data de inicio de férias selecionada {date}')
            else:
                st.session_state['data_final'] = date
                date_inicio = st.session_state['data_inicio']
                cols = st.columns([0.7, 0.3])
                with cols[0]:
                    st.warning(f'Data de inicio de férias selecionada {date_inicio}')
                # LIMPAR
                with cols[1]:
                    st.button('Limpar', 
                              use_container_width=True, 
                              on_click=limpar_datas)
                        
                cols = st.columns([0.7, 0.3])
                with cols[0]:
                    st.warning(f'Data final de férias selecionada {date}')
                with cols[1]:
                    st.button('Adicionar Férias', 
                              use_container_width=True, 
                              on_click=usuario.adicionar_ferias,
                              args=(date_inicio, date))

def pagina_principal():
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
        with st.sidebar:
            tab_gestao_usuarios()
        
    else:
        pagina_calendario()
                    
def main():
    if not 'logado' in st.session_state:
        st.session_state['logado'] = False
    if not 'pag_gestao_usuarios' in st.session_state:
        st.session_state['pag_gestao_usuarios'] = False
        if not 'ultimo_clique' in st.session_state:
            st.session_state['ultimo_clique'] = ''

    if not st.session_state['logado']:
        login()
    else:
        pagina_principal()
    
if __name__ == '__main__':
    main()