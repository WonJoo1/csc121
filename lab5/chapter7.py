a = 4
b = 5
c = 6

if a < b:
    print("a is less than b")

if a > b:
    print("a is greater than b")

if a <= b:
    print("a is less than or equal to b")

if a >= b:
    print("a is greater than or equal to b")

if a == b : 
    print("a is equal to b")
    
if a != b:
    print("a and b are not equal")

if a < b and a < c:
    print("a is less than b and c")

if a < b or a < c:
    print("a is less than either a or b (or both")

a = True
if a:
    print("a is Ture")

if not a:
    print("a is False")

a = True
b = False
if a and b:
    print("a and b are both true")

a = 3
b = 3
c = a == b
print(c)

if 1:
    print("1")

if "A":
    print("A")

if 0:
    print("Zero")

a = "c"     #a is True
if a == "B" or "b":
    print("a is equal to b. Maybe")

if a == "B" or a == "b":
    print("a is equal to b.")

temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
 
print("Done")

temperature = int(input("What is the temperature in Fahenheit? "))
if temperature > 90:
    print("It is hot outside")
else:
    print("It is not hot outside")
print("Done")

temperature = int(input("What is the temperature in Fahenheit? "))
if temperature > 90:
    print("It is hot outside")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is not hot outside")
print("Done")


temperature = int(input("What is the temperature in Fahenheit? "))
if temperature > 90 and temperature <= 110:
    print("It is hot outside")
elif temperature > 110:
    print("Oh man, you could fry eggs on the pavement!")
elif temperature < 30:
    print("It is cold outside")
else:
    print("It is ok outside")
print("Done")

user_name = input("What is your name? ")
if user_name =="Wonjoo":
    print("You have a nice name.")
else:
    print("Your name is ok.")