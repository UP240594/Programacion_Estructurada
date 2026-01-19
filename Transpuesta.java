
import static mat.Fn.*;

public class Transpuesta {
  public static void main(String[] args) {
    int[][] a = { { 1, 2, 3, 4 },
        { 5, 6, 7, 8 },
        { 9, 10, 11, 12 } };
    int f = a.length;
    int c = a[0].length;

    /*
     * transpuesta maual
     * int[][] t = new int[c][f];
     * for (int i = 0; i < f; i++) {
     * for (int j = 0; j < c; j++) {
     * t[j][i] = a[i][j];
     * }
     * }
     * 
     */
    int[][] trans = transponerMatriz(a);

    System.out.println("Matriz original");
    imprimirMatriz(a);
    System.out.println("\nMatriz transpuesta");
    imprimirMatriz(trans);
    System.out.println(". . . Hecho");

  }

}
