# Visualización de Algoritmos de Ordenamiento

Este repositorio cuenta con tres archivos .py donde se representa visualmente utilizando terminal algunos de los algoritmos de ordenamiento existentes

## Algoritmos incluidos

Actualmente el repositorio contiene tres implementaciones:

### Merge Sort

Implementación del algoritmo **Merge Sort**, utilizando recursividad para dividir la lista en partes más pequeñas y posteriormente unirlas de forma ordenada.

La visualización muestra los cambios de los elementos mientras se realiza el proceso de ordenamiento.

Archivo:

```text
AlgoritmoOrdenamientoMergeSort.py
```

### Bubble Sort

Implementación del algoritmo **Bubble Sort**.

El programa compara elementos consecutivos y los intercambia cuando se encuentran en un orden incorrecto. Durante el proceso se muestran visualmente las columnas que están siendo comparadas y las que ya fueron ordenadas.

Archivo:

```text
AlgoritmoOrdenamientoBurbuja.py
```

### Quick Sort

Implementación del algoritmo **Quick Sort**, utilizando un pivote para dividir la lista y ordenar sus elementos mediante recursividad.

La visualización permite observar el pivote y los elementos que se están comparando durante el proceso.

Archivo:

```text
AlgoritmoOrdenamientoQuickSort.py
```

## Tecnologías utilizadas

* **Python 3**
* `sys` para controlar la salida de la terminal.
* `random` para generar listas aleatorias.
* `time` para controlar la velocidad de las animaciones.
* Códigos **ANSI** para posicionar elementos en la terminal.
* Caracteres ASCII para representar las columnas.

## Representación visual

Los valores de las listas se representan mediante columnas.

Durante la ejecución se utilizan diferentes caracteres para identificar los elementos que están siendo procesados:

```text
█  Columna normal / elemento ordenado
▓  Elemento seleccionado o pivote
▒  Elemento en comparación
```

La representación puede variar ligeramente entre los diferentes algoritmos.

## 🧠 Algoritmos

| Algoritmo   | Método principal          | Complejidad promedio |
| ----------- | ------------------------- | -------------------- |
| Merge Sort  | Divide y combina          | O(n log n)           |
| Bubble Sort | Comparación e intercambio | O(n²)                |
| Quick Sort  | Pivote y particiones      | O(n log n)           |

**Julio César Ju Salido**
