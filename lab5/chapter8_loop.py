i = 1
while i <= 2 ** 32:
    print(i)
    i *= 2

'''
quit = "n"
while quit == "n":
    quit = input("Do you want to quit? ")

done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True

    attack = input("Does your elf attack the dragon?")
    if attack == "y":
        print("Bad choice, you died.")
        done = True
'''

i = 0
while i < 10:
    print(i)
    i = i + 1

while True:
    quit = input("Do you want to quit? ")
    if quit == "y":
        break
    
    attack = input("Does your elf attack the dragon? ")
    if attack == 'y':
        print("Bad choice, you died.")
        break