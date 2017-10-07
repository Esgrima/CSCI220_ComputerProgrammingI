# defining the function
def gymnasticsScore():
    # variables to keep track of total, min, and max
    total = 0
    max = 0
    min = 10

    # loop that asks user for 6 scores
    for i in range(6):
        score = eval(input("What is the score between 0.0 and 10.0?: "))

        # adds up scores the total
        total += score

        # stores highest value in min
        if score > max:
            max = score

        # stores the lowest value in min
        if score < min:
            min = score

    # calculates the average
    avg = (total - max - min) / 4

    print("The average score is", avg)

# calling the function
gymnasticsScore()
