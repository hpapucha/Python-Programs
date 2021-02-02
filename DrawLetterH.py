# LetterH Example
# Draw the letter H using asterisks

# Open output file
fout = open("h.txt", "w")

# Draw diagonal right>left
for y in range(0, 13):
    for x in range(0, 13 - y):
        fout.write(" ")
    for x in range(0, 3):
        fout.write("*")
    fout.write("\n")

# Draw diagonal left>right
for y in range(0, 13):
    for x in range(0, 0 + y):
        fout.write(" ")
    for x in range(0, 3):
        fout.write("*")
    fout.write("\n")

#letter A
for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or ((row==0 or row==3) and (col>0 and col<4)):
            fout.write("*")
        elif (col != 0 or col != 4) or((row != 0 or row != 3) and (col<0 and col<4)):
            fout.write(" ")
    fout.write("\n")



#letter X version 2
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
