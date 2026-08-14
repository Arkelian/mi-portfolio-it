import json


def almacen(productos):
    if productos["stock"] > 0:
        return f"Producto {productos['nombre']} disponible y su precio {productos['precio']} euros"
    else:
        return "Producto " + productos["nombre"] + " agotado."

disponibilidad = [
    {"nombre": "Manzanas", "precio": 4, "stock": 2},
    {"nombre": "Narangas", "precio": 2, "stock": 5},
    {"nombre": "Tomates", "precio": 4, "stock": 0}
    ]

try:
    with open("resultado.json", "r") as f:
        productos_leidos = json.load(f)
except FileNotFoundError:
    productos_leidos = []

with open("resultado.json", "w") as f:
    json.dump(disponibilidad, f)

for p in productos_leidos:
    mensaje = almacen(p)
    print(mensaje)


