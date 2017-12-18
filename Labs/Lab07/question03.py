from graphics import *
from math import sqrt


def myCircle():
    win = GraphWin(height=800, width=800)

    for i in range(5):
        center = win.getMouse()
        second = win.getMouse()
        deltaX = second.getX() - center.getX()
        deltaY = second.getY() - center.getY()

        radius = sqrt(deltaX ** 2 + deltaY ** 2)

        circle = Circle(center, radius)
        circle.draw(win)

    win.getMouse()


myCircle()
