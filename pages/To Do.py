import streamlit as st
from datetime import datetime


st.title('Studying session state in Input')

selected_ids = []
newDf = []


def handle_input(text):
    # Function to append data and clear input
    st.session_state['text_input'] = text
    unique_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
    if text:
        st.session_state['df'].append({'id': unique_id, 'content': text, 'hour': datetime.now(
        ).strftime("%H:%M:%S"), 'date': datetime.now().strftime("%d/%m/%Y")})
        st.session_state['text_input'] = ''  # Clear input after append


def remove_ids():
    # Remove ids selecinados
    for tasks in st.session_state['df']:
        if tasks['id'] not in selected_ids:
            newDf.append(tasks)
    st.session_state['df'] = newDf


def handle_text_change():
    # Observador para quando o texto mudar
    text = st.session_state['text_input']
    handle_input(text)


# Session state for the text input
if 'text_input' not in st.session_state:
    st.session_state['text_input'] = ''

# Criar o session_state chamado df caso ele nao exista
if 'df' not in st.session_state:
    st.session_state['df'] = []


# Crio um input para interagir e testar
st.text_input(label=' ', placeholder='Write Here..', key='text_input',
              on_change=handle_text_change)

st.button(label='Apagar Selecionados', on_click=remove_ids)

# Exibir checkbox para cada ID
for item in st.session_state['df']:
    if st.checkbox(label=item['content'], key=item['id']):
        if item['id'] not in selected_ids:
            selected_ids.append(item['id'])
