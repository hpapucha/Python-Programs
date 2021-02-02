#Monthly Loan Income 

#Loan amount
p = int(input("Enter the loan amount: "))
if p <= 0:
    print("Error, the amount can't be less than 0.")
    exit( )

#Interest rate
r = int(input("Enter the interest rate: "))
if r <= 0:
    print("Error, interest rate can't be less than 0.")
    exit( )

#Number of years
n = int(input("Enter the number of years: "))
if n <= 0:
    print("Error, number of years can't be less than 0.")
    exit( )

#Monthly payment formula
a = (p * r / 1200.0) / (1 - (1.0 + r / 1200.0) ** (-12 * n))
print("Monthly payment is:" ,round(a, 1))







