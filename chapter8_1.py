import random

def main():
    print("Hi! I'm thinking of a random number between 1 and 100")

    secret_number = random.randrange(1, 101)

    user_attempt_number = 1

    user_guess = 0

    while user_guess != secret_number and user_attempt_number < 8:
        