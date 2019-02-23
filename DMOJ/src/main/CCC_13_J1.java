package main;
import java.io.*;
import java.util.*;

public class CCC_13_J1 {
  public static void main(String[] args) throws IOException{
    BufferedReader input = new BufferedReader (new InputStreamReader (System.in));
    int num1 = Integer.parseInt(input.readLine());
    int num2 = Integer.parseInt(input.readLine());
    System.out.println(num2 - num1 + num2);
  }
}