package main;
import java.util.Scanner;

public class CCC_14_J3{
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int rounds = input.nextInt();
        int numA;
        int numB;
        int ScoreA = 100;
        int ScoreB = 100;
        for(int i = 0; i < rounds; i++){
            numA = input.nextInt();
            numB = input.nextInt();
            if(numB > numA){
                ScoreA -= numB;
            } else if (numA > numB){
                ScoreB -= numA;
            }
        }
        System.out.println(ScoreA);
        System.out.println(ScoreB);
    }
}