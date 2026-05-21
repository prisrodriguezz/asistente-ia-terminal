# Importamos la clase load_dotenv para cargar variables del archivo .env
from dotenv import load_dotenv
import os   # Importamos os para acceder a variables de entorno

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "openai/gpt-oss-120b"