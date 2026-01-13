package mat;

public class Fn{
   public static void imprimirMatriz(int[][] m) {
      for (int i = 0; i < m.length; i++) {
        for (int j = 0; j < m[0].length; j++) { //Columnas puedo cambiarle  a cero
          System.out.print(m[i][j] + "\t");
        }
        System.out.println();
      }
    }

     public static int[][] transpuesta(int[][] m) {
      int f = m.length;
      int c = m[0].length;
      int[][] t = new int[c][f];

      for (int i = 0; i < f; i++) {
        for (int j = 0; j < c; j++) {
          t[j][i] = m[i][j];
        }
      }
    
      return t;
    }
}

