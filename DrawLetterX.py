# Open output file
fout = open("X.txt", "w")

#letter X using rows and columns and variables
a = 0
b = 9
for row in range (10):
    for col in range(10):
        if row==a and col==b:
            fout.write("*")
            a=a+1
            b=b-1
        elif row==col:
            fout.write("*")
        else:
            fout.write(" ")
    fout.write("\n")
    
# Close output file.
fout.close( )
