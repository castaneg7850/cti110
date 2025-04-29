# Gabriel Castaneda
# 4/19.2025
# P3LAB3
# Amount of money

# Get valve from user
change= float(input("Enter the amount of money as a float: $"))
print(f'Change Amount: {change}')

# Converting the value to an integer
change = round(change * 100)
print(f'Change Amount: {change}')

# Determine how many coins are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickles = change // 5
change = change - (num_nickles * 5)

num_pennies = change

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")
if num_quarters > 0:
    if num_dollars == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")
if num_nickles > 0:
    if num_nickles == 1:
        print(f"{num_nickles} Nickle")
    else:
        print(f"{num_nickles} Nickles")
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")