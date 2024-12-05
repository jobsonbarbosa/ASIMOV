import streamlit as st
import pandas as pd
import time

st.set_page_config(
    layout="wide",
    page_title="Spotify Songs"
)

st.title('Brasquimica')

# - O decorador usado para protejer a função, guardando a função 
@st.cache_data
def load_data():

    df = pd.read_csv('dataset\\01 Spotify.csv')    
    # operação pesada
    time.sleep(5) # simula o atraso ou carregamento de dados
    return df

    # - st.session_state - abre um sessão para cada conexão ou usuário que esteja acessando o sistema.
st.session_state['df_spotify'] = load_data()

df = load_data()

df.set_index("Track", inplace=True)

artists = df['Artist'].value_counts().index
artist = st.sidebar.selectbox("Artista", artists )
df_filtered = df[df['Artist'] == artist]

# Seleção em cadeia
albuns = df_filtered['Album'].value_counts().index
album = st.selectbox("ALbum", albuns )
df_filtered2 = df[df['Album'] == album]

# agree = st.checkbox('Display')
# if agree:
#     st.bar_chart(df_filtered2['Stream'])

col1, col2 = st.columns([0.7, 0.3])

col1.bar_chart(df_filtered2['Stream'])
col2.line_chart(df_filtered2['Danceability'])

    
    
st.write(artist)