# Revisa el duplicado y añade el contacto.
def añadir_contacto(agenda, nombre, telefono):
    """Revisa si el contacta ya existe en la agenda"""
    if nombre in agenda:
        print("Contacto ya existe en la agenda.")
    else:
        agenda[nombre] = telefono
        print("Contacto añadido")

# Busca el contacto en la agenda.
def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else: 
        print(f"Contacto {nombre} no encontrado.")

# Elimina el contacta de la agenda.
def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} ha sido eliminado.")
    else:
        print("Contacto no encontrado.")

# Muestra todos los contactos de la agenda.
def informe_agenda(agenda):
    print()
    print("=" * 45)
    print(" Informe de agenda ")
    print("=" * 45)
    
    if not agenda:
        print("Agenda esta vacia.")
    else:
        for nombre, telefono in agenda.items():
            print(f"\n Contactos: {nombre} - {telefono}")

# Programa principal.
def main():
    agenda = {}

    print("=== Agenda de contactos ===")
    print("Escribe 'Salir' para cerrar la agenda.")
    print()

    while True:
        control = input("Eliga una opcion que desea hacer: 'Añadir contacto', 'Buscar contacto', 'Eliminar contacto', 'Ver agenda' o 'Salir':")

        if control.capitalize() == "Salir":
            break
        elif control.capitalize() == "Añadir contacto":
            nombre = input("Introduzca el nombre del contacto: ").capitalize()
            telefono = input("Introduzca el telefono del contacto: ")
            añadir_contacto(agenda, nombre, telefono)
        elif control.capitalize() == "Buscar contacto":
            buscar = input("Introduzca el nombre del contacto que desee buscar: ").capitalize()
            buscar_contacto(agenda, buscar)
        elif control.capitalize() == "Eliminar contacto":
            borrar = input("Intruduzca el nombre del contacto que desea eliminar: ").capitalize()
            eliminar_contacto(agenda, borrar)
        elif control.capitalize() == "Ver agenda":
            informe_agenda(agenda)
        else:
            print("Opcion inexistente, repita de nuevo.")


main()
        

