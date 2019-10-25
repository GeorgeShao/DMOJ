package main;
import java.util.Scanner;

public class CCC_17_J3 {
    public static void main (String [] args){
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int y = input.nextInt();
        int finX = input.nextInt();
        int finY = input.nextInt();
        int energy = input.nextInt();
        int standard = Math.abs(x-finX) + Math.abs(y-finY);
        if(standard <= energy && (energy - standard) % 2 == 0){
            System.out.println("Y");
        } else {
            System.out.println("N");
        }
    }
}