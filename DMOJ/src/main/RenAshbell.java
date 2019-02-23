package main;
import java.util.*;

public class RenAshbell {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int people = input.nextInt();
        int [] arr1 = new int[10];
        String result = "MAYBE";
        for(int i = 0; i < people-1; i++){
            arr1[i] = input.nextInt();
        }
        for(int i = 1; i < people; i++){
            if(arr1[i] >= arr1[0]){
                result = "NO";
                i = people;
            } else if (arr1[i] < arr1[0]){
                result = "YES";
            }
        }
        System.out.println(result);
    }
}