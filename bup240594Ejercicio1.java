public class bup240594Ejercicio1 {
    public static void main(String[] args) {
        double[][] cantidades = { { 40, 160, 80 }, { 120, 120, 120 }, { 150, 80, 80 } };
        String[] canastas = { "A", "B", "C" };
        String[] quesos = { " ", "manchego", "roquefort", "camembert" };
        double[] factores = {50, 80, 100}; // cantidad de bandejas

        int F = cantidades.length;
        int C = cantidades[0].length;

        double[] sumaCanastaA = new double[F];
        double[] sumaQueso = new double[C];

        // Encabezado
        System.out.printf("%-10s", "");
        for (int j = 1; j < quesos.length; j++) {
            System.out.printf("%-12s", quesos[j]);
        }
        System.out.printf("%-12s%n", "Total(kg)");

        // Filas
        for (int i = 0; i < F; i++) {
            double sumaCan = 0;
            System.out.printf("%-10s", canastas[i]);
            for (int j = 0; j < C; j++) {
                System.out.printf("%-12.1f", cantidades[i][j]);
                sumaCan += cantidades[i][j] * factores[i]; // multiplicar por cantidad de bandejas
                sumaQueso[j] += cantidades[i][j] * factores[i]; // suma correcta por queso
            }
            sumaCanastaA[i] = sumaCan;
            double totalKg = sumaCan / 1000.0; // pasar a kg
            System.out.printf("%-12.2f%n", totalKg);
        }
        System.out.println("________________________________");

        // Totales por queso
        System.out.printf("%-10s", "Total(kg)");
        for (int j = 0; j < C; j++) {
            double totalKg = sumaQueso[j] / 1000.0;
            System.out.printf("%-12.2f", totalKg);
        }
    }
}
