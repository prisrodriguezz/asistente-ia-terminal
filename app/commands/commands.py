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