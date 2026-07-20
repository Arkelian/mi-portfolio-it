cuenta = int(input("Introduzca el importe total de la cuenta: "))
propina = int(input("Cuanto quieres dejar de propina, 10, 15 o 20%: "))
total = cuenta * propina / 100
total_a_pagar = cuenta + total
print(f"\nTienes que pagar en total {total_a_pagar} euros.")

frase = input("Introduzca una frase: ")
palabras = len(frase.split())
letras = len(frase.replace(" ", ""))
print(f"Tu frase '{frase}' tiene {palabras} palabras y {letras} letras.")

def introducir_nota():
    notas = []
    while True:
        nota = input("Introduzca tu nota o escribe 'fin' para terminar: ")
        if nota.lower() == "fin":
            break
        elif int(nota) >= 0 and int(nota) <= 11:
            notas.append(int(nota))
    return notas

def calculos(notas):
    minima = min(notas)
    maxima = max(notas)
    middle = sum(notas) / len(notas)
    return {
        'maxima': maxima,
        'minima': minima,
        'media': middle
    }

def informe(notas, resultados):
    if not notas:
        print("No se introdujo ninguna nota.")
        return
    print(f"Todas las notas {notas}")
    print(f"Nota maxima {resultados['maxima']}")
    print(f"Nota minima {resultados['minima']}")
    print(f"Nota media {resultados['media']}")

def main():
    notas = introducir_nota()
    resultados = calculos(notas)
    informe(notas, resultados)

main()






