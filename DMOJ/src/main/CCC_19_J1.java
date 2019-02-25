package main;
import java.util.*;

public class CCC_19_J1 {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		
		int a = input.nextInt();
		int b = input.nextInt();
		int c = input.nextInt();
		int d = input.nextInt();
		int e = input.nextInt();
		int f = input.nextInt();
		
		if(a*3 + b*2 + c*1 > d*3 + e*2 + f*1) {
			System.out.println("A");
		} else if (a*3 + b*2 + c*1 < d*3 + e*2 + f*1){
			System.out.println("B");
		} else {
			System.out.println("T");
		}
	}
}
