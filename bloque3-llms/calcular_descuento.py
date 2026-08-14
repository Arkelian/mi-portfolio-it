def introduccion(precio, descuento):
    rebaja = precio * descuento / 100
    total = precio - rebaja
    return total

precio_usuario = float(input("Introduce el precio: "))
resultado = introduccion(precio_usuario, 20)
