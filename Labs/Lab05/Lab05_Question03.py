def initials():
    # user's input
    num = int(input("How many student's initials will be computed?: "))

    # loop that iterates num times
    for i in range(1, num + 1):
        # first name input
        first = input("Enter the first name of student " + str(i) + ': ')
        # Asks for last name and uses person's first name
        last = input("Enter " + first + "'s " + "last name: ")
        # prints the person initials
        print(first + "'s " + "initials are " + first[0] + last[0])

initials()
