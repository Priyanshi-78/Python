#Create Student Registration System
name = input("Enter Student Name: ")
age = input("Enter Student Age: ")
college = input("Enter College Name: ")
Course = input("Enter Course Name: ")
roll_no = input("Enter Roll Number: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.write("College: " + college + "\n")
file.write("Course: " + Course + "\n")
file.write("Roll Number: " + roll_no + "\n")

file.close()
