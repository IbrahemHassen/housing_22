import streamlit as st
import pandas as pd 
st.header('file upload app 2')
file= st.file_uploader('choose a file',type=['csv','xlsx'])
if file is not None:
  df= pd.read_csv(file)
  st.write(df)
