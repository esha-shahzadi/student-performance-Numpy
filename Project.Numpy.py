#project:
import numpy as np

# Student marks
marks = np.array([
    [70, 55, 60, 80],
    [45, 90, 65, 72],
    [80, 40, 75, 91],
    [52, 67, 49, 80],
    [95, 85, 85, 60]
])

print(" STUDENT PERFORMANCE ANALYSIS  ")

# Complete marks table
print("\nMarks:")
print(marks)

# First student
print("\nFirst Student:")
print(marks[0])

# First two students
print("\nFirst Two Students:")
print(marks[:2])

# Highest mark
print("\nHighest Mark:")
print(np.max(marks))

# Lowest mark
print("\nLowest Mark:")
print(np.min(marks))

# Average
print("\nAverage Mark:")
print(np.mean(marks))

# Pass / Fail
print("\nPass / Fail:")
print(np.where(marks >= 50, "Pass", "Fail"))

# Sorted marks
print("\nSorted Marks:")
print(np.sort(marks, axis=None))