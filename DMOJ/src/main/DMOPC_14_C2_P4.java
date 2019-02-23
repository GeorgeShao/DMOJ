package main;
import java.util.*;
import java.io.*;

public class DMOPC_14_C2_P4 {
    public static void main(String [] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int [] psa = new int [N];
        for(int i = 0; i < N; i++){
            psa[i] = Integer.parseInt(br.readLine());
        }
        for(int i=1; i < N; i++){
            psa[i] += psa[i-1];
        }
        int Q = Integer.parseInt(br.readLine());
        for(int i = 0; i < Q; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
            if(a == 0){
                System.out.println(psa[b]);
            } else {
                System.out.println(psa[b] - psa[a-1]);
            }
        }
    }
}