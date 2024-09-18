import streamlit as st
import pandas as pd 
st.header('file upload app 2')
file= st.file_uploader('choose a file',type=['csv','xlsx'])
if file is not None:
  df= pd.read_csv(file)
  st.write(df)
  num_row=st.slider('chosse num rows',min_value=0,max_value=len(df),step=1)
name_column=st.multiselect('choose name of columns',df.columns.to_list())
st.write(df[:num_row][name_column])

if name_column:
  st.write(df[:num_row][name_column])
else:
  st.write(df[:num_row])
fig=px.scatter(df,x='population',y='total_rooms') 
st.plotly_chart(fig)

