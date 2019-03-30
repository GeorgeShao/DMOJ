package main;
import java.io.*;
import java.util.*;

public class SixteenBitSWOnly {
    public static void main(String[] args) throws IOException{
        Scanner input = new Scanner(System.in);
    	
        int questions = (int) input.nextDouble();
        int a = 0;
        int b = 0;
        int c = 0;
        
        for(int i = 0; i < questions; i++){
        	try {
        		a = (int) input.nextLong();
        		b = (int) input.nextLong();
        		c = (int) input.nextLong();
        	} catch (Exception e) {
        	}
            if(a * b == c){
                System.out.println("POSSIBLE DOUBLE SIGMA");
            } else {
                System.out.println("16 BIT S/W ONLY");
            }
        }
    }
}