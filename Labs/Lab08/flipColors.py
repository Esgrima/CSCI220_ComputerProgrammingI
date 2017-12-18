from graphics import *


def flipColors(imageFileName):
    # opens image at anchor(0,0)
    image = Image(Point(0, 0), imageFileName)

    # opens the same image with the anchor at the center
    myImage = Image(Point((image.getWidth()) // 2, (image.getHeight() // 2)), imageFileName)

    # Window set at the dimensions of the image
    win = GraphWin(width=myImage.getWidth(), height=myImage.getHeight())

    # nested loop that gets the colors from each 1/3 section and flips the colors within the section
    for y in range(1, myImage.getHeight() // 3):
        for x in range(1, myImage.getWidth()):
            topRed, topGreen, topBlue = myImage.getPixel(x - 1, y - 1)
            middleRed, middleGreen, middleBlue = myImage.getPixel(x - 1, (myImage.getHeight() // 3) + y - 1)
            bottomRed, bottonGreen, bottomBlue = myImage.getPixel(x - 1, myImage.getHeight() - y - 1)

            myImage.setPixel(x - 1, y - 1, color_rgb(topRed, topBlue, topGreen))
            myImage.setPixel(x - 1, ((myImage.getHeight() // 3) + y - 1), color_rgb(middleGreen, middleRed, middleBlue))
            myImage.setPixel(x - 1, myImage.getHeight() - y - 1, color_rgb(bottomBlue, bottonGreen, bottomRed))

    # draws the file
    myImage.draw(win)
    # saves the file
    myImage.save('colorFlip.ppm')
    # waits for a mouse click
    win.getMouse()

flipColors('pic.ppm')
