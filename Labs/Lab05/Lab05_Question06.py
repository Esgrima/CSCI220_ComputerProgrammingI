def pigLatin():
    # initial sentence
    sentence = input("Enter a sentence to be converted to Pig Latin: ")

    # splits the sentence
    sent = sentence.split(' ')

    # initializes pig to space
    pig = ''

    # loop that iterates thru each word
    for word in sent:
        # Moves the the first letter to the end and adds ay
        pig += word[1:] + word[0] + 'ay '
    print(pig.lower(), end='')
pigLatin()
