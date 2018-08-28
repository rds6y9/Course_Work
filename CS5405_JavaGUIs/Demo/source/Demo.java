/**
  Demo file to perform operations required by homework 1.

  PROGRAMMER: Ryan Stoughton
  PROFESSOR:  Dr. Sabharwal
  CLASS:      CS5405 - Java GUIs
  ASSIGNMENT: Homework 1
 */

package code;

import java.util.Scanner;

public class Demo {

    public static void main(String args[]) {
        System.out.println("\n\n~~~~~|*~*~*~*~* Homework 1 Program *~*~*~*~*|~~~~~\n\n");
     
        Scanner scanner = new Scanner(System.in);

        System.out.printf("Enter Real Name: ");
        String name = scanner.nextLine();

        System.out.printf("Enter Phone Number: ");
        String number = scanner.nextLine();

        System.out.printf("Enter Address: ");
        String address = scanner.nextLine();

        System.out.printf("\n\nMy Real Name is %s\n", name);
        System.out.printf("My Phone Number is %s\n", number);
        System.out.printf("My Address is %s\n\n\n", address);


        System.out.println("~~~~~|*~*~*~* Thank You Dr. Sabharwal *~*~*~*|~~~~~\n\n");
    }

}