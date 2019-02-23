package main;
import java.util.*;

public class ListMinimum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        int [] list = new int[num];
        for(int i = 0; i < num; i++){
            list[i] = input.nextInt();
        }
        Arrays.sort(list);
        for(int i = 0; i < list.length; i++){
            System.out.println(list[i]);
        }
    }
}