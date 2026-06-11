#Create calculator using conditions

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

operator = input("Enter operation (+, -, *, /) ")

if operator == "+":
    print(number1 + number2)

elif operator == "-":
    print(number1 - number2)

elif operator == "*":
    print(number1 * number2)

elif operator == "/":
    print(number1 / number2)

else:
    print("Invalid Operation")