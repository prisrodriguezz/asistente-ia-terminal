# Importamos la clase Groq para conectarnos a la IA
from groq import Groq
from app.config.settings import GROQ_API_KEY, MODEL_NAME

# Creamos el cliente para interactuar con la API de Groq usando la API Key
client = Groq(
    api_key=GROQ_API_KEY
)

# Enviamos TODA la conversación a la IA para que recuerde el contexto
def send_message(messages):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages
    )

    return response.choices[0].message.content # Extraemos solamente el texto de la respuesta