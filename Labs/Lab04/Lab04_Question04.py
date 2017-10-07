# defining function
def caesarCode():
    # initializing letter to 1 to enter the loop. Overridden by user input in loop
    letter = input("Spell out a word: ")
    answer = ''

    # loop that will accept letters until '0' is entered
    while letter != '0':
        # string concantenation, converts letter to ASCII code value, adds 2, converts back to character
        answer += chr((ord(letter) + 2))
        # user input
        letter = input("Spell out a word: ")
    print(answer)
caesarCode()
