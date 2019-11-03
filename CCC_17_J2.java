package main;
import java.util.*;

public class CCC_17_J2 {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int k = input.nextInt();
        int temp = 0;
        int sum = 0;
        int [] nums = new int[10];
        for(int i = 0; i < nums.length; i++){
            nums[i] = 0;
        }
        for(int x = 0; x <= k; x++){
            temp = N;
            for(int j = 0; j < x; j++){
                temp = temp * 10;
            }
            nums[x] = temp;
        }
        for(int y = 0; y < nums.length; y++){
            sum = sum + nums[y];
        }
        System.out.println(sum);
    }
}