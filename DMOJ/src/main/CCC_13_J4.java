package main;

import java.util.Scanner;
import java.util.Arrays;
public class CCC_13_J4{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int maxTime = input.nextInt();
        int ntask = input.nextInt();
        int [] time = new int[ntask];
        for(int i = 0; i < ntask; i++){
            time[i] = input.nextInt();
        }
        Arrays.sort(time);
        int counter = 0;
        int index = 0;
        int total = 0;
        while(total <= maxTime){
            total = total + time[index];
            index++;
            counter++;
        }
        System.out.println(counter-1);
    }
}