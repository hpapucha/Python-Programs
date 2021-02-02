// Greeter Example
// Source code file Greeter.java
// The user is prompted to input for a name.  
// The application then constructs a greeting using that name.

import java.util.Scanner;

public class Greeter1
{
    public static void main(String[ ] args)
    {
        System.out.print("Enter your name: ");
        Scanner input = new Scanner(System.in);
        String name = input.nextLine( );
        System.out.println("Hello, " + name + ", how are you?");
    }
}