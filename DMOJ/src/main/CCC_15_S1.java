package main;
import java.util.*;

public class CCC_15_S1{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        Stack<Integer> num = new Stack<Integer>();
        int times = input.nextInt();
        int total = 0;
        for(int i = 0; i < times; i++){
            int temp = input.nextInt();
            if(temp != 0){
                num.push(temp);
                total = total + temp;
            } else {
                total = total - num.pop();
            }
        }
        System.out.println(total);
    }
}