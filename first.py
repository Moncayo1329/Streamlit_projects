import streamlit as st 

#titulo 

st.title("🎉 Mi Primera App con Streamlit")

st.write("¡Hola! Esto es una app web hecha solo con Python.")

# Un widget sencillo: slider 

edad = st.slider ("¿Cuántos años tienes?", 0, 100, 25)

st.write(f"¡Genial! Tienes **{edad}** años.")

# Otro widget: botón
if st.button("Haz clic aquí"):
    st.success("¡Botón presionado! 🎈 Streamlit es muy fácil, ¿verdad?")

# Puedes agregar más cosas fácilmente
nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.write(f"¡Hola, {nombre}! 👋")