/*
P1.5 Write a program that displays your name inside a box on the screen, like this:
          +------+
          | Dave |
          +------+
    Do your best to approximate lines with characters such as | - +.
*/
//chatGPT's solution to P1.5 question: 

import java.util.Scanner;

public class P1_05 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Please enter your name: ");
        String name = scan.nextLine();

        int nameLength = name.length();
        int boxWidth = nameLength + 4;

        // Top border
        System.out.print("+");
        for (int i = 0; i < boxWidth - 2; i++) {
            System.out.print("-");
        }
        System.out.println("+");

        // Middle section with name
        System.out.println("| " + name + " |");

        // Bottom border
        System.out.print("+");
        for (int i = 0; i < boxWidth - 2; i++) {
            System.out.print("-");
        }
        System.out.println("+");
    
    }//end of main
}//end of class


