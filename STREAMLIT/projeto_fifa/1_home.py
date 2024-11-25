import streamlit as st
import pandas as pd
from datetime import datetime
import webbrowser

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    
    # Jogadores que tenha contrato valido até a data atual
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    
    # Excluir jogadores que não tenham valores registrador
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state["data"] = df_data

    
    

st.markdown("# Jobs Solutions - FIFA OFFICIAL DATASET!")
st.sidebar.markdown("Desenvolvido por Jobs Solutions IT")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/")
    
st.markdown(
    """
    O conjunto de dados
    de jogadores de 2017 a 2023 fornece informações
    abrangentes sobre jogadores de futbok profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos
    do jogador, característivas físicas, estatíticas de jogo, detalhes do contrato e afiliações de clubes.
    
    Com **mais de 17.000 resgitros**, este conjuto de dados oferece um recurso valioso para
    analistas de futbol, pesquisadores e entusiastas interessados em explorar vários
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo
    """
)