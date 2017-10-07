# defining function
def avgOfNums():
    # keeps track of sum
    total = 0
    # num will be overridden in the loop by user input and allows entry into the loop
    num = 1
    # keeps track of total of numbers entered. starts at -1 to cancel out the last user input
    count = -1

    # loop that will run until num/user input is 0
    while num != 0:
        # user input
        num = float(input("Number: "))
        # increments count by 1 for each number entered
        count += 1
        # adds the numbers
        total += num

    # calculates the average
    avg = total / count
    # prints the sum
    print("The average is:", avg)
# calls the function
avgOfNums()
