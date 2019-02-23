package main;
import java.util.Scanner;
import java.util.Stack;

public class CCC_14_S3{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int caseCount = input.nextInt();
        while(caseCount-- != 0){
            Stack<Integer> mountainTop = new Stack<Integer>();
            Stack<Integer> branch = new Stack<Integer>();
            int cartCount = input.nextInt();
            for(int i=0; i < cartCount; i++)
                mountainTop.add(input.nextInt());
            int currentNumber = 1;
            boolean noSolution = true;
            while(true){
                if (mountainTop.isEmpty() && branch.isEmpty()) {
                    noSolution = false;
                    break;
                }
                if (!mountainTop.isEmpty() && mountainTop.peek() == currentNumber){
                    mountainTop.pop();
                    currentNumber += 1;
                    continue;
                } else if (!branch.isEmpty() && branch.peek() == currentNumber){
                    branch.pop();
                    currentNumber += 1;
                    continue;
                } else {
                    if (mountainTop.isEmpty()){
                        break;
                    }
                    branch.push(mountainTop.pop());
                }
            }
            if (noSolution)
                System.out.println("N");
            else
                System.out.println("Y");
        }
    }
}