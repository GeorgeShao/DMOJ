package main;
import java.io.*;

public class CCC_18_J2 {
	public static void main (String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int spaces = Integer.parseInt(br.readLine());
		String day1 = "";
		String day2 = "";
		int occupiedBothDays = 0;
		
		day1 = br.readLine();
		day2 = br.readLine();
		
		for(int i = 0; i < spaces; i++) {
			if(day1.substring(i, i+1).equals("C") && day2.substring(i, i+1).equals("C")) {
				occupiedBothDays++;
			}
		}
		
		System.out.println(occupiedBothDays);
	}
}