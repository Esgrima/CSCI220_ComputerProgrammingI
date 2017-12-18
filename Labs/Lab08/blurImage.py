from graphics import *


def blurImage(imageFileName):

    # opens image at anchor(0,0)
    image = Image(Point(0, 0), imageFileName)

    # opens the same image with the anchor at the center
    myImage = Image(Point((image.getWidth()) // 2, (image.getHeight() // 2)), imageFileName)

    # Window set at the dimensions of the image
    win = GraphWin(width=myImage.getWidth(), height=myImage.getHeight())

    # nested loop that gets the pixels surrounding a point
    for x in range(myImage.getWidth() - 2):
        for y in range(1, myImage.getHeight() - 2):
            red1, green1, blue1 = myImage.getPixel(x + 2, y + 2)
            red2, green2, blue2 = myImage.getPixel(x, y)
            red3, green3, blue3 = myImage.getPixel(x + 2, y)
            red4, green4, blue4 = myImage.getPixel(x, y + 2)

            # averages the rgb colors four the surrounding pixels
            red_avg = (red1 + red2 + red3 + red4) // 4
            green_avg = (green1 + green2 + green3 + green4) // 4
            blue_avg = (blue1 + blue2 + blue3 + blue4) // 4

            # sets the new color for the pixel
            myImage.setPixel(x + 1, y + 1, color_rgb(red_avg, green_avg, blue_avg))

    myImage.draw(win)
    myImage.save('blurpic.ppm')

    win.getMouse()

blurImage('pic.ppm')
