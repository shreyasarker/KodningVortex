package VoidSyntax9x12.M23JavaBasics.L5;

import java.util.Scanner;

class Operation {
    void performOperation(double num1, double num2) {
        // Empty method to be overridden
    }
}

class Addition extends Operation {
    @Override
    void performOperation(double num1, double num2) {
        double result = num1 + num2;
        System.out.println("Result of addition: " + result);
    }
}

class Subtraction extends Operation {
    @Override
    void performOperation(double num1, double num2) {
        double result = num1 - num2;
        System.out.println("Result of subtraction: " + result);
    }
}

class Multiplication extends Operation {
    @Override
    void performOperation(double num1, double num2) {
        double result = num1 * num2;
        System.out.println("Result of multiplication: " + result);
    }
}

class Division extends Operation {
    @Override
    void performOperation(double num1, double num2) {
        if (num2 != 0) {
            double result = num1 / num2;
            System.out.println("Result of division: " + result);
        } else {
            System.out.println("Error: Division by zero is not allowed.");
        }
    }
}

public class ACPCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double num1 = sc.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = sc.nextDouble();

        // Menu for selecting operation
        System.out.println("\nSelect operation:");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.print("Enter your choice (1/2/3/4): ");

        int choice = sc.nextInt();

        // Creating objects for corresponding classes based on user choice
        Operation operation = null;

        switch (choice) {
            case 1:
                operation = new Addition();
                break;
            case 2:
                operation = new Subtraction();
                break;
            case 3:
                operation = new Multiplication();
                break;
            case 4:
                operation = new Division();
                break;
            default:
                System.out.println("Invalid choice");
                return;
        }

        // Performing the operation
        operation.performOperation(num1, num2);

        sc.close();
    }
}
