#Create Student Name Analyzer

Students_Name= input("Enter your name: ")

#clean_student: stores the cleaned name by removing extra spaces and capitalizing the first letter of each word
clean_student = Students_Name.strip().title()
print(clean_student)