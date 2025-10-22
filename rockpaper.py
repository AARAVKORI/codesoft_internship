import random

print("🎮 Welcome to Rock, Paper, Scissors Game! 🎮")
print("Rules:")
print("Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.")
print("Let's begin!\n")

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # Step 1: Get user input
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Step 2: Validate input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.\n")
        continue

    # Step 3: Computer randomly chooses
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    # Step 4: Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win this round! 🎉")
        user_score += 1
    else:
        print("Computer wins this round! 🤖")
        computer_score += 1

    # Step 5: Display current scores
    print(f"Score => You: {user_score} | Computer: {computer_score}\n")

    # Step 6: Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! Final Scores:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Goodbye! 👋")
        break
