#Create Sales Data Analyzer

sale1 = input("Enter Sale 1: ")
sale2 = input("Enter Sale 2: ")
sale3 = input("Enter Sale 3: ")
sale4 = input("Enter Sale 4: ")
sale5 = input("Enter Sale 5: ")

# Write Data
with open("sale.txt", "w") as file:
    file.write(sale1 + "\n")
    file.write(sale2 + "\n")
    file.write(sale3 + "\n")
    file.write(sale4 + "\n")
    file.write(sale5 + "\n")

# Read Data
total = 0

with open("sale.txt", "r") as file:
 for line in file:
  print("line:", line.strip())
total = total + int(line)
print("Total Sales:", total)