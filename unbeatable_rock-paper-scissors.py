import time

options = ("rock", "paper", "scissors")

play_again_option = ("y", "n")

running = True

lose = 0

print("Welcome to the Rock-Paper-Scissors-Game")

while running:

    player = None
    computer = None


    while player not in options:
        
            player = input("Enter a Option: ").lower()

    if player == "rock":
        computer = "paper"
    elif player == "scissors":
        computer = "rock"
    elif player == "paper":
        computer = "scissors"

    print(f"Player: {player}")

    print(f"Computer: {computer}")

    time.sleep(0.5)

    print("You Lose!!!!")
    lose = lose + 1


    print(f"\nWins: 0\nLoses: {lose}\nNo Winner: 0")

    play_again = None

    while play_again not in play_again_option:
        play_again = input("Play agin? (y/n): ").lower()
        if play_again == "n":
            running = False
        elif play_again == "y":
            running = True
        else:
            print("Not an Option!!!!!!!!!!!!!")

print("Thanks for playing ")