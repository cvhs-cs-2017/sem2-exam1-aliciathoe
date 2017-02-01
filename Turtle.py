"""Create a Turtle Program that will draw a 3-dimensional cube"""


import turtle
sven = turtle.Turtle()

for i in range(4):
    sven.forward(45)
    sven.right(90)
sven.left(45)
sven.forward(45)
sven.right(45)
for i in range(4):
    sven.forward(45)
    sven.right(90)
sven.forward(45)
sven.left(45)
sven.backward(45)
sven.right(135)
for i in range(3):
    sven.forward(45)
    sven.left(135)
sven.right(90)
sven.forward(45)


input()



"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
