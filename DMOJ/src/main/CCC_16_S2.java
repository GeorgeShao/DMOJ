package main;
import java.util.*;

public class CCC_16_S2{
    public static int max(int a, int b){
            if(a > b){
                return a;
            } else {
                return b;
            }
        }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int qn = input.nextInt();
        int np = input.nextInt();
        int [] D = new int[np];
        int [] P = new int[np];
        for(int i = 0; i < np; i++){
            D[i] = input.nextInt();
        }
        for(int i = 0; i < np; i++){
            P[i] = input.nextInt();
        }
        Arrays.sort(D);
        Arrays.sort(P);
        int count = 0;
        if(qn == 2){
            for(int i = 0; i < D.length; i++){
                count = count + max(D[i],P[D.length-1-i]);
            }
        } else if (qn == 1){
            for(int i = 0; i < D.length; i++){
                count = count + max(D[i],P[i]);
            }
        }
        System.out.println(count);
    }
}