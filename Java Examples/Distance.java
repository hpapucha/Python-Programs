// Distance Example
// Source code file Distance.java
// Compute distance to origin "as the crow flies." 

import java.util.Scanner;

public class Distance
{
    public static void main(String[ ] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.err.print("Enter the x-coordinate: ");
        double x = Double.parseDouble(scanner.nextLine( ));
        System.err.print("Enter the y-coordinate: ");
        double y = Double.parseDouble(scanner.nextLine( ));
        double dist = Math.sqrt(Math.pow(x, 2.0) + Math.pow(y, 2.0));
        System.out.println("The distance from (0, 0) to (x, y) is " + dist + ".");
    }
}