package L3;

import java.util.Scanner;

public class HelloUser {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Please enter a string");
        String str = sc.nextLine();
        System.out.println("String is " + str);

        System.out.println("Please enter an integer");
        int num = sc.nextInt();
        System.out.println("Number is " + num);

        System.out.println("Please enter a float");
        float fnum = sc.nextFloat();
        System.out.println("Floating Number is " + fnum);

        sc.close();
    }
}
