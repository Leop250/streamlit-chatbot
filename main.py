import streamlit as st
from Mistral import *
# Import the appropriate client library for Mistral API (hypothetical)
# from mistral_sdk import Mistral  # Example, adjust according to the actual SDK

def generate_response(user_input):
    api_key = "tjyXiDGjeI1mw4ws5o0P2LSHcpXI75PZ"
    model = "mistral-large-latest"

    # Initialize the client (example)
    client = Mistral(api_key=api_key)

    try:
        #
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": user_input,  
                },
            ]
        )

        return chat_response['choices'][0]['message']['content']

    except Exception as e:
        # Handle errors and return an error message
        return f"Erreur : {str(e)}"


# Titre de l'application
st.title("Chatbot avec Streamlit")
st.write("Bienvenue sur l'interface de chatbot. Posez-moi des questions !")

# Historique de chat
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Formulaire pour la saisie de l'utilisateur
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')

# Affichage des réponses et ajout à l'historique
if submit_button and user_input:
    response = generate_response(user_input)
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Boucle pour afficher l'historique des messages
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")