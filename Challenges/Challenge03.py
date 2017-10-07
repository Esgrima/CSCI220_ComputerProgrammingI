def mean():
    print("This program calculates the average of three numbers.")
    a, b, c = eval(input("Enter three numbers separated by a comma(Ex: 1, 2, 3): "))

    avg = (a + b + c) / 3

    print('The average of these numbers is:', round(avg, 4))


mean()
