# Bloque 2 — Automatización con n8n

Proyecto integrador del bloque de automatización, construido en n8n Cloud durante las Sesiones 1-6.

## ¿Qué hace este workflow?

Consulta el clima actual de Huelva mediante una API externa (OpenWeatherMap), evalúa si la temperatura supera un umbral definido, y notifica el resultado por dos canales distintos: un webhook de prueba y un correo electrónico real vía Gmail.

## Flujo del workflow

1. **Trigger** (manual y programado por horario) — inicia la ejecución.
2. **Edit Fields** — genera datos base de identificación.
3. **HTTP Request (GET)** — consulta una API pública sin autenticación (agify.io) como primer ejercicio de integración.
4. **HTTP Request (GET, autenticado)** — consulta el clima actual de Huelva en OpenWeatherMap, usando autenticación por API key gestionada de forma segura con el sistema de Credentials de n8n.
5. **IF** — evalúa si la temperatura supera los 35°C.
6. **Notificación dual**:
   - Rama True/False → mensaje personalizado según el resultado.
   - Envío del mensaje mediante POST a un endpoint externo (probado con webhook.site).
   - Envío de un correo electrónico real mediante el nodo Gmail, autenticado con OAuth2 y un proyecto propio en Google Cloud Console.

## Conceptos aplicados

- Nodos Trigger, HTTP Request (GET/POST), IF, Edit Fields, Schedule Trigger, Gmail.
- Autenticación con API key (Query Auth) y con OAuth2 (Client ID/Secret, pantalla de consentimiento, test users).
- Expresiones de n8n (`{{ $json.campo }}`) para pasar datos entre nodos.
- Publicación/despublicación de workflows para activar disparadores programados.

## Archivo del workflow

El archivo [`workflow-alerta-clima.json`](./workflow-alerta-clima.json) contiene el workflow exportado, listo para importar en cualquier instancia de n8n (Cloud o self-hosted).
