import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
    continue

    player_number = int(player_input)

if player_number == computer_number:
    print("You guess it!")


elif player_number > computer_number:
    print("Too high!")
else:
    print("Too low!")
