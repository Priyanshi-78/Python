#Create Sales Data Cleaner
sales = ["8000", "10000", "Priyanshi", "20000"]
total = 0

for item in sales:
    try:
        total += int(item)
    except ValueError:
     print("Data Of invalid sales:", item)

print("Total Sales data:", total)