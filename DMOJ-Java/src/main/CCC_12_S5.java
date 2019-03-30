package main;
import java.util.*;

public class CCC_12_S5{
    public static void main (String [] args){
        Scanner input = new Scanner(System.in);
        int R = input.nextInt();
        int C = input.nextInt();
        int [][] path = new int[R+1][C+1];
        boolean [][] isCat = new boolean[R+1][C+1];
        for(int j = 0; j < isCat.length; j++){
            for(int k = 0; k < isCat[j].length; k++){
                isCat[j][k] = false;
            }
        }
        int n = input.nextInt();
        for(int i = 0; i < n; i++){
            int x = input.nextInt();
            int y = input.nextInt();
            isCat[x][y] = true;
        }
        path[1][1] = 1;
        isCat[1][1] = true;
        for(int i = 1; i < R+1; i++){
            for(int j = 1; j < C+1; j++){
                if(!isCat[i][j]){
                    path[i][j] = path[i-1][j] + path[i][j-1];
                }
            }
        }
        System.out.println(path[R][C]);
    }
}