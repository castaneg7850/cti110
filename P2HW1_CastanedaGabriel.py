# Gabriel Castaneda
# 04/07/2025
# P1HW2
# Travel Expenses

print("This program calculates and displays travel expenses")
print("\n")
# Get info from user
budget = float(input("Enter Budget: "))
print("\n")
destination = input("Enter your travel destination: ")
print("\n")
gas = float(input("How much do you think you will spend on gas? "))
print("\n")
num1 = float(input("Approximately, how much will you need for accomodation/hotel? "))
print("\n")
num2 = float(input("Last, how much do you need for food? "))
print("\n")

#How much money you have left
print("-----Travel Expenses-----")
print(f'Loaction:            {destination}')
print(f'Initial Budget:      ${budget:.2f}')
print(f'Fuel:                ${gas:.2f}')
print(f'Accomodation:        ${num1:.2f}')
print(f'Food:                ${num2:.2f}')
print("-------------------------")
print("\n")
print(f'Remaining Balance:   ${budget-gas-num1-num2:.2f}')