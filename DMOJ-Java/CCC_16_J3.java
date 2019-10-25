package main;
import java.util.Scanner;

public class CCC_16_J3{
    public static void printname(){
        System.out.println("CCC is on it's way");
    }
    public static void printname(String name){
        System.out.println(name);
    }
    public static int sum(int a, int b){
        return a + b;
    }
    public static boolean isEven(int x){
        return x % 2 == 0;
    }
    public static String substring(String str, int a, int b){
        String temp = "";
        for(int i = 0; i < b; i++){
            temp = temp + str.charAt(i);
        }
        return temp;
    }
    public static String reverse(String str){
        String temp = "";
        for(int i = str.length()-1; i >= 0; i--){
            temp = temp + str.charAt(i);
        }
        return temp;
    }
    public static boolean isPalindrome(String str){
        return str.equals(reverse(str));
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String word = input.next();
        int maxlength = 0;
        for(int i = 0; i < word.length(); i++){
            for(int j = i+1; j <= word.length(); j++){
                if(isPalindrome(word.substring(i, j))){
                    if(word.substring(i, j).length() >= maxlength){
                        maxlength = word.substring(i, j).length();
                    }
                }
            }
        }
        System.out.println(maxlength);
    }
}