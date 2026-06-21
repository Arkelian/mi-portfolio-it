# Perfiles_multiples.py
# Bloque 1, Sesion 2 - Listas y bucles

perfiles = [] # lista vacia que ira guardando cada perfil (diccionario)

print("=== GENERADOR DE PERFILES IT ===")
print("Vas a introducir datos de varias personas. Escribe 'fin' en el nombre para terminar.")
print()

while True:
    nombre = input("Nombre (o 'fin' para terminar): ")

    if nombre.lower() == "fin":
        break

    edad = int(input("Edad: "))
    lenguaje = input("Lenguaje que esta aprendieno: ")
    meses = int(input("Meses de formacion: "))

    # Determinar nivel
    if meses < 3:
        nivel = "Principiante"
    elif meses < 12: 
        nivel = "En formacion"
    else:
        nivel = "Intermedio"

    # Guardar como diccionario dentro de la lista
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "lenguaje": lenguaje,
        "meses": meses,
        "nivel": nivel
    }
    perfiles.append(perfil)
    print(f"-> Perfil de {nombre} guardado.\n")

# --- INFORME FINAL ---
print()
print("=" * 40)
print(f"      INFORME FINAL - {len(perfiles)} PERFILES")
print("=" * 40)

for indice, p in enumerate(perfiles):
    print(f"\n{indice + 1}. {p['nombre']}")
    print(f"   Edad     : {p['edad']} años")
    print(f"   Lenguaje : {p['lenguaje']}")
    print(f"   Nivel    : {p['nivel']} ({p['meses']} meses)")

print()
print("=" * 40)

#Bonus: contar cuantos hay en cada nivel
niveles = [p["nivel"] for p in perfiles]
print(f"Principiantes: {niveles.count('Principiante')}")
print(f"En formacion : {niveles.count('En formacion')}")
print(f"Intermedios  : {niveles.count('Intermedio')}")