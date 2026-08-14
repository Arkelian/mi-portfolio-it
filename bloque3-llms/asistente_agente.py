import anthropic
import os
import requests

clave = os.environ.get("OPENWEATHER_API_KEY")

cliente = anthropic.Anthropic()

herramientas = [
    {
        "name": "consultar_temperatura",
        "description": "Devuelve la temperatura actual de una ciudad.",
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
        "description": "Predice la edad segun un nombre.",
        "input_schema": {
            "type": "object",
            "properties": {
                "nombre": {"type": "string", "description": "nombre de persona"}
            },
            "required": ["nombre"]
        }
    }
]

historial = []

while True:
    control = input("Hazme una pregunta o escribe 'Fin' para terminar: ")

    if control.capitalize() == "Fin":
        break

    historial.append({"role": "user", "content": control})

    respuesta1= cliente.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        system="Eres un asistente serio, que intenta ayudar en lo que pueda al usuario",
        tools=herramientas,
        messages=historial
    )

    if respuesta1.stop_reason == "tool_use":
        print("Claude quiere usar una herramienta.")
        bloque_herramiente = respuesta1.content[1]

        if bloque_herramiente.name == "consultar_temperatura":
            ciudad_pedida = bloque_herramiente.input['ciudad']
            url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad_pedida}&appid={clave}&units=metric"
            respuesta_temp = requests.get(url)
            datos_temp = respuesta_temp.json()
            resultado = datos_temp['main']['temp']

        elif bloque_herramiente.name == "consultar_edad_estimada":
            nombre_pedido = bloque_herramiente.input['nombre']
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
                    "tool_use_id": bloque_herramiente.id,
                    "content": str(resultado)
                }
            ]
        }
    )

        respuesta2 = cliente.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=300,
            system="Eres un asistente serio, que intenta ayudar en lo que pueda al usuario",
            tools=herramientas,
            messages=historial
        )

        print(respuesta2.content[0].text)

    


    elif respuesta1.stop_reason == "end_turn":
        print("Claude a desidido responder sin usar las herramientas.")
        print(respuesta1.content[0].text)

    