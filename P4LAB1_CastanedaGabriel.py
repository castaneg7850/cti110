# Gabriel Castaneda
# 4/24/2025
# P4LAB1
# Use turtle

import turtle

win = turtle.Screen()
pen = turtle.Turtle()

pen.pensize(3)
pen.pencolor("purple")
pen.shape("turtle")

for side in range(4):
    pen.forward(100)
    pen.left(90)
    
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

win.mainloop()