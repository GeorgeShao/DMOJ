package main;
import java.util.*;

public class CCC_19_J2 {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		
		int lines = input.nextInt();
		
		for(int i = 0; i < lines; i++) {
			int times = input.nextInt();
			String character = input.next();
			for(int j = 0; j < times; j++) {
				System.out.print(character);
			}
			System.out.println("");
		}
	}
}
