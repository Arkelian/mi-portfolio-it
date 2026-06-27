# perfiles_v2.py
# Bloque 1, Sesion 3 - Funciones
# Version mejorada de perfiles_multiples.py


# ---- Funciones ----

def calcular_nivel(meses):
    """Devuelve el nivel de formacion segun los meses estudiados"""
    if meses < 3:
        return "Principiante"
    elif meses < 12:
        return "En formacion"
    else:
        return "Intermedio"
    

def pedir_perfil(nombre):
    """Pide datos de una persona y devuelve un diccionario con su perfil."""
    edad     = int(input("Edad: "))
    lenguaje = input("Lenguaje que esta aprendiendo: ")
    meses    = int(input("Meses de formacion: "))
    nivel    = calcular_nivel(meses)

    return {
        "nombre":   nombre,
        "edad":     edad,
        "lenguaje": lenguaje,
        "meses":    meses,
        "nivel":    nivel
    }

def imprimir_perfil(indice, perfil):
    """Imprime los datos de un perfil formateado."""
    print(f"\n{indice}. {perfil['nombre']}")
    print(f"   Edad     : {perfil['edad']} años")
    print(f"   Lenguaje : {perfil['lenguaje']}")
    print(f"   Nivel    : {perfil['nivel']} ({perfil['meses']} meses)")

def contar_por_nivel(perfiles):
    """Devuelve cuantos perfiles hay en cada nivel."""
    niveles = [p["nivel"] for p in perfiles]
    return {
        "Principiante": niveles.count("Principiante"),
        "En formacion": niveles.count("En formacion"),
        "Intermedio": niveles.count("Intermedio")
    }

def imprimir_informe(perfiles):
    """Imprime un informe completo de todos los perfiles."""
    print()
    print("=" * 45)
    print(f"      INFORME FINAL - {len(perfiles)} PERFILES")
    print("=" * 45)

    for indice, perfil in enumerate(perfiles):
        imprimir_perfil(indice + 1, perfil)

    print()
    print("=" * 45)

    conteo = contar_por_nivel(perfiles)
    print(f"Principiante : {conteo['Principiante']}")
    print(f"En formacion : {conteo['En formacion']}")
    print(f"Intermedio   : {conteo['Intermedio']}")

# --- PROGRAMA PRINCIPAL ---

def main():
    perfiles = []

    print("=== GENERADOR DE PERFILES IT ===")
    print("Escribe 'fin' en el nombre para terminar.")
    print()

    while True:
        control = input("Nombre (o 'fin' para terminar):")

        if control.lower() == "fin":
            break

        perfil = pedir_perfil(control)
        perfiles.append(perfil)
        print(f"-> Perfil de {perfil['nombre']} guardado.\n")

    if len(perfiles) == 0:
        print("No se introdujo ningun perfil")
    else:
        imprimir_informe(perfiles)


main()