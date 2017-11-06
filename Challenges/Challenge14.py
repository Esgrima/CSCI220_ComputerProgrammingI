def left_triangle():
    # number of stars the user wants
    num = int(input("Provide a number: "))

    # loop that controls the 'height' of the triangle of stars
    for i in range(num):
        # loop that controls the 'width' of each row in the triangle
        for j in range(i + 1):
            print('*', end=' ')
        print()


left_triangle()
