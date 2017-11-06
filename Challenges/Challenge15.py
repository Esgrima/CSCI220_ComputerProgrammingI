def right_triangle():
    # number of stars the user wants
    num = int(input("Provide a number: "))

    # loop that controls the 'height' of the triangle of stars
    for i in range(num):
        # loop that controls the number of spaces in each row of the triangle
        for s in range(num - i, 1, -1):
            print(' ', end=' ')
        # loop that controls the number of stars in each row of the triangle
        for j in range(i + 1):
            print('*', end=' ')
        print()


right_triangle()
