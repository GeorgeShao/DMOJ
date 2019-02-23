package main;
import java.io.*;
import java.util.*;

public class CCC_13_J3 {
  public static void main(String[] args) throws IOException{
    
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String year = br.readLine();
		
		for(int i = Integer.parseInt(year) + 1;; i++){
			
			String testyear = Integer.toString(i);
			boolean [] characters = new boolean[100];
			boolean unique = true;;
			
			for(int x = 0; x < testyear.length(); x++){
				if (characters[testyear.charAt(x) - '0']){
					unique = false;
					break;
				} else{
					characters[testyear.charAt(x)-'0'] = true;	
				}
			}
			
			if(unique){
				System.out.println(testyear);
				return;
			}
			
		}
  }
}