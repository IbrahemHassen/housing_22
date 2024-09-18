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
  
num_col=df.select_dtypes(include='number').columns.to_list()
x_axis=st.selectbox('choose x axis',num_col)
y_axis=st.selectbox('choose y axis',num_col)
color=st.selectbox('choose color',num_col)
fig=px.scatter(df,x=x_axis,y=y_axis,color=color) 
st.plotly_chart(fig)

