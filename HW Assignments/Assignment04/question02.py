from random import randint


def random_line(file_name):
    # opens the file
    file = open(file_name, 'r')

    # Stores number of lines in a file
    count = len(file.readlines())

    # closes the file
    file.close()

    # generates a random number between 0 and length of file
    rand = randint(0, count - 1)

    # reopens the file
    file = open(file_name, 'r')

    # stores random line
    r_countryCapital = file.readlines()[rand]

    # closes the file
    file.close()

    # returns the secret_word without \n
    return r_countryCapital.replace('\n', '')


def countryCapital():
    attempts = 5

    # loop that will give the user 5 attempts
    while attempts != 0:
        # stores the country and capital line from the random line
        countCap = random_line('country_capital.txt').split(" : ")
        # stores the country and capital in separate variables
        country, capital = countCap[0], countCap[1]

        # user's guess
        guess = input("What's the capital of {0}?: ".format(country))

        # checks if the user is correct or wrong, lower() was used to avoid case conflicts
        if guess.lower() == capital.lower():
            print("Congratulations!")
        else:
            print("You lost!")

        # reduces attempts by 1 after each question
        attempts -= 1


countryCapital()
