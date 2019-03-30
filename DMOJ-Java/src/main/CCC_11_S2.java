package main;
import java.util.Scanner;

public class CCC_11_S2{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int lines = input.nextInt();
        String student = "";
        String teacher = "";
        int correct = 0;
        for(int i = 0; i < lines; i++){
            student += input.next();
        }
        for(int j = 0; j < lines; j++){
            teacher += input.next();
        }
        for(int k = 0; k < lines; k++){
            if(teacher.charAt(k) == student.charAt(k)){
                correct++;
            }
        }
        System.out.println(correct);
    }
}