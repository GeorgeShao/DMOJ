package main;
import java.io.*;

public class CCC_18_J1 {
	public static void main (String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int digit1 = Integer.parseInt(br.readLine());
		int digit2 = Integer.parseInt(br.readLine());
		int digit3 = Integer.parseInt(br.readLine());
		int digit4 = Integer.parseInt(br.readLine());
		
		if(digit1 == 8 || digit1 == 9) {
			if(digit4 == 8 || digit4 == 9) {
				if(digit2 == digit3) {
					System.out.println("ignore");
				} else {
					System.out.println("answer");
				}
			} else {
				System.out.println("answer");
			}
		} else {
			System.out.println("answer");
		}
	}
}