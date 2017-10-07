# def nameReverse():
#     # user's input
#     fullName = input("What is your first and last name?: ")
#
#     # splits the users name at a space
#     answer = fullName.split(' ')
#
#     # prints the last name first then first
#     print(answer[1] + ', ' + answer[0])
# nameReverse()

# def companyName():
#     # user's input
#     domain = input('Provide the domain name of a company(i.e. www.target.com): ')
#
#     # splits the string domain at '.'
#     company = domain.split('.')
#
#     # prints the 2nd object in the company list
#     print(company[1])
# companyName()

# def initials():
#     # user's input
#     num = int(input("How many student's initials will be computed?: "))
#
#     # loop that iterates num times
#     for i in range(1, num + 1):
#         # first name input
#         first = input("Enter the first name of student " + str(i) + ': ')
#         # Asks for last name and uses person's first name
#         last = input("Enter " + first + "'s " + "last name: ")
#         # prints the person initials
#         print(first + "'s " + "initials are " + first[0] + last[0])
#
# initials()

# def wordCount():
#     # user's sentence
#     sentence = input("Enter a sentence: ")
#
#     # splits the sentence by spaces
#     sent = sentence.split(' ')
#
#     # prints the length of sent
#     print(len(sent))
# wordCount()

# def wordAverage():
#     # input number of sentences
#     num = int(input("How many sentences will be entered?: "))
#
#     # loop that iterates num times
#     for i in range(num):
#         # user enters a sentence
#         sentence = input("Enter a sentence: ")
#         # sentence is split by spaces
#         sent = sentence.split(' ')
#
#         total = 0
#         # loop that iterates through each object in sent and measures the length of each object and adds them
#         for j in sent:
#             total += len(j)
#         # calculates the average number of words
#         avg = total / len(sent)
#
#         # prints the average
#         print(avg)
#
# wordAverage()

# def pigLatin():
#     # initial sentence
#     sentence = input("Enter a sentence to be converted to Pig Latin: ")
#
#     # splits the sentence
#     sent = sentence.split(' ')
#
#     # initializes pig to space
#     pig = ''
#
#     # loop that iterates thru each word
#     for word in sent:
#         # Moves the the first letter to the end and adds ay
#         pig += word[1:] + word[0] + 'ay '
#     print(pig.lower(), end='')
# pigLatin()
