package main;
import java.io.*;
import java.util.Scanner;

public class CCC_18_J3 {
	public static void main (String [] args) throws IOException{
		Scanner input = new Scanner(System.in);
		
		int cities [] = new int[6];
		cities[0] = 0;
		
		for(int i = 1; i < 5; i++) {
			cities[i] = input.nextInt();
		}
		
		input.close();
		
		int sums [] = new int[6];
		
		for(int i = 1; i < 6; i++) {
			for(int j = 0; j < i; j++) {
				sums[i] += cities[j];
			}
		}
		
		for(int i = 1; i < 6; i++) {
			for(int j = 1; j < 6; j++) {  	
				System.out.print(Math.abs(sums[i] - sums[j]) + " ");
			}
			System.out.println("");
		}
	}
}