#Create Email Validator
Email = input("Enter your email address: ")
if Email.endswith("@gmail.com") or Email.endswith("@abcd.com") or Email.endswith("@xyzx.com"):
    print("Valid email address")
else:
    print("Invalid email address")