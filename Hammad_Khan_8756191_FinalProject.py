import random

userWins = 0
compWins = 0

choicesList = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors! Your goal is to beat the computer. Remember: Rock beats Scissors, Paper beats Rock, and Scissors beat Paper.")

while True:
    userChoice = input("Enter in Rock, Paper, or Scissors. Enter in 'end' to finish the game. ")
    
    if userChoice == "end":
        break

    elif userChoice not in choicesList:
        print("Oops! Please choose either rock, paper, or scissors please.")
        continue 

    randomNum = random.randint(0,2)
    comChoice = choicesList[randomNum]
    print("Computer chose: ", comChoice) 

    if userChoice == "Rock" and comChoice == "Scissors":
        print("Rock beats Scissors")
        userWins += 1

    elif userChoice == "Paper" and comChoice == "Rock":
        print("Paper beats Rock")
        userWins += 1

    elif userChoice == "Scissors" and comChoice == "Paper":
        print("Scissors beats Paper")
        userWins += 1

    else:
        print(comChoice, "beats", userChoice)
        compWins += 1 
