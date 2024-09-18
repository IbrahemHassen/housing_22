import streamlit as st
import time

st.sidebar.title('sidebar')
area= None
st.header('calculate area')
with st.sidebar:
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
  with st.spinner('calculating...'):
    time.sleep(5)
  st.write(f'the area is {area}')
