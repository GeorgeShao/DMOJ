package main;
import java.util.Scanner;

public class CCC_15_J1{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int month = input.nextInt();
        int day = input.nextInt();
        if(month == 2 && day == 18)System.out.println("Special");
        if(month == 2 && day < 18)System.out.println("Before");
        if(month == 2 && day > 18)System.out.println("After");
        if(month < 2)System.out.println("Before");
        if(month > 2)System.out.println("After");
    }
}