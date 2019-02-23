package main;
import java.util.*;

public class AMinusB {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int nums = input.nextInt();
        int a = 0;
        int b = 0;
        int diff = 0;
        for(int i = 0; i < nums; i++){
            a = input.nextInt();
            b = input.nextInt();
            diff = a - b;
            System.out.println(diff);
        }
    }
}