# importing the random module 
import random

secret_number = random.randint(1,10)

max_attempts = 3

# function to display a welcome message
def welcome_message():
    print("\n Welcome to the Number Guessing Game!")
    print(f"You haave {max_attempts} attempts to the guess the correct number. ")

# display for revurive guessing 
def guess_recursive (attempts_left):
    guess = int(input("\n Guess the number (between 1 to 10): "))

    if guess == secret_number:
        print("congratulations! You guessed the correct number!")
    else:
        print(f"Wrong guess. Attempts left: {attempts_left - 1}")
        if attempts_left >1:
            guess_recursive(attempts_left - 1)
        else:
            print(f"Sorry, you couldn't guess the number. the correct number was {secret_number}.")

welcome_message()
guess_recursive(max_attempts)

print (f"Memory address of secret number {secret_number} is: {id(secret_number)}")
