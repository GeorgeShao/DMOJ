package main;
import java.util.Scanner;

public class CCC_04_J2{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        System.out.println("All positions change in year " + a);
        int i = a;
        while(i <= b){
            if((i + 60) <= b){
                System.out.println("All positions change in year " + (i + 60));
                i += 60;
            } else {
                i++;
            }
        }
    }
}