package VoidSyntax9x12.M23JavaBasics.L3;

import java.util.Scanner;

public class GreaterThan10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a number:");
        int num = sc.nextInt();

        if (num > 10) {
            System.out.println("Yes, I am greater.");
        } else {
            System.out.println("Sorry, I feel bad.");
        }

        sc.close();
    }
}
