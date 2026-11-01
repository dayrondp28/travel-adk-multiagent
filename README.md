# Travel ADK Multiagent

Laboratorio UCV de sistema multiagente de viajes con Google ADK.

## Agentes

- Travel Coordinator Agent
- Web Search Agent
- Itinerary Agent
- Budget Agent
- Risk Reviewer Agent

## Instalación

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install poetry
    poetry install

## Variables de entorno

Crear un archivo `.env` a partir de `.env.example` y colocar la clave real:

    GOOGLE_API_KEY="TU_API_KEY"

## Ejecutar agente por consola

    poetry run adk run travel_assistant

## Ejecutar agente web

    poetry run adk web --port 8000

Abrir http://localhost:8000

## Ejecutar pruebas

    poetry run pytest

## Ejecutar lint

    poetry run ruff check .