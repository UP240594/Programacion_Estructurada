public class codigoraro {
    public static void main(String[] args){
       int r = factor(3);
       System.out.println(r);
    }
    public static int factor(int limit){
        int number = 5, result = 0;
        for (int i=0; i< limit; i++){
            result += number;
        }
        return result;
    }
}
