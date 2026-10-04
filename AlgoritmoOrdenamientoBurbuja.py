import sys
import random
import time

#Algoritmo de ordenamiento burbuja
#UTILIZAR ASCII 177 Y ASCII 178 PARA LAS COLUMNAS SELECCIONADAS
#UTILIZAR ASCII 219 PARA COLUMNAS YA REALIZADA

sys.stdout.write(f"\033[2J\033[H")
sys.stdout.flush()

def numeros_aleatorios():
    lista = []
    for x in range(15):
        x = random.randint(0,30)
        lista.append(x)
    return lista
lista = numeros_aleatorios()

#Esto es obsoleto profe
"""
def columna_inicial(lista):
    fila = 1
    for x in range(len(lista)):
        sys.stdout.write(f"\033[{33};{fila}H")
        print(lista[x])
        sys.stdout.flush()
        iniciocolumna = 31
        for i in range(int(lista[x])):
            sys.stdout.write(f"\033[{iniciocolumna};{fila}H")
            sys.stdout.write("█")
            sys.stdout.flush()
            iniciocolumna -= 1
        fila += 3
"""
def ordenamiento(lista, seleccionado1, seleccionado2, ordenado):
    fila = 1
    #borrar
    for x in range(15):
        iniciocolumna = 31
        for i in range(50):
            sys.stdout.write(f"\033[{iniciocolumna};{fila}H")
            print(" ", end="")
            iniciocolumna -= 1
        fila += 3
    fila = 1
    #imprimir
    for x in range(15):
        sys.stdout.write(f"\033[{33};{fila}H")
        print("  ", end = "")
        sys.stdout.flush()
        sys.stdout.write(f"\033[{33};{fila}H")
        print(lista[x], end = "")
        sys.stdout.flush()
        iniciocolumna = 31
        for i in range(int(lista[x])):
            sys.stdout.write(f"\033[{iniciocolumna};{fila}H")
            
            if ordenado[x] == True:
                cuadro = "█"
            elif seleccionado1[x] == True:
                cuadro = "▓"
            elif seleccionado2[x] == True:
                cuadro = "▒"
            else:
                cuadro = "█"
            
            print(cuadro, end="")
            sys.stdout.flush()
            iniciocolumna -= 1
        fila += 3
    
ordenado = [False]*15
for x in range(15): 
    for i in range(15 - x - 1):
        seleccionado1 = [False]*15
        seleccionado2 = [False]*15
        seleccionado1[i] = True
        seleccionado2[i + 1] = True
        
        ordenamiento(lista, seleccionado1, seleccionado2, ordenado)
        time.sleep(0.3)
        
        if lista[i] > lista[i + 1]:
            temp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = temp
            ordenamiento(lista, seleccionado1, seleccionado2, ordenado)
            time.sleep(0.3)
    ordenado[15 - x - 1] = True
seleccionado1 = [False]*15
seleccionado2 = [False]*15
ordenamiento(lista,seleccionado1,seleccionado2,ordenado)
#columna_inicial(lista)  
sys.stdout.write(f"\033[{35};{1}H")
sys.stdout.flush()