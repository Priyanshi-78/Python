#Create Sales Analysis Program
import numpy as np

# Monthly Sales
sales = np.array([
    10000,
    12000,
    15000,
    18000,
    22000
])

# Calculations
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))