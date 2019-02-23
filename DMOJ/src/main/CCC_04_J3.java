package main;
import java.util.*;

public class CCC_04_J3{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        String [] arr1 = new String[a];
        String [] arr2 = new String[b];
        for(int i = 0; i < a; i++){
            arr1[i] = input.next();
        }
        for(int j = 0; j < b; j++){
            arr2[j] = input.next();
        }
        for(int i = 0; i < a; i++){
            for(int j = 0; j < b; j++){
                System.out.println(arr1[i] + " as " + arr2[j]);
            }
        }
    }
}