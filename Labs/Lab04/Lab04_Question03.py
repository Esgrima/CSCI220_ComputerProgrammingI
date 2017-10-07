# importing randint function from random module
from random import randint


# defining function
def randPass():
    # initializing variable char
    char = 0

    # loop that will run until 101/e is generated
    while char != 101:
        # initializes char to random number between 97 and 122
        char = randint(97, 122)
        # prints a letter based on its ASCII code on the same line
        print(chr(char), end='')
# calls the function
randPass()
