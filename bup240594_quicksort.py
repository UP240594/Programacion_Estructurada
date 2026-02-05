#Cuales son los tres metodos de ordenacion que estan en la competencia, Investigarlo. Se entrega viernes o sabado
#Probar codigo con 20,000 datos en el rango de [11 a 99]
#semilla (50)


#Leer el sort de seleccion, bubble sort 
#Quicksort
import random
import time
import sys

sys.setrecursionlimit(30000)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Configuración
N, SEMILLA = 20000, 50
random.seed(SEMILLA)
datos = [random.randint(1, 100000) for _ in range(N)]

print(f"--- PRUEBA QUICKSORT ---")
print(f"Primeros 10 datos (Desordenados): {datos[:10]}")
print("Ordenando 20,000 datos...")

inicio = time.perf_counter()
resultado = quicksort(datos)
fin = time.perf_counter()

print(f"Primeros 10 datos (Ordenados): {resultado[:10]}")
print(f"Tiempo total: {fin - inicio:.6f} segundos\n")