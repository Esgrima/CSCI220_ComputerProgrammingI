def nameReverse():
    # user's input
    fullName = input("What is your first and last name?: ")

    # splits the users name at a space
    answer = fullName.split(' ')

    # prints the last name first then first
    print(answer[1] + ', ' + answer[0])
nameReverse()
