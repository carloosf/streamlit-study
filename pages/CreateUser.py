import streamlit as st

with st.form('createUser'):
    username = st.text_input(label='Username')
    pw = st.text_input(label='Password', type='password')
    pwConfirm = st.text_input(label='Confirm Password', type='password')
    submit = st.form_submit_button('createUser')
