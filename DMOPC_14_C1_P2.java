package main;
import java.io.*;
import java.util.*;

public class DMOPC_14_C1_P2 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int length = input.nextInt();
        int width = input.nextInt();
        int tileSize = input.nextInt();
        
        int lTiles = (int) Math.floor(length / tileSize);
        int wTiles = (int) Math.floor(width / tileSize);
        
        System.out.println(lTiles * wTiles);
    }
}