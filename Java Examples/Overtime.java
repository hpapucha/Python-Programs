// Overtime Example
// Source code file Overtime.java
// Compute total salary paying time and a half for any hours over 40.0
// Inputs: hours_worked, hourly_salary 

import java.util.*;

public class Overtime
{
    public static void main(String[ ] args)
    {
        // Instantiate scanner.
        Scanner scanner = new Scanner(System.in);
        
        // Input hours worked and hourly salary.
        System.out.print("Enter hours worked: ");
        double hoursWorked = Double.parseDouble(scanner.nextLine( ));
        System.out.print("Enter hourly salary: ");
        double hourlySalary = Double.parseDouble(scanner.nextLine( ));        
        
        // Validate input.
        if(hoursWorked < 0.0)
        {
            System.out.println("Hours worked cannot be negative.");
            System.exit(0);
        }
        if(hourlySalary < 0.0)
        {
            System.out.println("Hourly salary cannot be negative.");
            System.exit(0);
        }

        // Compute total wages.
        double totalWages;
        if(hoursWorked > 40.0)
        {
            totalWages = hourlySalary * (40.0 + (hoursWorked - 40) * 1.5);
        }
        else
        {   
            totalWages	= hoursWorked * hourlySalary;
        }
        
        // Print output.
        System.out.println("Total wages = " + totalWages);
    }
}
