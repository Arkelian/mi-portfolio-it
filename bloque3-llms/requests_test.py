import requests
import anthropic
import os

clave = os.environ.get("OPENWEATHER_API_KEY")

url = f"https://api.openweathermap.org/data/2.5/weather?q=Huelva&appid={clave}&units=metric"
respuesta_temp = requests.get(url)
datos_temp = respuesta_temp.json()
temp = datos_temp['main']['temp']

client = anthropic.Anthropic()

respuesta = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=250,
    messages=[
        {"role": "user", "content": f"¿Que ropa me recomendarias poner hoy con {temp} grados?"}
        ]
)

print(respuesta.content[0].text)