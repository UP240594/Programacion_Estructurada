import random
import time
import heapq

def heap_sort(arr):
    h = []
    for value in arr:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]

# Configuración
N, SEMILLA = 20000, 50
random.seed(SEMILLA)
datos = [random.randint(1, 100000) for _ in range(N)]

print(f"--- PRUEBA HEAP SORT ---")
print(f"Primeros 10 datos (Desordenados): {datos[:10]}")
print("Ordenando 20,000 datos...")

inicio = time.perf_counter()
resultado = heap_sort(datos)
fin = time.perf_counter()

print(f"Primeros 10 datos (Ordenados): {resultado[:10]}")
print(f"Tiempo total: {fin - inicio:.6f} segundos\n")