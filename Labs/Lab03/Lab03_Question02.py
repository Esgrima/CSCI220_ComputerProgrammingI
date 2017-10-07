# defining function
def printMaxMin():
    # user's inputs
    num1 = eval(input('Enter the 1st value: '))
    num2 = eval(input('Enter the 2nd value: '))
    num3 = eval(input('Enter the 3rd value: '))

    # Determines the max value
    if num1 > num2 and num1 > num3:
        print("The max value amongst the three is:", num1)
    elif num2 > num1 and num2 > num3:
        print("The max value amongst the three is:", num2)
    elif num3 > num1 and num3 > num2:
        print("The max value amongst the three is:", num3)

    # Determines the min value
    if num1 < num2 and num1 < num3:
        print("The min value amongst the three is:", num1)
    elif num2 < num1 and num2 < num3:
        print("The min value amongst the three is:", num2)
    elif num3 < num1 and num3 < num2:
        print("The min value amongst the three is:", num3)

# calling function
printMaxMin()
