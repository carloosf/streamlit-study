import streamlit as st

st.title('Hi, My name is Carlos')
st.write('My study for Streamlit FrameWork Python open and available below')


st.sidebar.page_link(page='https://github.com/carloosf',
                     label='Repository Here', icon='👨‍💻')
st.sidebar.page_link(
    page='https://www.linkedin.com/in/carloosf', label='Linkedin', icon='👔')
st.sidebar.page_link(
    page='https://www.instagram.com/carloosf.__', label='Instagram', icon='📱')
st.sidebar.page_link(
    page='http://mailto:contato.carlossilvaf@gmail.com', label='E-Mail', icon='✉️')
