from graphics import *


def flipImage(imageFileName):
    # opens image at anchor(0,0)
    image = Image(Point(0, 0), imageFileName)

    # opens the same image with the anchor at the center
    myImage = Image(Point((image.getWidth()) // 2, (image.getHeight() // 2)), imageFileName)

    # Window set at the dimensions of the image
    win = GraphWin(width=myImage.getWidth(), height=myImage.getHeight())

    # nested loop that gets the pixel from each end of the picture and move towards the center followed
    # by setting the pixel on the opposite side of the picture
    for x in range(1, myImage.getWidth() // 2):
        for y in range(1, myImage.getHeight()):
            red1, green1, blue1 = myImage.getPixel(x - 1, y - 1)
            red2, green2, blue2 = myImage.getPixel((myImage.getWidth() - x), y)
            myImage.setPixel((myImage.getWidth() - x), y, color_rgb(red1, green1, blue1))
            myImage.setPixel(x - 1, y - 1, color_rgb(red2, green2, blue2))
    # draws the image
    myImage.draw(win)
    # saves the new image
    myImage.save('horizontal_flip.ppm')

    # waits for a click to close the window
    win.getMouse()


flipImage('pic.ppm')
