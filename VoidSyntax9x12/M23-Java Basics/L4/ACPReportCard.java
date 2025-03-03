package L4;

import java.util.Scanner;

public class ACPReportCard {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        // Getting student name
        System.out.print("Enter student name: ");
        String name = sc.nextLine();

        // Getting number of subjects with validation
        int no = 0;
        while (no <= 0) {
            System.out.print("Enter number of subjects (positive integer): ");
            if (sc.hasNextInt()) {
                no = sc.nextInt();
                if (no <= 0) {
                    System.out.println("Please enter a positive number.");
                }
            } else {
                System.out.println("Invalid input. Please enter a valid integer.");
                sc.next(); // Clear invalid input
            }
        }

        // Create an integer array to store subject marks
        int[] marks = new int[no];

        marksEntry(marks); // Method call for entering marks

        printReportCard(name, marks, no); // Method call to generate report card
    }

    // Method to enter marks
    static void marksEntry(int[] marks) {
        for (int i = 0; i < marks.length; i++) {
            while (true) {
                System.out.print("Enter mark for Subject-" + (i + 1) + ": ");
                if (sc.hasNextInt()) {
                    marks[i] = sc.nextInt();
                    if (marks[i] >= 0 && marks[i] <= 100) {
                        break; // Valid input, move to next subject
                    } else {
                        System.out.println("Invalid mark. Enter a mark between 0 and 100.");
                    }
                } else {
                    System.out.println("Invalid input. Please enter a valid integer.");
                    sc.next(); // Clear invalid input
                }
            }
        }
    }

    // Method to generate the report card
    static void printReportCard(String name, int[] marks, int no) {
        System.out.println("---------------------------------------");
        System.out.println("\t REPORT CARD");
        System.out.println("NAME: " + name);
        System.out.println("---------------------------------------");

        System.out.println("  SUBJECT \t MARK");
        System.out.println("---------------------------------------");

        int total = 0;

        for (int i = 0; i < marks.length; i++) {
            System.out.println("Subject-" + (i + 1) + "\t  " + marks[i]);
            total += marks[i];
        }
        System.out.println("---------------------------------------");

        float avg = ((float) total) / no;
        System.out.printf("TOTAL: %d \tAVERAGE: %.2f \n", total, avg);
        System.out.println("---------------------------------------");
    }
}
