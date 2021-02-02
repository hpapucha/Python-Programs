
# Open output file
fout = open("A.txt", "w")

#letter A using rows and columns 
for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or ((row==0 or row==3) and (col>0 and col<4)):
            fout.write("*")
        elif (col != 0 or col != 4) or((row != 0 or row != 3) and (col<0 and col<4)):
            fout.write(" ")
    fout.write("\n")

# Close output file.
fout.close( )

