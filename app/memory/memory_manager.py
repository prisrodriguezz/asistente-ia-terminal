import json

MEMORY_PATH = "app/memory/memory.json"

DEFAULT_MEMORY = [
    {
        "role": "system",
        "content": "Eres un asistente amigable y útil."
    }
]

# Cargar memoria
def load_memory():

    try:

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

    save_memory(DEFAULT_MEMORY)

    return DEFAULT_MEMORY.copy()