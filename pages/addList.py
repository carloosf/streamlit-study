import streamlit as st

# Função de limpar o input
def clearInput():
    st.session_state.my_text = st.session_state.stateInitInput
    st.session_state.stateInitInput = ""
st.write(st.session_state)
# Criar o session_state chamado df caso ele nao exista
if 'df' not in st.session_state:
    st.session_state['df'] = []

# Crio um input para interagir e testar
data = st.text_input(label='Teste', key='stateInitInput', on_change=clearInput)
st.write(st.session_state.get('my_text'))
# Faço o append dentro do session_state df
if data:
    st.session_state['df'].append()
    
st.write(st.session_state.get('df'))
# Apresento o session_state chamado df
for c in st.session_state['df']:
    st.write(c)
