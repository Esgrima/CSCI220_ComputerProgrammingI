# imports randint function from the random library
from random import randint


# defining the function
def cowsBulls():
    # initializing 3 random numbers between 0 and 9
    rand1 = randint(0, 9)
    rand2 = randint(0, 9)
    rand3 = randint(0, 9)

    # keeps track of the number of trials
    trial = 0

    # keeps track of the number of cows
    cows = 0

    # loop that will run until the lose or win conditions are met
    while trial < 10 and cows != 3:
        # keeps track of the number of cows and bulls and resets them before execution
        cows = 0
        bulls = 0

        # user's guesses
        guess1 = int(input("Guess the 1st number between 0 and 9: "))
        guess2 = int(input("Guess the 2nd number between 0 and 9: "))
        guess3 = int(input("Guess the 3rd number between 0 and 9: "))

        # checks for the win condition
        if guess1 == rand1 and guess2 == rand2 and guess3 == rand3:
            cows = 3
            break
        # increments cows by 1 for each correct answer in the right place
        if guess1 == rand1:
            cows += 1
        if guess2 == rand2:
            cows += 1
        if guess3 == rand3:
            cows += 1

        # increments bulls by for each correct answer in the wrong place
        if guess1 == rand2 or guess1 == rand3:
            bulls += 1
        if guess2 == rand1 or guess2 == rand3:
            bulls += 1
        if guess3 == rand1 or guess3 == rand2:
            bulls += 1
        print(str(cows) + " cow(s) and " + str(bulls) + " bull(s).")
        trial += 1

    # determines if loop exit was due to either win or loss condition
    if cows == 3:
        print(str(cows) + " cow(s) and " + str(bulls) + " bull(s). \nCongratulations! You WON!")
    else:
        print("Sorry! Try again!")
cowsBulls()
