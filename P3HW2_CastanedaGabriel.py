# Gabriel Castaneda
# 4/19/2025
# P3HW2
# Employee Payroll

# Get input from user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter the employee's pay rate: "))

# Variables
regular_hours = min(hours_worked, 40)
overtime_hours = max(0, hours_worked - 40)

# Calculate pay
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * pay_rate * 1.5
gross_pay = regular_pay + overtime_pay

# Display results
print("---------------------------------------------------------------------------")
print(f"Employee Name: {employee_name}")
print('\n')
print('Hours worked   Pay Rate   Overtime   Overtime Pay   RegHour Pay   Gross Pay')
print("---------------------------------------------------------------------------")
print(f'{hours_worked:<12}   {pay_rate:<8}   {overtime_hours:<8}   {overtime_pay:<12.2f}   ${regular_pay:<10.2f}   ${gross_pay:.2f}')