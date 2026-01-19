public class multiplicacion_matriz {
    public static void main(String[] args){
        double[][] A =   {{1,3},{2,4}};
        double[][] B = {{2,0,-4},{3,2,6}};
        int FA = A.length;
        int CA = A[0].length;
        int CB = B[0].length;

        
        double[][] C = new double[FA][CB];

        for(int i=0; i<FA; i++){
            for(int j=0; j<CB; j++){
                for(int k=0; k<CA ; k++){
                    C[i][j]  +=  A[i][k] * B[k][j];
                }
            }
        }


        for(int i = 0; i<FA; i++ ){
            for(int j = 0; j<CB; j++){
                System.out.print(C[i][j] + "  ");
            }
             System.out.println();
 
        }
    }
}
