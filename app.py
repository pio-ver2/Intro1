import streamlit as st
from PIL import Image

# Establecer el fondo azul oscuro con CSS
st.markdown("""
    <style>
        body {
            background-color: #1e2a47;  /* Fondo azul oscuro */
            color: #ffffff;  /* Texto en color blanco */
        }
        .stTitle {
            color: #f4a261;  /* Título con un color cálido */
        }
        .stHeader {
            color: #ffb703;  /* Cabecera en un tono dorado */
        }
        .stTextInput>div>div>input {
            background-color: #4c6a92;  /* Fondo del campo de texto */
            color: white;  /* Texto en el campo de texto en blanco */
            border-radius: 10px;
        }
        .stImage>div>img {
            border-radius: 15px;  /* Bordes redondeados para la imagen */
        }
    </style>
""", unsafe_allow_html=True)

# Título relacionado con las medusas
st.title("Las Medusas: Criaturas Fascinantes del Mar")

# Introducción sobre las medusas
st.header("¡Bienvenidos al Mundo de las Medusas!")
st.write("Las medusas son animales marinos invertebrados que existen desde hace más de 500 millones de años. Aunque su cuerpo es mayormente agua, son criaturas fascinantes con increíbles habilidades.")

# Mostrar una imagen de una medusa
image = Image.open('medusa.jpg')  # Asegúrate de tener una imagen de medusa en el directorio
st.image(image, caption="Medusa: Una de las criaturas más antiguas y misteriosas del mar")

# Interacción con el usuario
texto = st.text_input('¿Qué sabes sobre las medusas?', 'Son animales marinos')
st.write(f"Interesante, parece que sabes algo sobre las medusas: {texto}")

# Añadir una pequeña curiosidad sobre las medusas
st.write("Dato curioso: ¡Algunas medusas son bioluminiscentes y pueden producir luz propia!")

