import anthropic        

cliente = anthropic.Anthropic()

respuesta = cliente.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hola Claude, esta es mi primera llamada a tu API desde Python."}
    ]
)

print(respuesta.content[0].text)