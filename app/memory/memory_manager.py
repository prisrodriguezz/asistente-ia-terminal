import json

MEMORY_PATH = "app/memory/memory.json"

# Memoria por defecto
DEFAULT_MEMORY = [
    {
        "role": "system",
        "content": "Eres un asistente amigable y útil."
    }
]

# Cargar memoria
def load_memory():

    try:

        # Abre el archivo memory.json y lo lee, convierte JSON a Python y retorna la memoria guardada
        with open(MEMORY_PATH, "r", encoding="utf-8") as file:

            return json.load(file)

    except FileNotFoundError:

        return DEFAULT_MEMORY.copy()

# Guardar memoria
def save_memory(messages):

    with open(MEMORY_PATH, "w", encoding="utf-8") as file:

        json.dump(  # convierte python en json
            messages,
            file,
            ensure_ascii=False,
            indent=4
        )

# Limpiar memoria
def clear_memory():

    save_memory(DEFAULT_MEMORY)     # Sobrescribe el archivo memory.json con la memoria por defecto

    return DEFAULT_MEMORY.copy()