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
N, SEMILLA = 10000, 50
random.seed(SEMILLA)
datos = [random.randint(1, 100000) for _ in range(N)]

print(f"--- PRUEBA QUICKSORT ---")
print(f"Primeros 10 datos (Desordenados): {datos[:10]}")
print("Ordenando 10,000 datos...")

inicio = time.perf_counter()
resultado = quicksort(datos)
fin = time.perf_counter()

print(f"Primeros 10 datos (Ordenados): {resultado[:10]}")
print(f"Tiempo total: {fin - inicio:.6f} segundos\n")

print("---------------------------------------------")



minimo = 15
maximo = 35

def countingSort(arr):
    if not arr:
        return arr
        
    max_val = max(arr)
    count = [0] * (maximo - minimo + 1)

    for num in arr:
        count[num] += 1
        
    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num] * freq)

    return arr


n = 10000

# Aquí es donde defines el rango de 15 a 35
datos2 = [random.randint(15, 35) for _ in range(n)]



print(f"--- PRUEBA CountingSort ---")
print(f"Primeros 10 datos (Desordenados): {datos2[:10]}")
print("Ordenando 10,000 datos...")


inicio2 = time.perf_counter()
fin2 = time.perf_counter()

resultadoCounting = countingSort(datos2)
print(f"Primeros 10 datos (Ordenados): {resultadoCounting[:10]}")
print(f"Tiempo total: {fin2 - inicio2:.6f} segundos\n")
