import random

def get_computer_choice():
    """Randomly choose between rock, paper, or scissors."""
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    """Prompt user to enter a valid choice."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("❌ Invalid choice. Please try again.")

def determine_winner(user, computer):
    """Determine the winner of a round."""
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    """Play multiple rounds of the game."""
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("You vs Computer - Let's begin!\n")

    while True:
        print(f"--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n🧍‍♂️ You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        print(f"\n🏆 Score: You {user_score} - {computer_score} Computer")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("\n🎯 Final Score:")
            print(f"🧍‍♂️ You: {user_score}")
            print(f"💻 Computer: {computer_score}")
            print("\nThanks for playing! 👋")
            break

        round_number += 1
        print()

# Run the game
play_game()