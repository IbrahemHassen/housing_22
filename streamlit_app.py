import streamlit as st
import pandas as pd 
import plotly.express as px
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
  
num_col = df.select_dtypes(include='number').columns.to_list()

col1,col2,col3 = st.columns(3)
with col1:
 x_col = st.selectbox('choose x column',num_col)
with col2:
  y_col = st.selectbox('choose y column',num_col)
with col3:
  color = st.selectbox('choose color',df.columns.to_list())


fig = px.scatter(df,x=x_col,y=y_col,color=color)
st.plotly_chart(fig)
x=st.selectbox('choose x axis',num_col)
fig=px.histogram(df,x=x)
st.plotly_chart(fig2)
