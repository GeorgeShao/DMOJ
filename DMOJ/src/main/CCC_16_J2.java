package main;
import java.util.Scanner;

public class CCC_16_J2{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int [][] marks = new int[4][4];
        //Getting User Input
        for(int i = 0; i < marks.length; i++){
            for(int j = 0; j < marks [i].length; j++){
                marks[i][j] = input.nextInt();
            }
        }
        //Find if it is a magic square
        int intBaseMagic = marks[0][0] + marks[1][0] + marks[2][0] + marks[3][0];
        if(intBaseMagic == marks[0][1] + marks[1][1] + marks[2][1] + marks[3][1]){
            if(intBaseMagic == marks[0][2] + marks[1][2] + marks[2][2] + marks[3][2]){
                if(intBaseMagic == marks[0][3] + marks[1][3] + marks[2][3] + marks[3][3]){
                    if(intBaseMagic == marks[0][0] + marks[0][1] + marks[0][2] + marks[0][3]){
                        if(intBaseMagic == marks[1][0] + marks[1][1] + marks[1][2] + marks[1][3]){
                            if(intBaseMagic == marks[2][0] + marks[2][1] + marks[2][2] + marks[2][3]){
                                if(intBaseMagic == marks[3][0] + marks[3][1] + marks[3][2] + marks[3][3]){
                                    System.out.println("magic");
                                } else {
                                    System.out.println("not magic");
                                }
                            } else {
                                System.out.println("not magic");
                            }
                        } else {
                            System.out.println("not magic");
                        }
                    } else {
                        System.out.println("not magic");
                    }
                } else {
                    System.out.println("not magic");
                }
            } else {
                System.out.println("not magic");
            }
        } else {
            System.out.println("not magic");
        }
    }
}