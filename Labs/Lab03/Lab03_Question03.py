# defining function
def fivePerLine():

    #loop that counts from 1000 to 2000
    for i in range(1000, 2000 + 1):
        # prints 'i's' on the same line
        print(i, end=" ")
        #every 5 iterations, 'i's' will be printed on the next line
        if i % 5 == 0:
            print()

# calling function
fivePerLine()
