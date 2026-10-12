# Number Guessing Game
# CodeOrbit Tech - Python Programming Internship

import random

while True:
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print("Congratulations! You guessed the number.")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")

    # Ask whether the user wants another round
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break