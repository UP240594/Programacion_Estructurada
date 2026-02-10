
public class bup240594_recursividad {

    //Multiplicacion Decendente
    public int multiplicacionDecendente(int n) {
        if (n <= 1) {
            n = n * 1;
            System.out.println("5 *" + n + "=" + n);
        } else {
            multiplicacionDecendente(n - 1);
            System.out.println("5 *" + n + "=" + 5 * n);
        }
        return n;
    }
    //Multiplicacion Ascendente
    public int multiplicacionAscendente(int n) {
        if (n <= 1) {
            System.out.println("5 *" + n + "=" + n);
            n = n * 1;
        } else {
            System.out.println("5 *" + n + "=" + 5 * n);
            multiplicacionAscendente(n - 1);
        }
        return n;
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println("Multiplicacion Decendente");
        bup240594_recursividad obj = new bup240594_recursividad();
        obj.multiplicacionDecendente(n);
        System.out.println("Multiplicacion Asencdente");
        obj.multiplicacionAscendente(n);


    }
}
