package main;
import java.util.Scanner;

public class CCC_12_J4{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int k = input.nextInt();
        input.nextLine();
        String encrypted = input.nextLine();
        String decrypted = "";
        String line = "";
        for(int i = 0; i < 20; i++){
            line = line + "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        }
        char c1 = 'A';
        int c2 = 0;
        for(int i = 0; i < encrypted.length(); i++){
            c1 = encrypted.charAt(i);
            c2 = ((int)(c1)) - 65;
            int shift = (3*(i+1))+k;
            c2 = c2 - shift;
            c1 = line.charAt(c2+26);
            decrypted = decrypted + c1;
        }
        System.out.println(decrypted);
    }
}