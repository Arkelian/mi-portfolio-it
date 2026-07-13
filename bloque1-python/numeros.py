# Programa para aprender a usar funciones y estructuras de control en Python

def recoger_numeros():
    """Pide al usuario que ingrese numeros hasta que ingrese 'fin' """
    numeros = []
    while True:
        entrada = input("Ingrese un numero (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        numeros.append(int(entrada))
    return numeros

def analizar_numeros(numeros):
    """Analiza la lista de numeros y devuelve el promedio, el maximo, el minimo y la suma de los numeros"""
    if not numeros:
        return {
            'maximo': None,
            'minimo': None,
            'suma': 0,
            'media': None
        }
    maximo = max(numeros)
    minimo = min(numeros)
    suma = sum(numeros)
    media = sum(numeros) / len(numeros)
    return {
        'maximo': maximo,
        'minimo': minimo,
        'suma': suma,
        'media': media
    }

def imprimir_informe(numeros, resultados):
    """imprimir un informe con los resultados del analisis de los numeros"""
    if not numeros:
        print("No se ingresaron numeros")
        return
    
    print("Informe de análisis de números:")
    print(f"Lista de números: {numeros}")
    print(f"Suma: {resultados['suma']}")
    print(f"Promedio: {resultados['media']}")
    print(f"Máximo: {resultados['maximo']}")
    print(f"Mínimo: {resultados['minimo']}")

def main():
    numeros = recoger_numeros()
    resultados = analizar_numeros(numeros)
    imprimir_informe(numeros, resultados)

main()