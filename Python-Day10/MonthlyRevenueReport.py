#Create Monthly Revenue Report using NumPy
import numpy as np

revenue = np.array([
    50000,
    55000,
    60000,
    65000,
    70000
])

#Analysis
print("Total Revenue:", np.sum(revenue))
print("Average Revenue:", np.mean(revenue))
print("Highest Revenue:", np.max(revenue))
print("Lowest Revenue:", np.min(revenue))