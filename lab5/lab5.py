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
        print()
        process()
        choice = input("Your choice? ")
        if choice.upper() == "Q":
            done = True
        elif choice.upper() == "E":
            print("Miles traveled: ", miles)
            print("Drinks in canteen: ", drink)
            print("The locals are ", -distance, " miles behind you.")
            print()
        elif choice.upper() == "D":
            print("You stop for the night.")
            print("Your camel is happy.")
            print("The locals don't stop.")
            print()
            camel_tiredless = 0
            distance += random.randrange(7, 14)
        elif choice.upper() == "C":
            full = random.randrange(10, 20)
            miles += full
            distance -= full
            distance += random.randrange(7, 14)
            thirst += 1
            camel_tiredless += random.randrange(1, 3)
            print("You trameled ", miles, " miles.")
        elif choice.upper() == "B":
            moderate = random.randrange(5, 12)
            miles += moderate
            distance -= moderate
            distance += random.randrange(7, 14)
            thirst += 1
            camel_tiredless += 1
            print("You trameled ", miles, " miles.")
        elif choice.upper() == "A":
            if drink > 0:
                thirst = 0
                drink -= 1
                print("You drank.")
            else:
                print("Error")






        if not done and thirst > 4 and thirst <= 6:
            print("You ard thirsty.")
        elif thirst > 6:
            print("You died of thirst.")
            done = True
            
        if not done and camel_tiredless > 5 and camel_tiredless <= 8:
            print("Your camel is getting tired.")
        elif camel_tiredless > 8:
            print("Your camel is dead.")
            done = True

        if not done and distance > -15 and distance < 0:
            print("The locals are getting close!")
        elif distance >= 0:
            print("You caught. You died.")
            done = True

        if not done and miles >= 200:
            print("You won!")
            done = True



if __name__ == '__main__':
    main()     


