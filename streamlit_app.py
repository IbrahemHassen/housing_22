import streamlit as st

name= st.text_input('Enter your name')
btn= st.button('show')
if btn:
  st.write(f'Hello{name}') 

# app 1

st.header('calculate area')
choose=st.selectbox('choose the shape',['rectangle','circle'])

if choose=='circle':
  r=st.number_input('enter the radius',min_value=1,max_value=100)
  area=3.14*r*r
  st.write(f'area of circle is {area}') 
elif choose=='rectangle':
  l=st.number_input('enter the length',min_value=1,max_value=100)
  b=st.number_input('enter the breadth',min_value=1,max_value=100)
  area=l*b

btn=st.button('calculate')

if btn:
  st.write(f'the area is {area}')
