# Gabriel Castaneda
# 4/26/2025
# P4LAB2
# Use while and for loop together

run_again = 'yes'
while run_again != "no":
    user_num = int(input("Enter an integer: "))
    if user_num >= 0:
        for item in range(1, 13):
            print (f"{user_num} * {item} = {user_num * item}")
    else:
        print ("This program does not handle negative values")
    run_again = input("Would you run the program again? ")

print("Exiting program....")