import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')
a = st.file_uploader(label='add data', accept_multiple_files=False,)

if a is not None:
  b = pd.read_csv(a, sep=';')
  st.dataframe(b)