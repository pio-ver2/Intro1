import streamlit as st
from PIT import image

st.title( "Te amo mi negra favorita")

st.header("dame un beso")
st.write("original en que aspecto?")
image = Image.open('gato.jpg')

st.image(image, caption ='interfac multimodales')

