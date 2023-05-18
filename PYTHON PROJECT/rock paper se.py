import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("TYPE ROCK/PAPER/SCISSORS OR Q TO QUIT: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picks", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("You lost!")
        computer_wins += 1

print("You won", str(user_wins) + " times.")
print("Computer won", str(computer_wins) + " times.")
print("GOODBYE! HAVE A NICE DAY")
