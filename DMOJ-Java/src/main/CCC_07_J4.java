package main;

import java.util.*;

public class CCC_07_J4{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        String str1 = input.nextLine();
        String str2 = input.nextLine();
        //Remove White Space In Both Strings
        str1 = str1.replaceAll(" ","");
        str2 = str2.replaceAll(" ","");
        //Go Through Each Char In Str2 and Find In Str1 and Str2
        //If there, replace both chars with empty string
        int count = 0;
        for(int i = 0; i < str1.length(); i++){
            if(str2.indexOf(str1.charAt(i)) >= 0){
                int x = str2.indexOf(str1.charAt(i));
                str2 = str2.substring(0,x) + "" + str2.substring(x+1,str2.length());
                count++;
            }
        }
        if(str2.equals("") && count == str1.length()){
            System.out.println("Is an anagram.");
        } else {
            System.out.println("Is not an anagram.");
        }
    }
}