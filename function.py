import random


def guess_the_number():
    secret_number = random.randint(1, 1000)

    attempts = 0

    print("Welcome to Guess The Number Game!")
    print("I'm thinking of a number between 1 and 1000. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


guess_the_number()
