from random import randint


def rockPaperScissors():
    # keeps track of times played and permits entry into loop
    count = 0
    # keeps track of user and computer wins
    userWins = 0
    compWins = 0

    # loop that will run 10 times
    while count < 10:
        # computer generates random play
        compPlay = randint(1, 3)

        # overrides random number with corresponding play
        if compPlay == 1:
            compPlay = 'rock'
        elif compPlay == 2:
            compPlay = 'paper'
        else:
            compPlay = 'scissors'

        # users play
        userPlay = input("Pick 'Rock', 'Paper', or 'Scissors': ")

        # identifies win conditions
        if ((userPlay == 'rock' and (compPlay == 'scissors')) or
            (userPlay == 'paper' and (compPlay == 'rock')) or
            (userPlay == 'scissors' and (compPlay == 'paper'))):
            userWins += 1
            print("Computer: " + compPlay + ". You Won!")

        # identifies a draw
        elif compPlay == userPlay:
            print("Computer: " + compPlay + ". Draw!")

        # computer won
        else:
            compWins += 1
            print("Computer: " + compPlay + ". You Lost!")
        count += 1
    print("User Wins:", userWins)
    print("Computer Wins:", compWins)
rockPaperScissors()
