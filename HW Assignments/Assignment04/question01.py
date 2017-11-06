from random import randint


# function that converts a word into dashes
def dash(word: str):
    # empty array
    hidden = []
    # loop that adds a dash for every letter and space for space
    for letter in word:
        if letter != ' ':
            hidden.append('-')
        elif letter == ' ':
            hidden.append(' ')
    # test feature
    # print(hidden)
    # returns an array of dashes
    return hidden

# test feature
# dash('emilia clarke')


# function that chooses a random word from a file
def random_line(file_name):
    # opens the file
    file = open(file_name, 'r')

    # Stores number of lines in a file
    count = len(file.readlines())

    # closes the file
    file.close()

    # generates a random number between 1 and length of file
    rand = randint(0, count - 1)

    # reopens the file
    file = open(file_name, 'r')

    # stores line 'rand' in secret_word
    secret_word = file.readlines()[rand]

    # closes the file
    file.close()

    # returns the secret_word without \n
    return secret_word.replace('\n', '')


# function that will take a guess and the secret_word as arguments
def converter(c_guess: str, c_word: str, c_hidden):
    # keeps track of letter's index
    count = 0

    # loop that looks for the guess in the word
    for letter in c_word:
        # replaces a dash in c_hidden if c_guess matches a letter in c_word
        if c_guess == letter:
            c_hidden[count] = c_guess
        count += 1
    # # test feature
    # print(c_hidden)
    return ''.join(map(str, c_hidden))


# # test feature
# converter('e', 'emilia clarke', dash('emilia clarke'))

# main controlling function
def hangman():
    print("WELCOME! You're now playing HANGMAN!")

    # lists that store guesses
    incorrect_letters = []
    correct_letters = []

    # number of incorrect guesses allowed
    guesses = 6

    # stores the word to be guessed
    word = random_line('wordBank.txt')
    # stores dash(word)
    hidden = dash(word)

    # loop that will run until user runs out of guesses or user guesses the correct word
    while guesses != 0 and hidden != word:
        # prints hidden in appealing string format
        print("Guess the word: {0}".format(''.join(map(str, hidden))))

        # stores previous guesses
        print("Incorrect Letters:", ' '.join(map(str, incorrect_letters)))
        print("Correct Letters:", ' '.join(map(str, correct_letters)))

        # users guess and displays remaining guesses
        guess = input("Guess a single letter or the entire word({0} remaining guesses): ".format(guesses))
        print()

        # ensures hidden is a list before passed into converter
        if type(hidden) is str:
            hidden = list(hidden)

        # determines if guess is a single character or the entire word
        if len(guess) > 1:
            # if the users chooses to guess the entire word
            if guess.lower() == word:
                print("Congratulations! You guessed the word!: {0}".format(word))
                return
            else:
                print("Wrong guess!")
                guesses -= 1

        else:
            # correct guess, adds letter to correct letters list, calls the converter function
            # and stores the return value in hidden
            if word.find(guess) != -1:
                print("Good guess!")
                correct_letters.append(guess)
                # hidden's previous value is overridden by converter's return value
                hidden = converter(guess, word, hidden)

            # wrong guess, adds letter to incorrect letters list and subtracts guesses by 1
            else:
                print("Wrong guess!")
                incorrect_letters.append(guess)
                guesses -= 1

    # identifies reason for breaking out of the loop, prints win or lose outcomes
    if guesses == 0:
        print("Sorry you lose! Try again!")
    else:
        print("Congratulations! You guessed the word!")


hangman()



