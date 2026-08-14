import anthropic
import os
import requests

clave = os.environ.get("OPENWEATHER_API_KEY")

cliente = anthropic.Anthropic()

herramientas = [
    {
        "name": "consultar_temperatura",
        "description": "Consulta la temperatura de una ciudad",
        "input_schema": {
            "type": "object",
            "properties": {
                "ciudad": {"type": "string", "description": "nombre de ciudad"}
            },
            "required": ["ciudad"]
        }
    },
    {
        "name": "consultar_edad_estimada",
        "description": "Predice la edad segun su nombre",
        "input_schema": {
            "type": "object",
            "properties": {
                "nombre": {"type": "string", "description": "nombre de una persona"}
            },
            "required": ["nombre"]
        }
    }
]

historial = [
    {"role": "user", "content": "¿Cuantos años tiene Javier?"}
]

respuesta1 = cliente.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    tools=herramientas,
    messages=historial
)

bloque_herramienta = respuesta1.content[1]

if bloque_herramienta.name == "consultar_temperatura":
    ciudad_pedida = bloque_herramienta.input['ciudad']
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad_pedida}&appid={clave}&units=metric"
    respuesta_temp = requests.get(url)
    datos_temp = respuesta_temp.json()
    resultado = datos_temp['main']['temp']

elif bloque_herramienta.name == "consultar_edad_estimada":
    nombre_pedido = bloque_herramienta.input['nombre']
    url = f"https://api.agify.io?name={nombre_pedido}"
    respuesta_edad = requests.get(url)
    datos_edad = respuesta_edad.json()
    resultado = datos_edad['age']

historial.append({"role": "assistant", "content": respuesta1.content})
historial.append({
    "role": "user",
    "content": [
        {
            "type": "tool_result",
            "tool_use_id": bloque_herramienta.id,
            "content": str(resultado)
        }
    ]
    }
)

respuesta2 = cliente.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    tools=herramientas,
    messages=historial
)

print(respuesta2.content[0].text)
print(respuesta2.stop_reason)