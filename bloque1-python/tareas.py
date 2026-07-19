# Gestor de tareas
import datetime
import json

def completar_tarea(tareas, indice):
    if indice < len(tareas):
        if tareas[indice]["completada"] == True:
            print("Tarea ya estaba completada.")
        else:
            tareas[indice]["completada"] = True
            print("Tarea completada.")
    else:
        print("Tarea no encontrada")

def eliminar_tarea(tareas, indice):
    if indice < len(tareas):
        del tareas[indice]
        print("Tarea eliminada.")
    else:
        print("Tarea no encontrada.")

def tareas_pendientes(tareas):
    encontradas = False
    for indice, tarea in enumerate(tareas):
        if tarea["completada"] == False:
            print(f"{indice + 1}. {tarea['descripcion']} | {tarea['fecha']} | Pendiente")
            encontradas = True
    if encontradas == False:
        print("No hay tareas pendientes.")

def guardar_tarea(tareas):
    with open("tareas.json", "w") as f:
        json.dump(tareas, f)
            
def cargar_tarea():
    try:
        with open("tareas.json", "r") as f:
            tareas = json.load(f)
        return tareas
    except FileNotFoundError:
        return [] 
    
def tareas_formateadas(tareas):
    if not tareas:
        print("Lista esta vacia.")
    else:
        for indice, tarea in enumerate(tareas):
            if tarea["completada"]:
                estado = "Completada"
            else:
                estado = "Pendiente"
            print(f"\n{indice + 1}. {tarea['descripcion']} | {tarea['fecha']} | {estado}")

def main():
    tareas = cargar_tarea()

    print()
    print("=== Lista de tareas ===")
    print("\n Para cerrar la lista escribe 'Salir'")
    print()
    
    while True:
        control = input("Elige una de las siquentes opciones: 'Añadir tarea', 'Completar tarea', 'Ver pendientes', 'Ver tareas' 'Eliminar tarea', 'Salir': ")

        if control.capitalize() == "Salir":
            break

        elif control.capitalize() == "Añadir tarea":
            descripcion = input("Escribe la descripcion de la tarea: ")
            fecha = datetime.datetime.now().strftime("%d/%m/%Y")
            tarea_nueva = {
                "descripcion": descripcion,
                "fecha": fecha,
                "completada": False
            }
            tareas.append(tarea_nueva)
            guardar_tarea(tareas)

        elif control.capitalize() == "Completar tarea":
            completar = int(input("Introduzca el numero de la tarea que desea completar: "))
            completar_tarea(tareas, completar - 1)
            guardar_tarea(tareas)

        elif control.capitalize() == "Ver pendientes":
            tareas_pendientes(tareas)

        elif control.capitalize() == "Ver tareas":
            tareas_formateadas(tareas)

        elif control.capitalize() == "Eliminar tarea":
            eliminar = int(input("Introduzca el numero de la tarea que desea eliminar: "))
            eliminar_tarea(tareas, eliminar - 1)
            guardar_tarea(tareas)

        else:
            print("Opcion no valida.")


main()



            


