# Gabriel Castaneda
# 04/05/2025
# P1HW2
# Travel Expenses

print("This program calculates and displays travel expenses")
print("\n")
# Get info from user
budget = int(input("Enter Budget: "))
print("\n")
destination = (input("Enter oyur travel destination: "))
print("\n")
gas = int(input("How much do you think you will spend on gas? "))
print("\n")
num1 = int(input("Approximately, how much will you need for accomodation/hotel? "))
print("\n")
num2 = int(input("Last, how much do you need for food? "))
print("\n")

#How much money you have left
print("-----Travel Expenses-----")
print("Location:", destination)
print("Enter Budget:", budget)
print("\n")
print("Fuel:", gas)
print("Accomodation:", num1)
print("Food:", num2)
print("\n")
print("Remaining Balance:", budget-gas-num1-num2)