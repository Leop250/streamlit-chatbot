import streamlit as st
# Import the appropriate client library for Mistral API (hypothetical)
# from mistral_sdk import Mistral  # Example, adjust according to the actual SDK

def generate_response(user_input):
    api_key = "VOTRE CLE API"
    model = "mistral-large-latest"

    # Initialize the client (example)
    client = Mistral(api_key=api_key)

    try:
        # Send the user input to the model and get a response
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": user_input,  # Using user input dynamically
                },
            ]
        )

        # Extract the response content (adjust based on API response structure)
        return chat_response['choices'][0]['message']['content']

    except Exception as e:
        # Handle errors and return an error message
        return f"Erreur : {str(e)}"
