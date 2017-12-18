from graphics import *


def drawTarget():
    win = GraphWin()

    colors = ['white', 'black', 'blue', 'red', 'yellow']
    radius = 50

    for color in colors:
        circle = Circle(Point(100, 100), radius)
        circle.setFill(color)
        circle.draw(win)
        radius -= 10

    win.getMouse()

drawTarget()
