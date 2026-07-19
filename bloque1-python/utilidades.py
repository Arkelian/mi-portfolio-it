# Script de prueba de os y datetime.
import os
import datetime

# 1. Imprime la carpeta actual.
print(os.getcwd())

# 2. Listar los archivos de esa carpeta.
print(os.listdir("."))

# 3. Comprobar si existe agenda.json
if os.path.exists("agenda.json"):
    print("Archivo existe")
else:
    print("Archivo no existe")

# 4. Imprimir fecha y hora actual formateada.
ahora = datetime.datetime.now()
print(ahora.strftime("%d/%m/%Y %H:%M"))