package main;
import java.util.Scanner;

public class CCC_11_J1{
    public static void main (String [] args){
        Scanner input = new Scanner(System.in);
        int antennas,eyes;
        antennas = input.nextInt();
        eyes = input.nextInt();
        if(antennas >= 3 && eyes <= 4){
            System.out.println("TroyMartian");
        }
        if(antennas <= 6 && eyes >= 2){
            System.out.println("VladSaturnian");
        }
        if(antennas <= 2 && eyes <= 3){
            System.out.println("GraemeMercurian");
        }
    }
}