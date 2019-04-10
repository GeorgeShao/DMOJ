package main;

import java.io.*;
import java.util.*;

public class CCC_98_S2 {
    public static void main (String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sum = 0;

        for(int i = 1000; i < 9999; i++){
            for(int j = 1; j < i; j++){
                if(i % j == 0){
                    sum += j;
                }
            }
            if(sum == i){
                System.out.println(sum);
            }
            sum = 0;
        }

        for(int i = 100; i <= 999; i++){
            if(Math.pow(Math.floor(i/100),3) + Math.pow((Math.floor(i/10) - Math.floor(i/100)*10),3) + Math.pow(i - 100*Math.floor(i/100) - 10*(Math.floor(i/10) - Math.floor(i/100)*10),3) == i){
                System.out.print(i + " ");
            }
        }
    }
}
