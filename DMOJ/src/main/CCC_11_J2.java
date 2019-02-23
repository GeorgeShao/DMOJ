package main;
import java.util.Scanner;

public class CCC_11_J2{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int humidity = input.nextInt();
        int maximumTIME = input.nextInt();
        int currentTIME = 1;
        boolean landed = false;
        while(currentTIME != maximumTIME && landed != true){
            double A1 = -6*(Math.pow(currentTIME, 4));
            double A2 = humidity*(Math.pow(currentTIME, 3));
            double A3 = 2*(Math.pow(currentTIME, 2));
            double A4 = currentTIME;
            double AA = A1 + A2 + A3 + A4;
            if(AA <= 0){
                landed = true;
                System.out.println("The balloon first touches ground at hour:");
                System.out.println(currentTIME);
            }
            currentTIME++;
        }
        if(landed == false){
            System.out.println("The balloon does not touch ground in the given time.");
        }
    }
}