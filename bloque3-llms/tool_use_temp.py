import anthropic
import requests
import os

clave = os.environ.get("OPENWEATHER_API_KEY")

cliente = anthropic.Anthropic()

herramienta = [
    {
        "name": "consultar_temperatura",
        "description": "Devulva la temperatura de una ciudad",
        "input_schema": {
            "type": "object",
            "properties": {
                "ciudad": {"type": "string", "description": "nombre de ciudad"}
            },
            "required": ["ciudad"]
        }
    }
]

historial = [
    {"role": "user", "content": "¿Que temperatura hace en Sevilla?"}
]

respuesta = cliente.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    tools=herramienta,
    messages=historial
)

bloque_herramienta = respuesta.content[1]
ciudad_pedida = respuesta.content[1].input['ciudad']

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad_pedida}&appid={clave}&units=metric"
respuesta_temp = requests.get(url)
datos_temp = respuesta_temp.json()
temp = datos_temp['main']['temp']

historial.append({"role": "assistant", "content": respuesta.content})
historial.append({
    "role": "user",
    "content": [
        {
            "type": "tool_result",
            "tool_use_id": bloque_herramienta.id,
            "content": str(temp)
        }
    ]
})

respuesta1 = cliente.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    tools=herramienta,
    messages=historial
)

print(respuesta1.content[0].text)
print(respuesta1.stop_reason)