#Create function to check even/odd
def check_even_odd(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

print(check_even_odd(22))