# Funcion que recibe la ruta de un archivo .txt como string y devuelve su contenido como string
def read_txt_file(file_path: str) -> str:
    """
    Lee un archivo de texto y devuelve su contenido como string.
    """

    try: 
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return "Archivo no encontrado"
    
    except Exception as e:
        return f"Error leyendo archivo: {str(e)}"