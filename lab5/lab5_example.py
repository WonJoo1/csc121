import random

def print_intro():
    print("Welcome to Camel!\n")
    print("In your desperation, you have stolen a camel to make your way")
    print("across the great Mobi desert.")
    print("The locals want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the locals.")


def process():
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")


def main():
    print_intro()

    done = False

    miles = 0
    thirst = 0
    camel_tiredless = 0
    distance = -20
    drink = 3

    while not done:
        process()
        user_choice = ['A', 'B', 'C', 'D', 'E']
        choice = input("Your choice? ") 
        
        if distance != 0:
            if choice == "A":
                if drink != 0:
                    drink -= 1
                    thirst = 0
                    print("Miles traveled: ", miles)  
                    print("Drinks in canteen: ", drink)
                else:
                    print("You don't have drink")
            elif choice == "B":
                moderate = random.randrange(5, 12)
                thirst += 1
                camel_tiredless += 1
                miles += moderate
                distance -= moderate
                distance += random.randrange(7, 14)
                print("Miles traveled: ", miles)

            elif choice == "C":
                full = random.randrange(10, 20)
                thirst += 1
                camel_tiredless += random.randrange(1, 3)
                miles += full
                distance -= full
                distance += random.randrange(7, 14)
                print("Miles traveled: ", miles)

            elif choice == "D":
                camel_tiredless = 0
                print("The camel is happy.")
                distance += random.randrange(7, 14)
                print("Miles traveled: ", miles)

            elif choice == "E":
                print("Miles traveled: ", miles)
                print("Drinks in canteen: ", drink)
                print("The locals are ", -distance, " miles behind you.")
                

        else:
            done = True 
    






if __name__ == '__main__':
    main()

