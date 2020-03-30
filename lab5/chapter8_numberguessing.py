import random

def main():
    print("Hi, I'm thinking of a random number betwenn 1 and 100")

    secret_number = random.randrange(1, 101)

    user_attempt_number = 1

    user_guess = 0

    while user_guess != secret_number and user_attempt_number < 8:
        print("---Attempt", user_attempt_number)
        user_input_text = input("Guess what number I am thinking of: ")
        user_guess = int(user_input_text)

        if user_guess > secret_number:
            print("Too high.")
        elif user_guess < secret_number:
            print("Too low.")
        else:
            print("You got it!")
        
        user_attempt_number += 1

    if user_guess != secret_number:
        print("Aw, you ran out of tries. The number was " + str(secret_number) + ".")

main()