import random

#while prompt == "Y"

def rockPaperScissors(userinput, computerinput):
    if((userinput == "rock") & (computerinput == "rock")):
       print("The computer threw rock. Rock and Rock ends in a draw.")
    elif((userinput == "Scissors") & (computerinput == "Scissors")):
        print("The computer threw scissors, scissors and scissors ends in a draw.")
    elif((userinput == "paper") & (computerinput == "paper")):
        print("The computer threw paper, paper and paper ends in a draw.")

    elif((userinput == "rock") & (computerinput == "scissors")):
        print("The computer threw scissors. Rock versus scissors, you win!")
    elif((userinput == "scissors") & (computerinput == "paper")):
        print("The computer threw paper, scissors versus paper, you win!")
    elif((userinput == "paper") & (computerinput == "rock")):
        print("The computer threw rock, paper versus rock, you win!")

    elif((userinput == "rock") & (computerinput == "paper")):
        print("The computer threw paper. Paper beats rock, computer wins!")
    elif((userinput == "paper") & (computerinput == "scissors")):
        print("The computer threw scissors. Scissors beats paper, computer wins!")
    elif((userinput == "scissors") & (computerinput == "rock")):
        print("The computer threw rock. Rock beats scissors, computer wins!")

rock = "rock"
paper = "paper"
scissors = "scissors"

list = [rock, paper, scissors]
computer = random.choice(list)

response = input("Do you want to play rockPaperScissors? 'Y' for yes, any other button for no: ").upper()
while response == "Y":
    user = input("Rock Paper. Scissors. Shoot!: "). lower()
    computer = random.choice(list)
    rockPaperScissors(user,computer)
    response = input("Do you want to play again? 'Y' for yes, anything else for no: ").upper()

                 
