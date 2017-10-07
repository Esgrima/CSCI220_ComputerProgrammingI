# defining function
def sumOfNums():
    # keeps track of sum
    total = 0
    # num will be overridden in the loop by user input and allows entry into the loop
    num = 1

    # loop that will run until num/user input is 0
    while num != 0:
        # user input
        num = float(input("Number: "))
        # adds the numbers
        total += num
    # prints the sum
    print("The sum is:", total)
# calls the function
sumOfNums()
