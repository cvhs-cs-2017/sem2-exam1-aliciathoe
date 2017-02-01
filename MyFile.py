#1
def AddTen(n):
    n = n + 10
    return n

print(AddTen(3))

#2
import turtle
sven = turtle.Turtle()

def DrawRectangle(AnyTurtle , x , y):
    for i in range(2):
        AnyTurtle.forward(x)
        AnyTurtle.right(90)
        AnyTurtle.forward(y)
        AnyTurtle.right(90)
'''
DrawRectangle(sven , 70 , 50)
'''
#3
sally = turtle.Turtle()

def NSides(y):
    x = 360 / y
    for i in range(y):
        sally.forward(35)
        sally.right(x)
'''
NSides(6)
'''
