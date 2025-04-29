# Gabriel Castaneda
# 04/07/2025
# P2HW2
# Grades

# Input: Read grades from user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

#Dictionary
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total /len(grades)

# Output
print("\n------------Results------------")
print(f"Lowest Grade:     {lowest}")
print(f"Highest Grade:    {highest}")
print(f"Sum of Grades:    {total}")
print(f"Average:          {average:.2f}")
print("--------------------------------")
 