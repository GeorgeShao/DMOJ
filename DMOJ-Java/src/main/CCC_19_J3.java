import java.util.*;
import java.io.*;

public class Main {
    public static void main(String [] args) {
        Scanner input = new Scanner(System.in);

        int lines = input.nextInt();
        int counter = 0;

        for(int i = 0; i < lines; i++) {
            String line = input.next();
            while(!line.isEmpty()) {
                String startchar = line.substring(0, 1);
                for(int j = 0; j < line.length(); j++) {
                    counter = 0;
                    try{
                        while(startchar.equals(line.substring(counter, counter+1))) {
                            if(counter < line.length()) {
                                counter++;
                            }
                        }
                    } catch (Exception e){

                    }

                }
                System.out.print(counter + " " + startchar + " ");
                line = line.substring(counter, line.length());
            }
            System.out.println("");
        }
    }
}