# Gabriel Castaneda
# 04/07/2025
# P2LAB2
# Using dictionary

cars = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26  }

#Get keys from dict
cars_keys = cars.keys()

print(cars_keys)

#Get a car from user
car_name = input("Enter a vehicle to see it's mpg: ")

#Get mpg for the given car
car_mpg = cars [car_name]
print(f"The {car_name} gets {car_mpg} mpg.")

#Get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#Calculate how many gallons
gallons_needed = miles_driven/car_mpg

#Results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles.")
