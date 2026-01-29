import random
print("Welcome to Rock Paper Scissor developed by Monty")

choices = ["rock","paper","scissor"]
while True:
    user_choice = input("Enter rock,paper or scissor (or 'exit' to quit):").lower()

    if user_choice == "exit":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer choose:{computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif(user_choice == "rock" and computer_choice == "scissor") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissor" and computer_choice == "paper"):
        print("You Win!")
    else:
        print("You Loose!")
