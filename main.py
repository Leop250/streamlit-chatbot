import os
import streamlit as st
from mistralai import Mistral

# Obtenir la clé API à partir des variables d'environnement
api_key = os.environ.get("VOTRE CLE API") 
model = "mistral-large-latest"

# Vérifier si la clé API est définie
if api_key is None:
    st.error("La clé API Mistral n'est pas définie dans les variables d'environnement.")
    st.stop()  # Arrêter l'application si la clé API n'est pas disponible

# Initialiser le client Mistral
client = Mistral(api_key=api_key)

def generate_response(user_input):
    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                },
            ]
        )

        # Retourner la réponse du bot
        return chat_response.choices[0].message.content

    except Exception as e:
        return f"Erreur : {str(e)}"

# Configuration de Streamlit
st.title("Chatbot avec Mistral AI")
st.write("Bienvenue sur l'interface de chatbot. Posez-moi des questions !")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')

if submit_button and user_input:
    response = generate_response(user_input)
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Affichage de l'historique des échanges
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")
