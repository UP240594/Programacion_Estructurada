class numero_si_existe{

    public static void main(String[] args){
        int[] e = {4,1,5,3,2}; //Arreglo
        int n = 1;

        for(int i=0; i< e.length ; i++){
            boolean x = false;
            if(n == e[i]){
                x = true;    
                System.out.println(e[i]);
            }else{
                System.out.println(-1);
            }
        }

    }


}