import random

options = ("rock","paper", "scissors")

playing = True

while playing:

    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Entre your choice(rock,paper,scissors)")

    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "paper " and computer == "rock":
        print("you win!")
    elif player == "rock" and computer == "scissors":
        print("you win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")
    else :
        print("you loose !")
    if not input("play agin? (y/n):").lower() == "y":
        playing = False


print("Thanks for playing")


