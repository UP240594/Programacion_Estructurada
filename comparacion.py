import random
import time
import sys

# 1. Aumentamos el límite de recursión para QuickSort
sys.setrecursionlimit(50000)

# --- MÉTODO 1: QUICKSORT ---
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)
    return array

# --- MÉTODO 2: COUNTING SORT ---
def countingSort(arr):
    if not arr: return arr
    max_val = max(arr)
    min_val = min(arr)
    count = [0] * (max_val - min_val + 1)
    for num in arr:
        count[num - min_val] += 1
    output = []
    for i, freq in enumerate(count):
        output.extend([i + min_val] * freq)
    return output

# --- MÉTODO 3: RADIX SORT ---
def radixSort(arr):
    if not arr: return arr
    maxVal = max(arr)
    exp = 1
    while maxVal // exp > 0:
        buckets = [[] for _ in range(10)]
        for val in arr:
            index = (val // exp) % 10
            buckets[index].append(val)
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        exp *= 10
    return arr

# --- CONFIGURACIÓN DE LA PRUEBA ---
N = 100000
SEMILLA = 50
MIN_R, MAX_R = 15, 35  # Ajustado al rango solicitado de la tarea

random.seed(SEMILLA)
datos_originales = [random.randint(MIN_R, MAX_R) for _ in range(N)]

print(f"--- COMPARATIVA FINAL: N={N}, Rango=[{MIN_R}-{MAX_R}] ---")

# Prueba QuickSort
dq = datos_originales.copy()
i = time.perf_counter()
quicksort(dq)
f = time.perf_counter()
t_q = f - i
print(f"1. QuickSort:    {t_q:.6f} s")

# Prueba CountingSort
dc = datos_originales.copy()
i = time.perf_counter()
countingSort(dc)
f = time.perf_counter()
t_c = f - i
print(f"2. CountingSort: {t_c:.6f} s")

# Prueba RadixSort
dr = datos_originales.copy()
i = time.perf_counter()
radixSort(dr)
f = time.perf_counter()
t_r = f - i
print(f"3. RadixSort:    {t_r:.6f} s")

print("-" * 45)