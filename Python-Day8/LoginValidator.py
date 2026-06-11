#Create Login Validator

username = input("Enter Username:")
password = input("Enter Password:")

try:
    if password =="":
     raise Exception("Password cannot be empty")
    if username =="":
     raise Exception("Username cannot be empty")
    print("Login Successful")
except:
    print("Login Failed:")