from graphics import *


def drawHouse():
    win = GraphWin(height=500, width=800)

    # first and second click coords
    firstClick = win.getMouse()
    secondClick = win.getMouse()

    # rectangle drawn based on first and second clicks
    if firstClick.getX() > secondClick.getX() or firstClick.getY() < secondClick.getY():
        firstClick, secondClick = secondClick, firstClick

    rect1 = Rectangle(firstClick, secondClick)
    rect1.draw(win)

    # calculates the width of rect1
    houseWidth = (abs(firstClick.getX() - secondClick.getX()))

    # third click coords
    thirdClick = win.getMouse()

    # draws rect2 based off first and third click at 1 / 5 of the width of rect1
    Rect2 = Rectangle(Point(thirdClick.getX() + (houseWidth / 10), thirdClick.getY()),
                      Point(thirdClick.getX() - (houseWidth / 10), firstClick.getY()))
    Rect2.draw(win)

    # fourth click coords
    fourthClick = win.getMouse()

    # calculates door width
    doorWidth = (1 / 5) * houseWidth

    # draws the square based off the fourth click at 1 / 2 the size of the door
    squareX1 = fourthClick.getX() - (doorWidth / 4)
    squareX2 = fourthClick.getX() + (doorWidth / 4)
    squareY1 = fourthClick.getY() - (doorWidth / 4)
    squareY2 = fourthClick.getY() + (doorWidth / 4)
    square = Rectangle(Point(squareX1, squareY1), Point(squareX2, squareY2))
    square.draw(win)

    win.getMouse()


drawHouse()
