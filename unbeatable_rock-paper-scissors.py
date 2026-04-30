import time

options = ("rock", "paper", "scissors")

play_again_option = ("y", "n")

running = True

win = 0

lose = 0

no_winner = 0

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

    time.sleep(1.5)
    if player == computer:
        print("No Winner!!!!")
        no_winner = no_winner + 1
    elif player == "rock" and computer == "scissors":
        print("You Win!!!!")
        win = win + 1
    elif player == "scissors" and computer == "paper":
        print("You Win!!!!")
        win = win + 1
    elif player == "paper" and computer == "rock":
        print("You Win!!!!")
        win = win + 1
    else:
        print("You Lose!!!!")
        lose = lose + 1







    print(f"\nWins: {win}\nLoses: {lose}\nNo Winner: {no_winner}")

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