package VoidSyntax9x12.M23JavaBasics.L3;

import java.util.Scanner;

public class Ten10 {
    public static void main(String[] args) {
        // Using for loop to print numbers in descending order
        System.out.println("First 10 natural numbers in descending order:");
        for (int i = 10; i >= 1; i--) {
            System.out.print(i + " ");
        }

        System.out.println(); // Move to the next line for better formatting

        // Using while loop to print numbers in ascending order
        System.out.println("First 10 natural numbers in ascending order:");
        int j = 1;
        while (j <= 10) {
            System.out.print(j + " ");
            j++;
        }
    }
}
