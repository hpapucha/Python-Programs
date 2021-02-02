// Cel2FahrWithValidation Example
// Convert a Celsius temperature to Fahrenheit.
// Don't allow input temperatures less than absolute zero (-273 degrees C). 

import java.util.Scanner;

public class Cel2FahrWithValidation
{
    public static void main(String[ ] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.err.print("Enter a Celsius temperature: ");
        double cel = Double.parseDouble(scanner.nextLine( ));
        if(cel < -273.0)
        {
            System.err.println("Input temperature cannot be less than absolute zero.");
            System.exit(0);
        }
        double fahr = 9.0 * cel / 5.0 + 32.0;
        System.out.println(
            "The corresponding Fahrenheit temperature is " + fahr + ".");
    }
}