import random
#Python module

userWins = 0
compWins = 0

choicesList = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors! Your goal is to beat the computer. Remember: Rock beats Scissors, Paper beats Rock, and Scissors beat Paper.")

print("")

while True:
    userChoice = input("Enter in rock, paper, or scissors as your choice. Enter in 'end' if you wish to finish the game.")
    
    if userChoice == "end":
        break

    elif userChoice not in choicesList:
        print("Oops! Please choose either 'rock', 'paper', 'scissors', or 'end' in lowercase please.")
        continue 

    randomNum = random.randint(0,2)
    #0 = rock     1 = paper     2 = scissors
    comChoice = choicesList[randomNum]
    print("Computer chose: ", comChoice) 

    if userChoice == "rock" and comChoice == "scissors":
        print("You win!")
        userWins += 1

    elif userChoice == "paper" and comChoice == "rock":
        print("You win!")
        userWins += 1

    elif userChoice == "scissors" and comChoice == "paper":
        print("You win!")
        userWins += 1

    elif userChoice == comChoice:
        print("Tie!")

    else:
        print("You lose!")
        compWins += 1 

print("You won", userWins, "games.")
print("The computer won", compWins, "games.")

print("")

print("See you later!") 