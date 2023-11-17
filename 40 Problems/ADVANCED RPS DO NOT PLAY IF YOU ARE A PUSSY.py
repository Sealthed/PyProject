import random

def play_rock_paper_scissors(ai_move, player_move):
    # Convert player's move to lowercase
    player_move = player_move.lower()

    # Check if both moves are valid
    if player_move not in ["rock", "paper", "scissors"]:
        print("Invalid player move. Please enter 'rock', 'paper', or 'scissors'.")
        return False

    # Determine the winner
    if ai_move == player_move:
        winner = "tie"
    elif ai_move == "rock" and player_move == "paper":
        winner = "player"
    elif ai_move == "rock" and player_move == "scissors":
        winner = "ai"
    elif ai_move == "paper" and player_move == "rock":
        winner = "ai"
    elif ai_move == "paper" and player_move == "scissors":
        winner = "player"
    elif ai_move == "scissors" and player_move == "rock":
        winner = "player"
    elif ai_move == "scissors" and player_move == "paper":
        winner = "ai"

    # Print the results
    if winner == "ai":
        print(f"AI chose: {ai_move}")
        print("AI wins!")
    elif winner == "player":
        print(f"AI chose: {ai_move}")
        print("Player wins!")
    else:
        print(f"AI chose: {ai_move}")
        print("It's a tie!")

    return winner

# Initialize the AI's move
ai_move = random.choice(["rock", "paper", "scissors"])
previous_winner = None

while True:
    # Get the player's move
    player_move = input("Enter your move (Rock, Paper, Scissors)"
                        " or type 'quit' to stop: ")

    # Play the game and determine the winner
    winner = play_rock_paper_scissors(ai_move, player_move)

    # Update the AI's strategy based on the outcome
    if winner == "ai":
        ai_move = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }[ai_move]
    elif winner == "player":
        ai_move = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }[ai_move]
    else:
        # It's a tie, so randomly choose a new move
        ai_move = random.choice(["rock", "paper", "scissors"])

    # Check if the player wants to quit
    if player_move.lower() == "quit":
        break
