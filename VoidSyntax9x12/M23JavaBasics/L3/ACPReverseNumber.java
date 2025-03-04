package VoidSyntax9x12.M23JavaBasics.L3;

import java.util.Scanner;

public class ACPReverseNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Step 1: Taking input from the user
        System.out.print("Enter a 3-digit number: ");
        int number = scanner.nextInt();

        // Step 2: Breaking the number into digits and reversing it
        int reversedNumber = 0;

        // Loop to break the number into digits
        while (number != 0) {
            int digit = number % 10; // Get the last digit
            reversedNumber = reversedNumber * 10 + digit; // Build the reversed number
            number = number / 10; // Remove the last digit
        }

        // Step 3: Displaying the reversed number
        System.out.println("Reversed Number: " + reversedNumber);

        scanner.close();
    }
}
