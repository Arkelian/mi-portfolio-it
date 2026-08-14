import anthropic

cliente = anthropic.Anthropic()

respuesta = cliente.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=400,
    system="Eres un critico de cine principiante, analizas la pelicula con emociones propias.",
    messages=[
        {"role": "user", "content": "¿Que pelicula me recomiendas ver hoy?"}
    ]
)

print(respuesta.content[0].text)