#TurtleGraphics.py
#Name: Nick Meier 
#Date: February 13, 2025
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(100/(.5 * (sides)))
        myTurtle.right(360/sides)
        
def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100)
    
    if corner == 1:
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 2:
        myTurtle.forward(50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 3:
        myTurtle.forward(100)
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 4:
        myTurtle.forward(100)
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()


def squaresInSquares(myTurtle, number):
    radius = 175
    length = (2*radius)
    for i in range(number):
        myTurtle.penup()
        myTurtle.goto(-radius,radius)
        myTurtle.pendown()
        drawSquare(myTurtle, (length))
        radius = (radius - 25)
        length = (radius * 2)


def main():
    myTurtle = turtle.Turtle()
    

    #drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon


    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
