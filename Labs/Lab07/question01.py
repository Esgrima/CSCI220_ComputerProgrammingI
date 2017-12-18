# random list
currList = [1, 5, 22, 89, 28]


def maxInFirst(myList):
    # tracks max value
    maxValue = 0

    # loop that will find max number
    for i in myList:
        if i > maxValue:
            maxValue = i
    # Copies first object to position of maxValue
    currList.insert(currList.index(maxValue), currList[0])
    # Removes the first object
    currList.pop(0)
    # Removes first occurrence of maxValue
    currList.remove(maxValue)
    # Inserts the maxValue at index 0
    currList.insert(0, maxValue)


print(currList)

maxInFirst(currList)

print(currList)
