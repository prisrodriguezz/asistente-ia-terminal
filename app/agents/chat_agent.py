import os
from app.services.groq_service import send_message

from app.memory.memory_manager import (
    load_memory,
    save_memory,
    clear_memory
)

from app.commands.commands import (
    show_help,
    show_history,
    show_tools
)

# Importacion de herramientas
from app.tools.file_reader import read_txt_file


class ChatAgent:

    def __init__(self):     # self hace referencia al objeto actual

        self.messages = load_memory() # Cargar memoria

        self.mode = "chat"  # Inicia en modo chat

        self.current_file = None    # Archivo actual para utilizar en modo herramientas

    def start(self):

        print("Asistente IA iniciado")
        print("Escribí '/help' para ver comandos disponibles \n")

        while True:
            if self.mode == "chat":
                user_input = input("Tú: ").strip()
                self.handle_chat(user_input)
            
            elif self.mode == "tools":
                user_input = input("Tools: ").strip()
                self.handle_tools(user_input)


    
    # Funcion que maneja los comandos de herramientas
    def handle_tools(self, user_input):

        # Menu de herramientas
        if user_input == "/tools":
            show_tools()
            return
        
        # Volver al chat
        if user_input == "/return":
            self.mode = "chat"
            print("Volviendo al chat...\n")

            print("\n=== CHAT ACTIVADO ===")
            print("Escribí '/help' para ver comandos disponibles \n")
            return

        # Leer archivo
        if user_input == "/read":

            file_path = input("Ingrese ruta del archivo: ").strip()     # strip() elimina espacios vacios

            # Validaciones 
            # -- Existencia
            if not os.path.exists(file_path):
                print("\nEl archivo no existe\n")
                return

            # -- Extension del arhivo
            if not file_path.endswith(".txt"):
                print("\nEl archivo no es valido. Solo se admite archivos .txt\n")
                return            

            content = read_txt_file(file_path)

            # Guardar archivo actual
            self.current_file = {

                "path": file_path,
                "content": content
            }

            print("\nArchivo cargado correctamente\n")
            print("\n========== CONTENIDO ==========\n")
            print(content[:500])  # Para archivos grandes solo se realiza una previsualizacion
            print("\n===============================\n")

            show_tools()

            return
        

    # Funcion para el chat normal
    def handle_chat(self, user_input):

        # Mostrar comandos disponibles
        if user_input == "/help":
            show_help()
            return

        # Mostrar historial completo
        if user_input == "/history":
            show_history(self.messages)
            return

        # Borrar memoria del chat
        if user_input == "/clear":

            self.messages = clear_memory()

            print("Memoria borrada\n")

            return

        # Cerrar asistente
        if user_input == "/exit":

            print("Asistente: ¡Hasta luego!")
            exit()

        # Utilizar herramientas
        if user_input == "/tools":

            self.mode = "tools"
            show_tools()

            return

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

            return


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