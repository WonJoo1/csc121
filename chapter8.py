def print_about_gum(repetitions):
    for i in range(repetitions):
        print("I will not chew gum in class.")

def main():
    print_about_gum(10)

main()

for i in range(2, 12, 2):
    print(i)

for i in range(5):
    print((i + 1) * 2)

mile_traveled = 0
done = False
while not done:
    choice = input('Choice? ')
    if choice == 'A':
        mile_traveled += 10
    if mile_traveled > 50:
        done = True

total = 0
for i in range(5):
    new_number = int(input("Enter a number: "))
    total = total + new_number
print("The total is: ", total)

for i in range(1, 101):
    total = total + i
print(total)

value = 0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)

while Ture:
    quit = input("Do you want to quit? ")
    if quit == 'y':
        break
    attack = input("Does your elf attack the dragon? ")
    if attack == 'y':
        print("Bad choice, you died.")
        break