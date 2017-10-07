# imports the random number generator
from random import randint

# defining the function
def guessNumber():
    # generates random number between 1 and 100
    myRandom = randint(1, 100)

    # loop that simulates 5 tries
    for i in range(1, 6):
        # user's input
        user_Guess = eval(input("Guess a number between 1 and 100: "))

        # checks if the guess is correct, prints 'You win!' and breaks out of the loop if it is
        if user_Guess == myRandom:
            print("You win!")
            break

        # checks if the guess is higher and prints 'Go Lower' if i != 5, if i==5 it prints 'You Lose'
        # and breaks out of the loop
        elif user_Guess > myRandom:
            if i == 5:
                print("You lose")
            else:
                print("Go lower!")

        # checks if the guess is lower and prints 'Go Higher' if i != 5, if i==5 it prints 'You Lose'
        # and breaks out of the loop
        elif user_Guess < myRandom:
            if i == 5:
                print("You lose")
            else:
                print("Go higher!")

# calling the function
guessNumber()
