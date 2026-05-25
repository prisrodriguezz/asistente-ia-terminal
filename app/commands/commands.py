# Funcion de ayuda
def show_help():

    print("""
Comandos disponibles:

/help     → Mostrar ayuda
/tools    → Ver herramientas
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

# Funcion herramientas
def show_tools():
    print("""
===============================
>>>>>> MODO HERRAMIENTAS <<<<<<
===============================
          
Herramientas disponibles:

/read        → Leer archivo .txt
/summarize   → Generar resumen
/export      → Exportar resumen
/return      → Volver al chat
""")