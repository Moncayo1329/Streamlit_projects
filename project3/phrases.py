import streamlit as st 
import random

st.title("Bible phrases  generate") 

st.write("Bible phrases") 

# list de frases 
phrases = [
     "Dios es amor ❤️",
    "Todo lo puedo en aquel que me fortalece",
    "El Señor es mi pastor, nada me faltará",
    "Confía en el plan de Dios",
    "Ora y no te rindas 🙏"
 ]

if st.button("Give me a phrase"):  
   selected_phrase = random.choice(phrases)
   
# Solo una frase
   st.success("📖 " + selected_phrase)