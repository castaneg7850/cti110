# Gabriel Castaneda
# 4/24/2025
# P4HW2
# Employee Pay


total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
    name = input('Enter employee\'s name or "Done" to terminate: ')
    if name.lower() == 'done':
        break

    hours = float(input(f'How many hours did {name} work? '))
    rate = float(input(f'What is {name}\'s pay rate? '))

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        regular_pay = 40 * rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * rate

    gross_pay = regular_pay + overtime_pay

    print('\nEmployee name:\t', name)
    print('\nHours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay')
    print('-------------------------------------------------------------------------------')
    print(f'{hours:.1f}\t\t{rate:.2f}\t\t{overtime_hours:.1f}\t\t{overtime_pay:.2f}\t\t${regular_pay:.2f}\t\t${gross_pay:.2f}\n')

    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

# Final summary output
print(f'Total number of employees entered: {total_employees}')
print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
print(f'Total amount paid for regular hours: ${total_regular_pay:.2f}')
print(f'Total amount paid in gross: ${total_gross_pay:.2f}')