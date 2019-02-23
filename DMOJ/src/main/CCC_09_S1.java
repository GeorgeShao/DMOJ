package main;
import java.util.*;

public class CCC_09_S1{
    public static void main(String[] args) {
        Scanner input = new Scanner (System.in);
        int x = input.nextInt();
        int y = input.nextInt();
        int done = 0;
        for (int i = x; i <= y; i++){
            if (Math.sqrt(i)==(int)Math.sqrt(i) && Math.cbrt(i)==(int)Math.cbrt(i)){
                done += 1;
            }
        }
        System.out.print(done);
    }
}