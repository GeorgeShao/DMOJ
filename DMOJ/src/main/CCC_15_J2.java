package main;
import java.util.Scanner;

public class CCC_15_J2{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int happy = 0;
        int sad = 0;
        String str = input.nextLine();
        for(int i = 0; i < str.length()-3; i++){
            if(str.charAt(i) == ':'){
                if(str.substring(i, i+3).equals(":-)")){
                    happy++;
                } else if (str.substring(i, i+3).equals(":-(")){
                    sad++;
                }
            }
        }
        if(happy > sad)System.out.println("happy");
        else if (sad > happy)System.out.println("sad");
        else if (happy != 0 && sad !=0 && (happy == sad))System.out.println("unsure");
        else System.out.println("none");
    }
}