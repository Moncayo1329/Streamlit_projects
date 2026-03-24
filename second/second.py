import streamlit as st 

st.title("Mi asistente diario")

st.write("Una mini app útil para el día a día")

#Selector de humor del dia a dia. 

humor = st.select_slider(
     "¿Cómo te sientes hoy?",
    options=["😩 Terrible", "🙁 Regular", "😐 Normal", "🙂 Bien", "😄 Excelente"]
)


# Recordatorio rapido 

Tarea = st.text_input("¿Qué tarea importante tienes hoy?")
if st.button("Guardar tarea"):
    st.success(f"✅ Guardado: {tarea}")

#Mini lista de pendientes 

st.subheader("Mis pendientes rápidos")
pendientes = st.multiselect("Marca lo que ya hiciste:", 
    ["Tomar agua", "Hacer ejercicio", "Responder mensajes", "Comer saludable", "Descansar 10 min"])

if pendientes:
    st.balloons()

# Consejo aleatorio del día
if st.button("Dame un consejo random"):
    consejos = [
        "Bebe un vaso de agua ahora mismo 💧",
        "Respira profundo 3 veces",
        "Levántate y estírate",
        "Di algo bonito a alguien",
        "Sonríe aunque no tengas ganas 😊"
    ]
    st.info("💡 " + consejos.__getitem__(__import__('random').randint(0,4)))