
class maximo {

    public static void main(String[] args) {
        int[] e = {4, 1, 5, 3, 2};

        int minimo = e[0];
        int maximo = e[0];

        for (int i = 1; i < e.length; i++) {

            if (e[i] < minimo) {
                minimo = e[i];
            }
             //Sacar maximo
            if (e[i] > maximo) {
                maximo = e[i];
            }
        }

       
       

        System.out.println("el minimo es: " + minimo);
        System.out.println("el maximo es: " + maximo);

    }
}
