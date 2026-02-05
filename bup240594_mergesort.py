import random
import time

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

# Configuración
N, SEMILLA = 20000, 50
random.seed(SEMILLA)
datos = [random.randint(1, 100000) for _ in range(N)]

print(f"--- PRUEBA MERGE SORT ---")
print(f"Primeros 10 datos (Desordenados): {datos[:10]}")
print("Ordenando 20,000 datos...")

inicio = time.perf_counter()
resultado = merge_sort(datos)
fin = time.perf_counter()

print(f"Primeros 10 datos (Ordenados): {resultado[:10]}")
print(f"Tiempo total: {fin - inicio:.6f} segundos\n")