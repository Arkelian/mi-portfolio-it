import anthropic

cliente = anthropic.Anthropic()

historial = [
    {"role": "user", "content": "¿Que plato de comida me recomiendas?"}
]

respuesta1 = cliente.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=historial
)

print(respuesta1.content[0].text)

historial.append({"role": "assistant", "content": respuesta1.content[0].text})
historial.append({"role": "user", "content": "¿Que ingredientes lleva?"})

respuesta2 = cliente.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=historial
)

print(respuesta2.stop_reason)

print(respuesta2.content[0].text)