package main;
import java.util.Scanner;

public class CCC_12_J3{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int scalefactor = input.nextInt();
        String cross = "";
        String space = "";
        String asterisk = "";
        for(int i = 0; i < scalefactor; i++){
            cross = cross + "x";
            space = space + " ";
            asterisk = asterisk + "*";
        }
        String p1 = " " + asterisk + cross + asterisk;
        String p2 = " " + space + cross + cross;
        String p3 = " " + asterisk + space + asterisk;
        
        for(int i = 0; i < scalefactor; i++){
            System.out.println(p1);
        }
        for(int i = 0; i < scalefactor; i++){
            System.out.println(p2);
        }
        for(int i = 0; i < scalefactor; i++){
            System.out.println(p3);
        }
    }
}