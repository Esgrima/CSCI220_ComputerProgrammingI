import datetime
from random import randint

bigArrays = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000]

# # Tests sorting
# bigArrays = [20]

# loops through list of lengths for sort size
for array in bigArrays:
    currArray = []
    # loop that adds random numbers in new array
    for i in range(array):
        currArray.append(randint(0, array))

    # # Test Feature
    print(currArray)

    # stores the start time for bubble sort
    timeInitial = datetime.datetime.now()

    sortStatus = False

    while not sortStatus:
        # loop that shifts the limit to the left after each pass
        for limit in range(len(currArray)):
            sortFlag = True
            for num in range(len(currArray) - 1 - limit):
                if currArray[num] > currArray[num + 1]:
                    currArray[num], currArray[num + 1] = currArray[num + 1], currArray[num]
                    sortFlag = False
        if sortFlag == True:
            sortStatus = True

    timeFinal = datetime.datetime.now()

    # # Test Feature
    print(currArray)

    # stores the end time for bubble sort

    # stores the duration of the bubble sort
    timeDiff = timeFinal - timeInitial

    print("Bubble Sort of size {0} took {1} milliseconds".format(array, timeDiff.microseconds / 1000))
