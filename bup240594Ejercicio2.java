public class bup240594Ejercicio2 {
    public static void main(String[] args) {
        String[] tamanos = { "", "Chico", "Mediano", "Grande" };
        String[] modelos = { "", "A", "B" };
        String[] lugares = { "taller", "administracion" };
        int[][] unidades = { { 400, 200, 50 }, { 300, 100, 30 } };
        double[][] horas_taller_administracion = { { 25, 30, 33 }, { 1.0, 1.2, 1.3 } };

        int filasA = unidades.length;
        int columnasA = unidades[0].length;

        int filasB = horas_taller_administracion.length;
        int columnasB = horas_taller_administracion[0].length;

        // Matriz A modelos y tamaños con sus respectivas unidades
        System.out.println("Matriz A");
        // Encabezado de la matriz

        for (int j = 0; j < tamanos.length; j++) {
            System.out.printf("%-10s", tamanos[j]);
        }
        System.out.println();

        // Mostrar unidades
        for (int i = 0; i < filasA; i++) { // Filas
            System.out.printf("%-10s", modelos[i]);
            for (int j = 0; j < columnasA; j++) { // Columnas
                System.out.printf("%-10d", unidades[i][j]);
            }
            System.out.println();
        }

        System.out.println("______________________________________________________________________");

        // Matriz B

        System.out.println("Matriz B");

        // Encabezado de la matriz

        for (int j = 0; j < tamanos.length; j++) {
            System.out.printf("%-17s", tamanos[j]);
        }
        System.out.println();

        // Mostrar unidades
        for (int i = 0; i < filasB; i++) { // Filas
            System.out.printf("%-17s", lugares[i]);
            for (int j = 0; j < columnasB; j++) { // Columnas
                System.out.printf("%-17.1f", horas_taller_administracion[i][j]);
            }
            System.out.println();
        }

        System.out.println("______________________________________________________________________");

        // Sacar matriz C
        System.out.println("Matriz de Horas de talleres y administracion, segun el modelo");
        // Primero cambiamos la matriz B a una transpuesta para que se pueda multiplicar

        // transpuesta maual
        double[][] t = new double[columnasB][filasB];
        for (int i = 0; i < filasB; i++) {
            for (int j = 0; j < columnasB; j++) {
                t[j][i] = horas_taller_administracion[i][j];
            }
        }
        double[][] C = new double[filasA][filasB];

        // Multiplicacion de matrices

        for (int i = 0; i < filasA; i++) {
            for (int j = 0; j < filasB; j++) {
                for (int k = 0; k < columnasA; k++) {
                    C[i][j] += unidades[i][k] * t[k][j];
                }
            }
        }
        // Imprimir matrices C
        // Encabezado
        for (int j = 0; j < modelos.length; j++) {
            System.out.printf("%-15s", modelos[j]);
        }
        System.out.println();
        // unidades
        for (int i = 0; i < filasA; i++) {
            System.out.printf("%-15s", lugares[i]);
            for (int j = 0; j < filasB; j++) {
                System.out.printf("%-15.2f", C[i][j]);

            }
            System.out.println();
        }
    }
}
