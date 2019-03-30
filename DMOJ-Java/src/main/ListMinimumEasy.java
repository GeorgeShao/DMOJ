package main;

import java.util.Scanner;

public class ListMinimumEasy {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int nums = input.nextInt();
		
		for(int i = 0; i < nums; i++) {
			System.out.print(i + 1);
			if(i != nums - 1) {
				System.out.print(" ");
			}
		}
    }
}