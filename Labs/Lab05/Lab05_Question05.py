def wordAverage():
    # input number of sentences
    num = int(input("How many sentences will be entered?: "))

    # loop that iterates num times
    for i in range(num):
        # user enters a sentence
        sentence = input("Enter a sentence: ")
        # sentence is split by spaces
        sent = sentence.split(' ')

        total = 0
        # loop that iterates through each object in sent and measures the length of each object and adds them
        for j in sent:
            total += len(j)
        # calculates the average number of words
        avg = total / len(sent)

        # prints the average
        print(avg)

wordAverage()
