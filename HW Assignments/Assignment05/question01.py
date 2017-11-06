from PIL import Image, ImageDraw


def drawCheckerBoard(squareWidthSize: int, imageFileName: str, numOfRows: int):
    # creates a new image object
    myImage = Image.new("RGB", (squareWidthSize, squareWidthSize), "black")
    # saves the image object
    myImage.save("newImage.ppm")
    # calculates the width of the checker boxes
    xyIncrement = squareWidthSize // numOfRows
    # creates an ImageDraw object to modify myImage in RGB mode
    newImage = ImageDraw.Draw(myImage, 'RGB')

    # starting values for y-coord
    oddRowsY1 = 0
    oddRowsY2 = xyIncrement
    evenRowsY1 = xyIncrement
    evenRowsY2 = 2 * xyIncrement

    # loop that iterates based on numOfRows
    for rows in range(1, numOfRows + 1):
        # checks if the current row is odd
        if rows % 2 != 0:
            # loop that iterates from initial x-coord value to final value in the current row
            for oddRowsX1 in range(xyIncrement, squareWidthSize, 2 * xyIncrement):
                # draws a white rectangle with coordinates serving as the 2 corners of the rectangle
                newImage.rectangle([(oddRowsX1, oddRowsY1), (oddRowsX1 - 1 + xyIncrement, oddRowsY2 - 1)], fill='white')
            oddRowsY1 += 2 * xyIncrement
            oddRowsY2 += 2 * xyIncrement
        # this loop is executed if the current row is even
        else:
            # loop that iterates from initial x-coordinate to final value in the current row
            for evenRowsX1 in range(0, squareWidthSize, 2 * xyIncrement):
                newImage.rectangle([(evenRowsX1, evenRowsY1), (evenRowsX1 - 1 + xyIncrement, evenRowsY2 - 1)], fill='white')
            evenRowsY1 += 2 * xyIncrement
            evenRowsY2 += 2 * xyIncrement

    myImage.save(fp=imageFileName)


# drawCheckerBoard(1000, "1000x50.ppm", 50)
# drawCheckerBoard(1000, "1000x20.ppm", 20)
drawCheckerBoard(1000, "1000x100.ppm", 100)
# drawCheckerBoard(100, "100x2.ppm", 2)
# drawCheckerBoard(300, "300x30.ppm", 5)
