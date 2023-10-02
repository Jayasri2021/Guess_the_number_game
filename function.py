import random


def gtn():
    sec_num = random.randint(1, 1000)

    no_of_tries = 0

    print("Welcome to Guess The Number Game!")
    print("I'm thinking of a number between 1 and 1000. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        no_of_tries += 1

        if user_guess < sec_num:
            print("Too low! Try again.")
        elif user_guess > sec_num:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", no_of_tries, "tries.")
            break
