#Store and Read Student Marks
marks1 = input("Enter Mark 1: ")
marks2 = input("Enter Mark 2: ")
marks3 = input("Enter Mark 3: ")
marks4 = input("Enter Mark 4: ")
marks5 = input("Enter Mark 5: ")

with open("marks.txt", "w") as file:
    file.write(marks1 + "\n")
    file.write(marks2 + "\n")
    file.write(marks3 + "\n")
    file.write(marks4 + "\n")
    file.write(marks5 + "\n")

total = 0
with open("marks.txt", "r") as file:
 for line in file:
    print("Marks:", line.strip())
total = total + int(line)

print("Total Marks:", total)