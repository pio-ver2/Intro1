import streamlit as st
from PIL import Image


st.title("Las Medusas: Criaturas Fascinantes del Mar")


st.header("¡Bienvenidos al Mundo de las Medusas!")
st.write("Las medusas son animales marinos invertebrados que existen desde hace más de 500 millones de años. Aunque su cuerpo es mayormente agua, son criaturas fascinantes con increíbles habilidades.")


image = Image.open('medusas.png')  
st.image(image, caption="Medusa: Una de las criaturas más antiguas y misteriosas del mar")


texto = st.text_input('¿Qué sabes sobre las medusas?', 'Son animales marinos')
st.write(f"Interesante, parece que sabes algo sobre las medusas: {texto}")


st.write("Dato curioso: ¡Algunas medusas son bioluminiscentes y pueden producir luz propia!")
