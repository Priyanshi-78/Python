#Create Student Marks Analyzer
import numpy as np
#Marks Data:
marks = np.array([
78,
85,
92,
88,
76,
95
])
#Analysis:
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Total Marks:", np.sum(marks))