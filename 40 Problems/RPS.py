import random

play_again = input("Enter y to play rock paper scissors: ")

while play_again == "y":

    user = input("Enter a choice (Rock, Paper, Scissors): ")

    possible_actions = ["Rock", "Paper", "Scissors"]
    computer = random.choice(possible_actions)

    print(f"\nYou chose {user}, and the computer chose {computer}")

    if user == computer:
        print(f"Both players select {user}. It's a tie!")
    elif user == "Rock":
        if computer == "Scissors":
            print("Rock smashes scissors, You Win!")
        else:
            print("Paper covers rock, You Lose!")
    elif user == "Scissors":
        if computer == "Paper":
            print("Scissors cut paper, You Win!")
        else:
            print("Rock crushes scissors, You Lose!")
    elif user == "Paper":
        if computer == "Rock":
            print("Paper covers rock,, You Win!")
        else:
            print("Rock smashes scissors, You Lose!")
    play_again = input("Enter 'y' to play again: ")
