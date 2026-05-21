# Importamos la clase Groq para conectarnos a la IA y load_dotenv para cargar variables del archivo .env
from groq import Groq
from dotenv import load_dotenv
import os # Importamos os para acceder a variables de entorno
import json

load_dotenv()

# Creamos el cliente de Groq usando la API Key
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


print("Asistente IA iniciado")
print("Escribí '/exit' para terminar\n")

# Funcion de ayuda
def show_help():

    print("""
        Comandos disponibles:

        /help     → Mostrar ayuda
        /history  → Ver historial
        /clear    → Borrar memoria
        /exit     → Salir
    """)

# Funcion historial
def show_history(messages):

    print("\n=== HISTORIAL ===")

    for message in messages:

        print(f"{message['role']}: {message['content']}")

    print("=================\n")

# Funcion limpiar memoria
def clear_memory():

    print("Memoria borrada\n")

    return [
        {
            "role": "system",
            "content": "Eres un asistente amigable y útil."
        }
    ]

# Enviamos TODA la conversación a la IA para que recuerde el contexto
def send_message(messages):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    return response.choices[0].message.content  # Extraemos solamente el texto de la respuesta


# Guardar memoria
def save_memory(messages):

    with open("memory.json", "w", encoding="utf-8") as file:

        json.dump(  # convierte python en json
            messages,
            file,
            ensure_ascii=False,
            indent=4
        )

# Cargar memoria
def load_memory():

    try:

        with open("memory.json", "r", encoding="utf-8") as file:

            return json.load(file)

    except FileNotFoundError:

        return [
            {
                "role": "system",
                "content": "Eres un asistente amigable y útil."
            }
        ]
    
# Lista que almacena TODA la conversación (la IA guarda memoria del chat)
messages = load_memory()


# Bucle infinito para mantener el chat activo
while True:
    user_input = input("Tú: ").strip()

    # Mostrar comandos disponibles
    if user_input == "/help":
        show_help()
        continue

    # Mostrar historial completo
    if user_input == "/history":
        show_history(messages)
        continue

    # Borrar memoria del chat
    if user_input == "/clear":
        messages = clear_memory()
        save_memory(messages)
        continue

    # Cerrar asistente
    if user_input.lower() == "/exit":
        print("Asistente: ¡Hasta luego!")
        break
    
    # Guardamos el mensaje del usuario en el historial
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Manejo de error
    try:
        assistant_reply = send_message(messages)

    except Exception as error:
        print("Ocurrió un error")

        continue    # si falla vuelve al inicio del while

    # Mostrar respuesta
    print(f"Asistente: {assistant_reply}\n")

    # Guardar respuesta del asistente (esto permite mantener el contexto)
    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    # Guardar memoria en JSON
    save_memory(messages)