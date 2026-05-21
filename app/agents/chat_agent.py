from app.services.groq_service import send_message

from app.memory.memory_manager import (
    load_memory,
    save_memory,
    clear_memory
)

from app.commands.commands import (
    show_help,
    show_history
)

class ChatAgent:

    def __init__(self):

        self.messages = load_memory() # Cargar memoria

    def start(self):

        print("Asistente IA iniciado")
        print("Escribí '/help' para ver comandos disponibles \n")


        # Bucle infinito para mantener el chat activo
        while True:

            user_input = input("Tú: ").strip()

            # Mostrar comandos disponibles
            if user_input == "/help":
                show_help()
                continue

            # Mostrar historial completo
            if user_input == "/history":
                show_history(self.messages)
                continue

            # Borrar memoria del chat
            if user_input == "/clear":

                self.messages = clear_memory()

                print("Memoria borrada\n")

                continue

            # Cerrar asistente
            if user_input == "/exit":

                print("Asistente: ¡Hasta luego!")

                break

            # Guardar mensaje del usuario en el historial
            self.messages.append(
                {
                    "role": "user",
                    "content": user_input
                }
            )

            # Manejo de error
            try:

                assistant_reply = send_message(self.messages)

            except Exception as error:

                print("Ocurrió un error:", error)

                continue    # si falla vuelve al inicio del while


            # Mostrar respuesta
            print(f"Asistente: {assistant_reply}\n")

            # Guardar respuesta del asistente (esto permite mantener el contexto)
            self.messages.append(
                {
                    "role": "assistant",
                    "content": assistant_reply
                }
            )

            # Guardar memoria en JSON
            save_memory(self.messages)