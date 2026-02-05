import java.util.*;

public class bup240594_mergesort {
    public static void main(String[] args) {
        int n = 20000;
        long semilla = 50;
        Random rd = new Random(semilla);
        int[] datos = new int[n];
        for (int i = 0; i < n; i++) datos[i] = rd.nextInt(100000);

        System.out.println("--- PRUEBA MERGE SORT ---");
        System.out.println("Muestra desordenada: " + Arrays.toString(Arrays.copyOfRange(datos, 0, 10)));

        long inicio = System.nanoTime();
        mergeSort(datos, 0, n - 1);
        long fin = System.nanoTime();

        System.out.println("Muestra ordenada: " + Arrays.toString(Arrays.copyOfRange(datos, 0, 10)));
        System.out.printf("Tiempo total: %.6f segundos\n", (fin - inicio) / 1e9);
    }

    public static void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    private static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1; int n2 = r - m;
        int L[] = new int[n1]; int R[] = new int[n2];
        for (int i = 0; i < n1; ++i) L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j) R[j] = arr[m + 1 + j];
        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) { arr[k] = L[i]; i++; }
            else { arr[k] = R[j]; j++; }
            k++;
        }
        while (i < n1) { arr[k] = L[i]; i++; k++; }
        while (j < n2) { arr[k] = R[j]; j++; k++; }
    }
}