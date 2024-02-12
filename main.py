from random import randint

t = ["Rock", "Paper", "Scissors"]

while True:
    computer = t[randint(0,2)] #Used to select randomly some strings based on the list 't' from 0-1 range
    player = input("Rock, Paper, Scissors? ").capitalize() #First letter of the word is coverted to uppercase

    print("Computer picks:", computer)

    if player == computer:
        print("Tie!")
    elif player == "Rock": #nested if statements
        if computer == "Paper":
            print("You lose! ", computer, " covers ", player)
        else:
            print("You win! ", player, " smashes ", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose! ", computer, " cuts ", player)
        else:
            print("You win! ", player, " covers ", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose! ", computer, " smashes ", player)
        else:
            print("You win! ", player, " cuts ", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes": #It's a string coversion to lowercase for the input "yes" and it is placed in a break condition
        break
