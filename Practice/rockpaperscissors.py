from random import randint

#create a list
game = ["Rock", "Paper", "Scissors"]
#create computer choices
computer = game[randint(0,2)]

#set player to false
player = False

while player == False:
    #set player to true
    print("Rock(R), Paper(P), Scissors(S)? or Quit(Q)")
    player = input("")
    if player == "Q":
        exit()
    if player == computer:
        print("It is a tie!!")
    elif player == "R":
        if computer == "Paper":
            print("You Lose!!")
        else:
            print("You Win!!")
    elif player == "P":
        if computer == "Scissors":
            print("You Lose!!")
        else:
            print("You Win!!")
    elif player == "S":
        if computer == "Rock":
            print("You Lose!!")
        else:
            print("You Win!!")
    else:
        print("Invalid Option, Try Again... ")
    player = False
    computer = game[randint(0,2)]
