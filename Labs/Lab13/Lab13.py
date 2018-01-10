import datetime
from random import randint

bigArrays = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000]

# # Tests sorting
# bigArrays = [50]

# loops through list of lengths for sort size
for array in bigArrays:
    currArray = []
    # loop that adds random numbers in new array
    for i in range(array):
        currArray.append(randint(0, array))

    # # Test Feature
    # print(currArray)

    # stores the start time for insertion sort
    timeInitial = datetime.datetime.now()

    # loop that sorts values
    for elOuter in range(1, array):
        flag = True
        for elInner in range(elOuter - 1, -1, -1):
            if currArray[elInner] < currArray[elOuter]:
                popped = currArray.pop(elOuter)
                currArray.insert(elInner + 1, popped)
                flag = False
                break
        if flag:
            popped = currArray.pop(elOuter)
            currArray.insert(elInner, popped)

    # # Test Feature
    # print(currArray)

    # stores the end time for insertion sort
    timeFinal = datetime.datetime.now()
    # stores the duration of the insertion sort
    timeDiff = timeFinal - timeInitial

    print("Insert Sort of size {0} took {1} milliseconds".format(array, timeDiff.microseconds / 1000))
