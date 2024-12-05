import json

import streamlit as st

from streamlit_calendar import calendar

with open('calendar_options.json') as f:
    calendar_options = json.load(f)

if not 'ultimo_clique' in st.session_state:
    st.session_state['ultimo_clique'] = ''

def limpar_datas():
    del st.session_state['data_inicio']
    del st.session_state['data_final']

calendar_events = [
    {
        "title": "Férias do Jobs",
        "start": "2025-05-19T08:30:00",
        "end": "2025-06-17T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "start": "2023-07-31T07:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
        "resourceId": "a",
    }
]

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
                st.button('Limpar', use_container_width=True, on_click=limpar_datas)
                    
            cols = st.columns([0.7, 0.3])
            with cols[0]:
                st.warning(f'Data final de férias selecionada {date}')
            with cols[1]:
                st.button('Adicionar Férias', use_container_width=True)

        

st.write(calendar_widget)