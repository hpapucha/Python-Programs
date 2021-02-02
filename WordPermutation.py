#These are the two jumble words, five and six letters 
#nalun
#ruvedo
import itertools

#defining a permutations method that finds all of the permutations of a word
def get_permutations(input_string):
        letters = list(input_string)
        permutation_list = list(itertools.permutations(letters))
        permutations = [ ]
        for perm in permutation_list:
                permutations.append("".join(perm))
        return permutations

#user inputs a random string and the program compares it
#to a dictionary file and finds a matching word
input_string = input("Enter an input string: ")
perms = get_permutations(input_string)
fin = open("dict.txt", "r")
line = fin.readline( )
while line != "":
        word = line.strip()
        if word[0] == word[0].lower():
                for p in perms:
                        if word == p:
                                print(word)
        line = fin.readline()

#closing file        
fin.close()
