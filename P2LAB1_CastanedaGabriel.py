# Gabriel Castaneda
# 04/07/2025
# P2LAB1
# Circle Formulas

import math
#Get radius user
radius = float(input("What is the radius of the circle? "))

#Calculate circum, diameter, area
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#Display the results
print(f"The diameter of the circle is {diam:.1f}")
print(f"The circumference of the circle is {cir:.2f}")
print(f"The area of the circle is {area:.3f}")