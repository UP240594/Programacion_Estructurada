import java.util.*;

public class bup240594_heap_sort{
    public static void main(String[] args) {
        int n = 20000;
        long semilla = 50;
        Random rd = new Random(semilla);
        int[] datos = new int[n];
        for (int i = 0; i < n; i++) datos[i] = rd.nextInt(100000);

        System.out.println("--- PRUEBA HEAP SORT ---");
        System.out.println("Muestra desordenada: " + Arrays.toString(Arrays.copyOfRange(datos, 0, 10)));

        long inicio = System.nanoTime();
        heapSort(datos);
        long fin = System.nanoTime();

        System.out.println("Muestra ordenada: " + Arrays.toString(Arrays.copyOfRange(datos, 0, 10)));
        System.out.printf("Tiempo total: %.6f segundos\n", (fin - inicio) / 1e9);
    }

    public static void heapSort(int[] arr) {
        int n = arr.length;
        for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);
        for (int i = n - 1; i > 0; i--) {
            int temp = arr[0]; arr[0] = arr[i]; arr[i] = temp;
            heapify(arr, i, 0);
        }
    }

    private static void heapify(int[] arr, int n, int i) {
        int largest = i; int l = 2 * i + 1; int r = 2 * i + 2;
        if (l < n && arr[l] > arr[largest]) largest = l;
        if (r < n && arr[r] > arr[largest]) largest = r;
        if (largest != i) {
            int swap = arr[i]; arr[i] = arr[largest]; arr[largest] = swap;
            heapify(arr, n, largest);
        }
    }
}