def square():
    # number of stars the user wants
    num = int(input("Provide a number: "))

    # loop that controls the 'height' of the square of stars
    for i in range(num):
        # loop that controls the 'width' of the square of stars
        for j in range(num):
            print('*', end=' ')
        print()


square()
