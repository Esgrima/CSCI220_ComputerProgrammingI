import math


def heron(a, b, c):
    s = (a + b + c) / 2.0

    calc = s * (s - a) * (s - b) * (s - c)
    global area               #Allows triangle() to reference area
    area = math.sqrt(calc)


def triangle():
    print("Area of a Triangle Calculator.")
    print("Note: The triangle must satisfy the 'Triangle Inequality Theorem'.")

    a = eval(input("What is the length of the 1st side(a)?: "))
    b = eval(input("What is the length of the 2nd side(b)?: "))
    print("Remember 'a + b' must be greater than 'c'!")
    c = eval(input("What is the length of the 3rd side(c)?: "))

    while (a + b < c) or (a + c < b) or (b + c < a):          #Verifies Triangle Inequality Theorem
        print("A triangle at these dimensions cannot exist.")
        c = eval(input("What is the correct length of the 3rd side(c)?: "))

        if a + b > c or (a + c > b) or (b + c > a):
            break

    heron(a, b, c)
    print("The area of the triangle is", round(area, 4), "units.")
triangle()

