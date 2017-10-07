# defining function
def yesNo():
    # initializes answer to a to enter the loop
    answer = 'a'

    # loop that will run until the right answer is provided
    while answer != 'y' and answer != 'n' and answer != 'yes' and answer != 'no':
        answer = input("Do you like ice cream?: ")
    # prints if the first letter of y or yes is y
    if answer[0] == 'y':
        print("Great!")
    # prints if the first letter of n or no is n
    elif answer[0] == 'n':
        print("-_-")
yesNo()
