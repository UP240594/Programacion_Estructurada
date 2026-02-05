class matriz_anidada{
    public static void main(String[] args){
        int[][] calificaciones = {
                { 10, 9, 8, 7 },
                { 9, 7, 6, 8 },
                { 8, 9, 5, 9 },
                { 7, 8, 9, 10 }
        };

        int f = calificaciones.length;
        int c = calificaciones[0].length;

        for(int i=0; i<f ; i++){
            System.out.println();
            System.out.print("Fila " + i + ": ");
            for(int j=0; j<c ; j++){
                if(i == j){
                    System.out.print(1);
                }
                System.out.print(0);
            }
        }
        
    }
} 