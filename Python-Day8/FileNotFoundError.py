# Handle FileNotFoundError

try:
    file = open("student.txt")
    print(file.read())
except FileNotFoundError:
    print("File not found")