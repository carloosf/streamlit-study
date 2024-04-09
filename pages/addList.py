import streamlit as st
from datetime import datetime

st.title('Studying session state in Input')

# Function to append data and clear input
def handle_input(text):
    st.session_state['text_input'] = text
    if text:
        st.session_state['df'].append({'content': text, 'hour': datetime.now(
        ).strftime("%H:%M:%S"), 'date': datetime.now().strftime("%d/%m/%Y")})
        st.session_state['text_input'] = ''  # Clear input after append

# Session state for the text input
if 'text_input' not in st.session_state:
    st.session_state['text_input'] = ''

# Criar o session_state chamado df caso ele nao exista
if 'df' not in st.session_state:
    st.session_state['df'] = []

# Observador para quando o texto mudar
def handle_text_change():
    text = st.session_state['text_input']  # Access current input value
    handle_input(text)  # Call the function with the current text

# Crio um input para interagir e testar
st.text_input(label='', placeholder='Write Here..', key='text_input',
              on_change=handle_text_change)

st.write(st.session_state)
