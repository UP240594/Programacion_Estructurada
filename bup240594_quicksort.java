import java.util.*;

public class bup240594_quicksort {
    public static void main(String[] args) {
        int n = 20000;
        long semilla = 50;
        Random rd = new Random(semilla);
        int[] datos = new int[n];
        for (int i = 0; i < n; i++) datos[i] = rd.nextInt(100000);

        System.out.println("--- PRUEBA QUICKSORT ---");
        System.out.println("Muestra desordenada: " + Arrays.toString(Arrays.copyOfRange(datos, 0, 10)));

        long inicio = System.nanoTime();
        quicksort(datos, 0, n - 1);
        long fin = System.nanoTime();

        System.out.println("Muestra ordenada: " + Arrays.toString(Arrays.copyOfRange(datos, 0, 10)));
        System.out.printf("Tiempo total: %.6f segundos\n", (fin - inicio) / 1e9);
    }

    public static void quicksort(int[] arr, int low, int high) {
        if (low < high) {
            int p = partition(arr, low, high);
            quicksort(arr, low, p - 1);
            quicksort(arr, p + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
            }
        }
        int temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;
        return i + 1;
    }
}
