# perfil.py
# Script de presentacion personal - Bloque 1, Sesion 1 

# ---RECOGER INFORMACION DEL USUARIO---
print("=== GENERADOR DE PERFIL IT ===")
print()

nombre   = input("¿Cual es tu nombre? ")
edad     = int(input("¿Cuantos años tienes? "))
ciudad   = input("¿En que ciudad vives? ")
lenguaje = input("¿Que lenguaje de programacion estas aprendiendo? ")
meses    = int(input("¿Cuantos meses llevas estudiando IT? "))

# --- PROCESAMIENTO ---
experiencia_horas = meses * 8    # estimacion de 8 horas de estudio por mes
nivel = ""

if meses < 3:
    nivel = "Principiante"
elif meses < 12:
    nivel = "En formacion"
else:
    nivel = "Intermedio"

# --- MOSTRAR EL PERFIL ---
print()
print("=" * 40)
print("          PERFIL IT PROFESIONAL")
print("=" * 40)
print(f"  Nombre     : {nombre}")
print(f"  Edad       : {edad} años")
print(f"  Ciudad     : {ciudad}")
print(f"  Lenguaje   : {lenguaje}")
print(f"  Nivel      : {nivel}")
print(f"  Formacion  : {meses} meses ({experiencia_horas} horas estimadas)")
print("=" * 40)
print()
print(f"¡Sigue adelante, {nombre}! El mercado IT te espera.")