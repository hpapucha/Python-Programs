#Rock Paper Scissor Game

import random
human_score = 0.0
computer_score = 0.0


while True:
    

#Human inputs the words rock/paper/scissors     
    human_play = input("Input 'rock', 'paper' or 'scissors' to play: ")
    random_number = random.randrange(0, 3)

#The computer plays rock/paper/scissors based on their number assignment
    if random_number == 0:
        computer_play = "rock"
    elif random_number == 1:
        computer_play = "paper"
    else:
        computer_play = "scissors"


#These 3 if statements show all of the tie results that add 0.5 score
#both to computer and human
    if human_play == "rock" and computer_play == "rock":
        print ("Computer plays rock.")
        print ("The result is tie")
        computer_score = computer_score + 0.5
        human_score = human_score + 0.5
    elif human_play == "paper" and computer_play == "paper":
        print ("Computer plays paper")
        print ("The result is tie")
        computer_score = computer_score + 0.5
        human_score = human_score + 0.5
    elif human_play == "scissors" and computer_play == "scissors":
        print ("Computer plays scissors")
        print ("The result is tie")
        computer_score = computer_score + 0.5
        human_score = human_score + 0.5

#All of the rock paper and scissor combinations
    if human_play == "rock" and computer_play == "paper":
        print("Computer plays paper. Paper covers rock.")
        print("Computer wins")
        computer_score = computer_score + 1.0
    elif human_play == "rock" and computer_play == "scissors":
        print("Computer plays scissors. Rock crushes scissors.")
        print("Human wins")
        human_score = human_score + 1.0
    elif human_play == "scissors" and computer_play == "paper":
        print("Computer plays paper. Scissors cut paper.")
        print("Human wins")
        human_score = human_score + 1.0
    elif human_play == "scissors" and computer_play == "rock":
        print("Computer plays rock. Rock crushes scissors.")
        print("Computer wins")
        computer_score = computer_score + 1.0
    elif human_play == "paper" and computer_play == "rock":
        print("Computer plays rock. Paper covers rock.")
        print("Human wins")
        human_score = human_score + 1.0
    elif human_play == "paper" and computer_play == "scissors":
        print("Computer plays scissors. Scissors cut paper.")
        print("Computer wins")
        computer_score = computer_score + 1.0
    print ("Computer score is:", computer_score)
    print ("Human score:", human_score)



   
