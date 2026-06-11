#Create Calculator with Exception Handling

try:
    number1 = float(input("Enter the First Number: "))
    number2 = float(input("Enter the Second Number: "))

    print("Addition:", number1 + number2)
    print("Subtraction:", number1 - number2)
    print("Multiplication:", number1 * number2)
    print("Division:", number1 / number2)

except ZeroDivisionError:
    print("Number cannot be divided by zero")

except ValueError:
    print("Please enter a valid numbers")