#Handle ValueError
try:
    age = int(input("Enter your Age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid age")