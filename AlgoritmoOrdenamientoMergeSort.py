
import sys
import random
import time

def mover_cursor(fila, columna):
    sys.stdout.write(f"\033[{fila};{columna}H")
    sys.stdout.flush()

def limpiar_pantalla():
    print("\033[2J\033[H", end="")

datos = list(range(1, 71))
random.shuffle(datos)

def dibujar(lista, select):
    limpiar_pantalla()

    if select is None:
        select = []

    altura = max(lista)

    for y in range(altura, 0, -1):
        mover_cursor(altura - y + 1, 1)

        for z in range(len(lista)):
            valor = lista[z]

            if z in select:
                if z == select[0]:
                    ascii = "▒"
                else:
                    ascii = "▓"
            else:
                ascii = "█"

            if valor >= y:
                print(" " + ascii, end="")
            else:
                print("  ", end="")
        print()

    mover_cursor(altura + 1, 1)
    print(" ", end="")

    for i in range(len(lista)):
        print(f"{lista[i]:2}", end="")

def merge(lista, izquierda, medio, derecha):
    L = lista[izquierda:medio + 1]
    R = lista[medio + 1:derecha + 1]

    i = 0
    j = 0
    k = izquierda

    while i < len(L) and j < len(R):
        dibujar(lista, [k])
        time.sleep(0.1)

        if L[i] <= R[j]:
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1

        dibujar(lista, [k])
        time.sleep(0.2)
        k += 1

    while i < len(L):
        dibujar(lista, [k])
        time.sleep(0.1)

        lista[k] = L[i]
        i += 1

        dibujar(lista, [k])
        time.sleep(0.2)
        k += 1

    while j < len(R):
        dibujar(lista, [k])
        time.sleep(0.1)

        lista[k] = R[j]
        j += 1

        dibujar(lista, [k])
        time.sleep(0.2)
        k += 1

def merge_sort(lista, izquierda, derecha):
    if izquierda < derecha:
        medio = (izquierda + derecha) // 2
        merge_sort(lista, izquierda, medio)
        merge_sort(lista, medio + 1, derecha)
        merge(lista, izquierda, medio, derecha)

def visual(lista):
    dibujar(lista, None)
    merge_sort(lista, 0, len(lista) - 1)
    dibujar(lista, None)

if __name__ == "__main__":
    visual(datos)