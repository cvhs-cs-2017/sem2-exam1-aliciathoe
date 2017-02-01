#1
def AddTen(n):
    n = n + 10
    return n

print(AddTen(3))

#2
import turtle
sven = turtle.Turtle()

def DrawRectangle(x , y):
    for i in range(2):
        sven.forward(x)
        sven.right(90)
        sven.forward(y)
        sven.right(90)
'''
DrawRectangle(70 , 50)
'''
#3
sally = turtle.Turtle()

def NSides(y):
    x = 360 / y
    for i in range(y):
        sally.forward(35)
        sally.right(x)

NSides(6)
