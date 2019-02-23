package main;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boolean {
	public static void main (String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String sentence = br.readLine();
		
		StringTokenizer tokens = new StringTokenizer(sentence);
	    int nums = tokens.countTokens() - 1;
	    
	    if(nums % 2 == 0) {
	    	if(sentence.indexOf("True") == -1) {
	    		System.out.println("False");
	    	} else {
	    		System.out.println("True");
	    	}
	    } else {
	    	if(sentence.indexOf("True") == -1) {
	    		System.out.println("True");
	    	} else {
	    		System.out.println("False");
	    	}
	    }
	}
}