package main;
import java.util.Scanner;

public class CCC_03_J1{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int sum = 0;
        int sum2 = 0;
        int length = input.nextInt();
        int spacing = input.nextInt();
        int handle = input.nextInt();
        //Print Out Tines
        for(int k = 1; k <= length; k++){
            for(int i = 1; i <= 2; i++){
            System.out.print("*");
            for(int j = 1; j <= spacing; j++){
                System.out.print(" ");
            }
        }
        System.out.print("*");
        System.out.println("");
        }
        //Print Out Bar Below Tines
        sum = spacing + spacing + 3;
        for(int l = 0; l < sum; l++){
            System.out.print("*");
        }
        System.out.println("");
        //Print Out Handle
        sum2 = spacing + 1;
        for(int n = 1; n <= handle; n++){
            for(int m = 0; m < sum2; m++){
                System.out.print(" ");
            }
        System.out.println("*");
        }
    }
}
