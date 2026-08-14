# Bloque 3 — APIs de LLMs con Python

Scripts de práctica y proyecto integrador construidos durante el Bloque 3, usando la API de Anthropic (Claude) desde Python.

## Progresión de scripts

- `primera_llamada.py` — primera llamada básica a la API, estructura cliente/mensaje/respuesta.
- `system.py` — comparación del parámetro `system` con distintas personalidades del modelo.
- `content_ext.py` — conexión de la API de Claude con datos externos reales (OpenWeatherMap), construyendo mensajes dinámicos con f-strings.
- `tool_use_temp.py` — primer ejercicio de tool use (function calling): una única herramienta, ciclo completo de petición → ejecución → resultado.

## Proyecto de cierre — `asistente_agente.py`

Asistente conversacional multi-turno con capacidad de agente, construido combinando todas las piezas del bloque:

- **Historial multi-turno**: el usuario puede hacer varias preguntas seguidas dentro de la misma sesión, y el modelo mantiene el contexto de la conversación.
- **`system` propio**: personalidad definida para el asistente.
- **Dos herramientas reales conectadas a APIs externas**:
  - `consultar_temperatura` (OpenWeatherMap)
  - `consultar_edad_estimada` (agify.io)
- **Manejo robusto de `stop_reason`**: el asistente distingue correctamente entre cuando Claude necesita usar una herramienta (`tool_use`) y cuando puede responder directamente con su propio conocimiento (`end_turn`), sin asumir un único camino fijo.
- **Bucle de conversación abierto** (`while True`), con salida controlada por el usuario.

## Cómo ejecutarlo

Requiere las variables de entorno `ANTHROPIC_API_KEY` y `OPENWEATHER_API_KEY` configuradas en el sistema, y las librerías `anthropic` y `requests` instaladas (`pip install anthropic requests`).

```powershell
python asistente_agente.py
```

## Conceptos aplicados

- Cliente de la API de Anthropic, roles `user`/`assistant`, parámetro `system`.
- Tool use / function calling: definición de herramientas con `input_schema`, lectura de `stop_reason`, construcción de `tool_result` con `tool_use_id`.
- Integración con APIs externas desde Python (librería `requests`), reutilizando el patrón ya dominado en n8n (Bloque 2).
- Manejo de errores y variables de entorno para credenciales seguras.
