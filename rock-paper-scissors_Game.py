import random

options = ("rock", "paper", "scissors")

play_again_option = ("y", "n")

running = True

print("Welcome to the Rock-Paper-Scissors-Game")

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a Option: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")


    if player == computer:
        print("No Winner!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    else:
        print("You Lose!")

    play_again = None

    while play_again not in play_again_option:
        play_again = input("Play agin? (y/n): ").lower()
        if play_again == "n":
            running = False

print("Thanks for playing ")