nombre = input("¿Como te llamas? ")
edad = int(input("¿Cuantos años tienes? "))
calculo = 2026 - edad + 100
if edad >= 18 and edad < 100:
    print(f"Eres mayor de edad y vas a cumplir 100 años en el {calculo}")
elif edad < 18:
    print (f"Eres menor de edad y vas a cumplir 100 años en el {calculo}")
else:
    print(f"Felicidades {nombre}!")
