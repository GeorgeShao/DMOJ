package main;
import java.util.*;

public class CCC_16_J1 {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        String [] arr1 = new String[6];
        int win = 0;
        int lose = 0;
        for(int i = 0; i < 6; i++){
            arr1[i] = input.next();
            if(arr1[i].equals("W")){
                win++;
            } else {
                lose++;
            }
        }
        if(win == 5 || win == 6){
            System.out.println(1);
        }
        if(win == 3 || win == 4){
            System.out.println(2);
        }
        if(win == 1 || win == 2){
            System.out.println(3);
        }
        if(win == 0){
            System.out.println(-1);
        }
    }
}