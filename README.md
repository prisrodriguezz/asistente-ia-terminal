# Asistente IA en Terminal

Proyecto desarrollado en Python que permite interactuar con un asistente de inteligencia artificial desde la terminal utilizando la API de Groq.

## Funcionalidades

- Chat interactivo en terminal
- Memoria persistente mediante JSON
- Manejo básico de errores
- Lectura de archivos `.txt`
- Generación automática de resúmenes
- Exportación de resúmenes en archivos `.txt`

## Comandos disponibles

### Chat
- `/help` → Mostrar ayuda
- `/tools` → Entrar en modo herramientas
- `/history` → Ver historial de conversación
- `/clear` → Borrar memoria del chat
- `/exit` → Cerrar el asistente

### Modo Herramientas
- `/read` → Leer archivo .txt
- `/summarize` → Generar resumen
- `/export` → Exportar resumen
- `/return` → Volver al chat

## Tecnologías utilizadas

- Python
- Groq API
- JSON
- python-dotenv

## Instalación

1. Clonar repositorio

```bash
git clone https://github.com/prisrodriguezz/asistente-ia-terminal.git
```

2. Crear entorno virtual

```bash
python -m venv .venv
```

3. Activar entorno virtual

### Windows

```bash
.\.venv\Scripts\Activate
```

4. Instalar dependencias

```bash
pip install -r requirements.txt
```

5. Crear archivo `.env`

```env
GROQ_API_KEY=tu_api_key
```

## Ejecutar proyecto

```bash
python -m app.main
```

## Objetivo del proyecto

Este proyecto fue desarrollado con el objetivo de aprender:

- Consumo de APIs
- Manejo de contexto conversacional
- Persistencia de datos
- Organización de código en Python
- Desarrollo de asistentes IA por terminal
