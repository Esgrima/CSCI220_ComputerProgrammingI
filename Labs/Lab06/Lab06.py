# from math import pi
#
#
# def sphereArea(radius):
#     area = 4 * pi * radius ** 2
#     return area
#
# def sphereVolume(radius):
#     vol = (4 / 3) * pi * radius ** 3
#     return vol
#
# print(sphereArea(5))
# print(sphereVolume(5))

# def numberWords():
#     # opens rawWords.txt
#     myFile = open('rawWords', 'r')
#
#     # stores the first line in 'words'
#     words = myFile.readline()
#
#     # counter for list
#     count = 1
#     # loop that iterates through each word
#     for i in words.split(' '):
#         # prints the number and the current word
#         print("{0}.  {1}".format(count, i))
#         count += 1
#     # closes the file
#     myFile.close()
#
#
# numberWords()

# def hourlyWages(fileName):
#     # opens files
#     myFile = open(fileName, 'r')
#
#     # loop that iterates thru each line
#     for line in myFile.readlines():
#         # splits the line and stores in newLine
#         newLine = line.split(' ')
#         # converts from str to float and multiplies hours and pay
#         weekPay = float(newLine[2]) * float(newLine[3])
#         # prints first name, last name, and weekly pay(formatted to display money correctly
#         print("{0} {1} ${2:0.2f}".format(newLine[0], newLine[1], weekPay))
#     # closes the file
#     myFile.close()
#
#
# hourlyWages('hourlyWages')

# def nameValue(name):
#     numValue = 0
#     # loop that iterates through each character of the lower cased name
#     for i in name.lower():
#         # adds up the ASCII value of the character minus 96
#         numValue += (ord(i) - 96)
#     return(numValue)
#
#
# print(nameValue('REX'))
# print(nameValue('rex'))
