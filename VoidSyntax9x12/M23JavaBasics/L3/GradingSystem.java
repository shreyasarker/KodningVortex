package VoidSyntax9x12.M23JavaBasics.L3;

import java.util.Scanner;

public class GradingSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter marks: ");
        int marks = scanner.nextInt();

        if (marks > 90) {
            System.out.println("Grade: O");
        } else if (marks > 80 && marks <= 90) {
            System.out.println("Grade: A+");
        } else if (marks > 70 && marks <= 80) {
            System.out.println("Grade: A");
        } else if (marks > 60 && marks <= 70) {
            System.out.println("Grade: B");
        } else {
            System.out.println("Grade: C");
        }

        scanner.close();
    }
}
