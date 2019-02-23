package main;
import java.util.*;

public class Ship {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        String all = "BFTLC";
        String parts = input.next();
        for(int i = 0; i < parts.length(); i++){
            all = all.replaceAll(parts.substring(i,i+1), "");
        }
        if(all.equals("")){
            System.out.println("NO MISSING PARTS");
        } else {
        System.out.println(all);
        }
    }
}