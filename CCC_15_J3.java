package main;
import java.util.Scanner;

public class CCC_15_J3{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        String alphabets = "abcdefghijklmnopqrstuvwxyz";
        String closevows = "aaaeeeeiiiiioooooouuuuuuuu";
        String consonant = "bcdfghjklmnpqrstvwxyz";
        String nextconso = "cdfghjklmnpqrstvwxyzz";
        String word = input.next();
        for(int i = 0; i < word.length(); i++){
            if(consonant.indexOf(word.charAt(i)) == -1){
                System.out.print(word.charAt(i));
            } else {
                System.out.print(word.charAt(i));
                System.out.print(closevows.charAt((alphabets.indexOf(word.charAt(i)))));
                System.out.print(nextconso.charAt(consonant.indexOf(word.charAt(i))));
            }
        }
    }
}