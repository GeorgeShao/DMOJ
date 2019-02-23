package main;
import java.util.*;

public class UnevenSand {
    public static void main(String [] args) throws Exception{
        Scanner input = new Scanner(System.in);
        long low = 1;
        long high = 2000000000;
        long guess = 1000000000;
        System.out.println(guess);
        System.out.flush();
        String str = input.next();
        for(int i = 0; low <= high; i++){
            if(str.equals("FLOATS")){
                high = guess - 1;
                guess = low + (high-low)/2;
                System.out.println(guess);
                System.out.flush();
            } else if(str.equals("SINKS")){
                low = guess + 1;
                guess = low + (high-low)/2;
                System.out.println(guess);
                System.out.flush();
            } else {
                break;
            }
            str = input.next();
            System.out.flush();
        }
    }
}
