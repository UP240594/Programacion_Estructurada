import java.util.Arrays;

class bup240594arreglos_y_matrices{
    public static void main(String[] args){
        String[] nombres = {"Ana","Luis","Carlos","Marta"};
        String[] materias= {"Matematicas", "Fisica" , "Quimica" , "Biologia"};
        double[][] calificaiones = {
            {10,9,8,7},
            {9,7,6,8},
            {8,9,5,9},
            {7,8,9,10}
        };


        for (int i = 0; i < calificaiones.length; i++){
            System.out.print(Arrays.toString(calificaiones[i]));
            if(i < calificaiones.length){
                System.out.println(", \n");
            }
        } 
    }
}