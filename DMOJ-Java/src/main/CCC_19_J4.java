import java.io.*;
import java.util.*;

public class Main {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int topleft = 1;
        int topright = 2;
        int bottomleft = 3;
        int bottomright = 4;

        int temptopleft = 0;
        int temptopright = 0;
        int tempbottomleft = 0;
        int tempbottomright = 0;

        String moves = br.readLine();

        for(int i = 0; i < moves.length(); i++) {
            if(moves.substring(i,i+1).equals("H")) {
                temptopleft = bottomleft;
                temptopright = bottomright;
                tempbottomleft = topleft;
                tempbottomright = topright;
            } else if (moves.substring(i,i+1).equals("V")) {
                temptopleft = topright;
                temptopright = topleft;
                tempbottomleft = bottomright;
                tempbottomright = bottomleft;
            }
            topleft = temptopleft;
            topright = temptopright;
            bottomleft = tempbottomleft;
            bottomright = tempbottomright;
        }

        System.out.println(topleft + " " + topright);
        System.out.println(bottomleft + " " + bottomright);
    }
}