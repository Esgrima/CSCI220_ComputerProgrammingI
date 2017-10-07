from math import *


def distance():
    print("Distance Equation")

    x1, y1 = eval(input("What is the 1st (x,y) coordinate?: "))
    x2, y2 = eval(input("What is the 2nd (x,y) coordinate?: "))

    delta_x = x1 - x2
    delta_y = y1 - y2

    dist = sqrt((delta_x ** 2.0) + (delta_y ** 2.0))

    print("The distance between " + '(' + str(x1) + ',' + str(y1) + ')' +
          " and (" + str(x2) + ',' + str(y2) + ") is " + str(round(dist, 4)) + " units.")
distance()
