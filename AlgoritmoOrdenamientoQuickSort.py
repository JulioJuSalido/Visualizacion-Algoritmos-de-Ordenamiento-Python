import sys
import time
import random

print("\033[2J\033[H", end="")

lista = list(range(1,71))
random.shuffle(lista)

def borrar_columna(x):
    equis = (x * 4) + 2

    for y in range(73, 0, -1):
        sys.stdout.write(f"\033[{y};{equis}H ")
    sys.stdout.write(f"\033[{75};{equis}H  ")
    sys.stdout.flush()


def imprimir_columna(x, valor, simbolo):
    borrar_columna(x)

    equis = (x * 4) + 2
    sys.stdout.write(f"\033[{75};{equis}H{valor}")

    basey = 73
    for i in range(valor):
        sys.stdout.write(f"\033[{basey};{equis}H{simbolo}")
        basey -= 1
    sys.stdout.flush()


def imprimirlista(lista):
    for i in range(len(lista)):
        imprimir_columna(i, lista[i], "█")


def quicksort(lista, inicio, fin):
    if inicio >= fin:
        return

    pivote = lista[fin]
    i = inicio - 1

    for j in range(inicio, fin):

        imprimir_columna(j, lista[j], "▒")
        imprimir_columna(fin, lista[fin], "▓")

        time.sleep(0.1)

        if lista[j] < pivote:

            i += 1
            lista[i], lista[j] = lista[j], lista[i]

            imprimir_columna(i, lista[i], "█")
            imprimir_columna(j, lista[j], "█")

            time.sleep(0.2)
        imprimir_columna(j, lista[j], "█")
        imprimir_columna(fin, lista[fin], "█")

    lista[i+1], lista[fin] = lista[fin], lista[i+1]

    imprimir_columna(i+1, lista[i+1], "█")
    imprimir_columna(fin, lista[fin], "█")
    time.sleep(0.2)

    pivote = i + 1

    quicksort(lista, inicio, pivote- 1)
    quicksort(lista, pivote + 1, fin)

imprimirlista(lista)
quicksort(lista, 0, len(lista)-1)
sys.stdout.write("\033[80;0H")