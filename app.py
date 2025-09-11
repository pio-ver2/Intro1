import streamlit as st
from PIL import Image

st.title( "Oliver es un gato gordo")

st.header("Dile hola a Oliver")
st.write("Este es oliver ")
image = Image.open('Oli.jfif')

st.image(image, caption ='interfac multimodales')


texto = st.text_input('Que miras', 'Holis')
st.write('Alguien huele feo', texto)
