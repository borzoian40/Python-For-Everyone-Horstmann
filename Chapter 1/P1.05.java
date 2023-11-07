"""
P1.5 Write a program that displays your name inside a box on the screen, like this:
          +------+
          | Dave |
          +------+
    Do your best to approximate lines with characters such as | - +.
"""
import java.util.Scanner;

public class hello {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a word: ");
        String str = scan.nextLine();
        char[] letters_input = str.toCharArray();


        int length_of_str = str.length();

        // Printing the pattern
        for (int row = 0; row < 5; row++) {
            if (row == 0 || row == 4) {
                for (int i = 0; i < length_of_str + 4; i++) {
                    if (i == 0 || i == length_of_str + 3) {
                        System.out.print("+");
                    } else {
                        System.out.print("-");
                    }
                }
                System.out.println();
            } else {
                if (row == 1 || row == 3) {
                    for (int x = 0; x < length_of_str + 4; x++) {
                        if (x == 0 || x == length_of_str + 3) {
                            System.out.print("|");
                        } else {
                            System.out.print(" ");
                        }

                    }
                    System.out.println();
                } else {
                    int index = 0;
                    for (int x = 0; x < length_of_str + 4; x++) {

                        if (x == 0 || x == length_of_str + 3) {
                            System.out.print("|");
                        } else if (x == 1 || x == length_of_str + 2) {
                            System.out.print(" ");
                        } else {
                            System.out.print(letters_input[index]);
                            index++;
                        }

                    }
                    System.out.println();

                }
            }


        }//end of main for

    }//end of main

}//end of class


