import math


def area_circle():
    print("This program calculates the area of a circle.")

    radius = input("What is the radius of the circle?: ")
    area = round((math.pi * float(radius) ** 2), 2)

    print("The area of the circle is approximately " + str(area) + ".")


area_circle()
