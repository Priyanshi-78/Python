#Create Student Class
class Student:
 def __init__(self, name, marks, roll_no):
  self.name = name
  self.marks = marks
  self.roll_no = roll_no

def display(self):
 print("Student Name:", self.name)
 print("Student Marks:", self.marks)
 print("Student Roll_No:", self.roll_no)

student1 = Student("Priyanshi", 95, 101)
student2 = Student("Shambhavi", 88, 102)
student3 = Student("Ritika", 91, 103)

student1.display()
student2.display()
student3.display()