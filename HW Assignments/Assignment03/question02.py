def checkIfEven():
    # user input
    num = int(input("Provide a number: "))

    # loop that runs until num is negative
    while num > 0:
        # checks if num is even and prints
        if num % 2 == 0:
            print("The number is even.")
        # prints the number is odd if its not even
        else:
            print("The number is odd.")
        # asks for another number
        num = int(input("Provide a number: "))
checkIfEven()
