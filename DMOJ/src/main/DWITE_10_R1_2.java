package main;
import java.util.*;

public class DWITE_10_R1_2 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        for(int j = 0; j < 5; j++){
            String line = input.nextLine();
            int pos = line.indexOf("*");

            for(int k = 0; k < 5; k++){
                String move = input.nextLine();
                if(move.equals("L")){
                    if(pos > 0){
                        pos--;
                    }
                } else if (move.equals("R")){
                    if(pos < 4){
                        pos++;
                    }
                }
            }
            
            if(pos < 0){
                pos = 0;
            } else if (pos > 4){
                pos = 4;
            }
            
            for(int i = 0; i < 5; i++){
                if(pos == i){
                    System.out.print("*");
                } else {
                    System.out.print(".");
                }
            }
            System.out.println("");
        }
        
    }
}