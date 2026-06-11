#Create Username Formatter
Username = input("Enter your username: ")

#f:: "stores the value of the variable in the string"
#Print the original username
print(f"Original Username: {Username}")
#lower: converts all letters to lowercase
print(f"Lowercase: {Username.lower()}")
#Uppercase: Converts all letters to uppercase
print(f"Uppercase: {Username.upper()}")
#title: first letter of each word is capitalized
print(f"Title Case: {Username.title()}")
#strip: removes all the extra spaces
print(f"Without any Space: {Username.strip()}")

