import random
import os


def computerPlay() -> str:
    moves = ['rock', 'paper', 'scissors']
    randomMove = random.choice(moves)
    return randomMove

def getInputFromPlayer() -> str:
    playerSelection = ""
    validInput = False
    while validInput == False:
        playerInput = input("enter move: (r)ock, (p)aper or (s)cissors \n")
        if playerInput == "r":
            playerSelection = "rock"
            validInput = True
        elif playerInput == "p":
            playerSelection = "paper"
            validInput = True
        elif playerInput == "s":
            playerSelection = "scissors"
            validInput = True
        else:
            print("Not a valid option, try again!")
    return playerSelection


def evaluateGame(playerSelection: str, computerSelection: str) -> str:
    if playerSelection == computerSelection:
        print("It's a tie!")
        return "tie"
    elif playerSelection == "scissors" and computerSelection == "rock":
        print("rock beats scissors, you lose!")
        return "lose" 
    elif playerSelection == "scissors" and computerSelection == "paper":
        print("scissors beats paper, you win!")
        return "win"
    elif playerSelection == "rock" and computerSelection == "scissors":
        print("rock beats scissors, you win!")
        return "win"
    elif playerSelection == "rock" and computerSelection == "paper":
        print("paper beats rock, you lose!")
        return "lose"
    elif playerSelection == "paper" and computerSelection == "scissors":
        print("scissors beats paper, you lose!")
        return "lose"
    elif playerSelection == "paper" and computerSelection == "rock":
        print("paper beats rock, you lose!")
        return "lose"


def game():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("##### Rock  Paper  Scissors #####")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    rounds = 0
    wins = 0
    loses = 0
    ties = 0
    while rounds < 5:
        computerSelection = computerPlay()
        playerSelection = getInputFromPlayer()
        result = evaluateGame(playerSelection, computerSelection)
        if result == "win":
            wins += 1
        elif result == "lose":
            loses += 1
        elif result == "tie":
            ties += 1
        rounds += 1
        print("round "+ str(rounds) +"/5.\n")
    os.system('cls')
    print("\n~~~~~~~~~~~~~~~~~~~~")
    print("End of the game")
    print("wins: ", wins)
    print("loses: ", loses)
    print("ties: ", ties)
    print("Thanks for playing")
    print("~~~~~~~~~~~~~~~~~~~~~")

if __name__ == '__main__':
    game()
