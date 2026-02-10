class bup240594_insertion_sort{
    public static void main(String[] args){
        int[] e = {4,1,5,3,2}; //Arreglo
        int f = e.length; //Sacamos ls valores totales del arreglo
        for(int i=1; i<f ; i++){  //hacemos el for, que va a ir comparando de 1 a f en este caso a 5
            int key = e[i]; 
            int j=i-1;
            while(j>=0 && e[j] > key){
                e[j+1] = e[j];
                j=j-1;
            }
           e[j+1] = key;
        }

        //for para imprimir datos
        for(int i=0 ; i<f ; i++){
            System.out.println(e[i]);
        }
        
    }
}