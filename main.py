import random

attempts = 6


def display_rules():
    print("Welcome to Rock, Paper, Scissors!\n")
    print("Choose rock, paper, or scissors.")
    print(f"You have {attempts} rounds to play.\n")


def play_game(attempt=1, point=0, c_point=0):
    if attempt > attempts:
        print("\nGame Over!")

        if point > c_point:
            print("Congratulations! You won the game!")
        elif c_point > point:
            print("Computer won the game!")
        else:
            print("The game is a tie!")

        print(f"Final score: You {point} - {c_point} Computer")
        return

    guess = input(
        f"Round {attempt}/{attempts} - Enter your choice: "
    ).lower().strip()

    if guess not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.\n")
        return play_game(attempt, point, c_point)

    choice = random.choice(["rock", "paper", "scissors"])

    print("You chose:", guess)
    print("Computer chose:", choice)

    check_winner = lambda player, computer: (
        "Tie" if player == computer else
        "Player wins" if (
            (player == "rock" and computer == "scissors") or
            (player == "paper" and computer == "rock") or
            (player == "scissors" and computer == "paper")
        ) else "Computer wins"
    )

    result = check_winner(guess, choice)

    if result == "Tie":
        print("It's a tie! No points awarded.")
    elif result == "Player wins":
        point += 1
        print("You win this round!")
    else:
        c_point += 1
        print("Computer wins this round!")

    print(f"Score: You {point} - {c_point} Computer\n")

    play_game(attempt + 1, point, c_point)


# Start the game
display_rules()
play_game()
