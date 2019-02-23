package main;
import java.util.Arrays;
import java.util.Scanner;

public class ListMinimumHard {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int nums = input.nextInt();
		
		Integer [] arr1 = new Integer[nums];
		
		for(int i = 0; i < nums; i++) {
			arr1[i] = input.nextInt();
		}
		
		Arrays.sort(arr1);
		
		for(int j = 0; j < nums; j++) {
			System.out.println(arr1[j]);
		}
    }
}