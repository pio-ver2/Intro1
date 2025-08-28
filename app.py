import streamlit as st
from PIL import Image

st.title( "Te amo mi nalgona favorita")

st.header("dame un beso")
st.write("original en que aspecto?")
image = Image.open('gato.jpg')

st.image(image, caption ='interfac multimodales')


texto = st.text_input('Tu eres mi mundo entero mi negra', 'Ramon')
st.write('camila llega ya plis :C', texto)
