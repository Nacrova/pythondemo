from random import randint
choice = randint(1,3)
if (choice == 1):
    computer = "rock"
if (choice == 2):
    computer = "scissors"
if (choice == 3):
    computer = "paper"
move = (raw_input("Choose your move: "))
if move == "rock" and computer == "paper":
    print("You lose, computer chose paper.")
if move == "rock" and computer == "scissors":
    print("You win, computer chose scissors.")
if move == "rock" and computer == "rock":
    print("You tied, computer chose rock.")
if move == "paper" and computer == "paper":
    print("You tied, computer chose paper.")
if move == "paper" and computer == "rock":
    print("You win, computer chose rock.")
if move == "paper" and computer == "scissors":
    print("You lose, computer chose scissors.")
if move == "scissors" and computer == "paper":
    print("You win,computer chose paper.")
if move == "scissors" and computer == "rock":
    print("You lose, computer chose rock.")
if move == "scissors" and computer == "scissors":
    print("You tied, computer chose scissors.")
else:
    print("Please choose rock, paper, or scissors.")