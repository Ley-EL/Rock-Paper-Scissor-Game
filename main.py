# Borno Kendley
# bornokendley@gmail.com
# instagram: @kendleyone

import random

print("Welcome to Rock-Paper-Scissors game\n")
print("Possibility: Rock-Paper-Scissors")

userScore = 0
computerScore = 0

Possibility = ["Rock", "Paper", "Scissor"]



def Play():
    global userScore
    global computerScore

    if userChoice == "Rock" and computerChoice == "Paper":
        print(f"Comuter choice: {computerChoice}")
        print("Computer won")
        computerScore += 1
        print(f"Score : You {userScore}-{computerScore} Computer\n")
    elif userChoice == "Rock" and  computerChoice == "Scissor":
        print(f"Comuter choice: {computerChoice}")
        print("You won")
        userScore += 1
        print(f"Score : You {userScore}-{computerScore} Computer\n")
    elif userChoice == "Paper" and computerChoice == "Rock":
        print(f"Comuter choice: {computerChoice}")
        print("You won")
        userScore += 1
        print(f"Score : You {userScore}-{computerScore} Computer\n")
    elif userChoice == "Paper" and computerChoice == "Scissor":
        print(f"Comuter choice: {computerChoice}")
        print("Computer won")
        computerScore += 1
        print(f"Score : You {userScore}-{computerScore} Computer\n")
    elif userChoice == "Scissor" and computerChoice == "Rock":
        print(f"Comuter choice: {computerChoice}")
        print("Computer won")
        computerScore += 1
        print(f"Score : You {userScore}-{computerScore} Computer\n")
    elif userChoice == "Scissor" and computerChoice == "Paper":
        print(f"Comuter choice: {computerChoice}")
        print("You won")
        userScore += 1
        print(f"Score : You {userScore}-{computerScore} Computer\n")
    else:
        print(f"Comuter choice: {computerChoice}")
        print("Same")
        print(f"Score : You {userScore}-{computerScore} Computer\n")

        
while (userScore or computerScore) != 3:
    userChoice = input("Make your choice: ")
    computerChoice = random.choice(Possibility)
    Play()

    if(userScore == 2 and computerScore == 0) :
        print("You are the winner")
        break
    elif computerScore == 2 and userScore == 0 :
        print("Computer is the winner")
        break

if (userScore or computerScore) == 3:
    if (userScore > computerScore) :
        print("You are the winner")
    else :
        print("Computer is the winner")