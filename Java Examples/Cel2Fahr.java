// Cel2Fahr Example
// Source code file Cel2Fahr.java
// Convert a Celsius temperature to Fahrenheit. 

import java.util.Scanner;

public class Cel2Fahr
{
    public static void main(String[ ] args)
    {
        System.err.print("Enter a Celsius temperature: ");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine( );
        double cel = Double.parseDouble(input);
        double  fahr = 9.0 * cel / 5.0 + 32.0;
        System.out.print(
          "The corresponding Fahrenheit temperature is " + fahr + ".\n");
    }
}