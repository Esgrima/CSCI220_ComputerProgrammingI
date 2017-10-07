def wordCount():
    # user's sentence
    sentence = input("Enter a sentence: ")

    # splits the sentence by spaces
    sent = sentence.split(' ')

    # prints the length of sent
    print(len(sent))
wordCount()
