class arreglos_y_matrices{
    public static void main(String[] args){
         String[] nombres = { "Ana", "Luis", "Carlos", "Marta" };
        String[] materias = { "Matemáticas", "Física", "Química", "Biología" };
        double[][] calificaciones = {
                { 10, 9, 8, 7 },
                { 9, 7, 6, 8 },
                { 8, 9, 5, 9 },
                { 7, 8, 9, 10 }
        };
        int F = calificaciones.length; //Longitud de calificaciones
        int C = calificaciones[0].length; //Longitud de columnas empezando con cero ya que lo toma desde el inicio, es de ley por asi decirlo

        double avgAlumnos[] = new double[F];  //Aqui se crea el nuevo objeto
        double avgMaterias[] = new double[C]; // Tambien aqui se crea el nuevo objeto para exista
        double total = 0;

        //Calcular promedios
      
        for(int i = 0 ; i < F; i++){  //Filas
            double sumaAlumno=0;
            for(int j = 0; j < C ; j++){ //Columnas
                sumaAlumno += calificaciones[i][j];
                avgMaterias[j] += calificaciones[i][j]; //Aqui se suma
                //dividir el 4
            }
            avgAlumnos[i] = sumaAlumno / C;
        }


    }
}