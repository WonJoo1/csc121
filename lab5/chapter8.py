for i in range(3):
    print("a")
    for j in range(3):
        print("b")
print("Done")

total = 0
for i in range(5):
    new_number = int(input("Enter a number: "))
    total = total + new_number
print("The total is: ", total)

total_sub = 0
for i in range(5):
    new_number = int(input("Enter a number: "))
    if new_number == 0:
        total_sub += 1
print("You entered a total of", total_sub, "zeros")

for i in range(10):
    print("Hi")

for i in range(5):
    print("Hello")
print("There")

for i in range(5):
    print("Hello")
    print("There")

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(10):
    print(i + 1)

for i in range(2, 12, 2):
    print(i)

for i in range(5):
    print((i + 1) * 2)

for i in range(10, 0, -1):
    print(i)

for i in [2, 6, 4, 2, 4, 6, 7, 400]:
    print(i)

for i in range(3):
    print("a")
    for j in range(3):
        print("b")

a = 0
for i in range(10):
    a = a + 1
print(a)

a = 0
for i in range(10):
    a = a+1
for i in range(10):
    a = a+1
print(a)

a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)

sum = 0
for i in range(1, 101):
    sum = sum = i
print(sum)