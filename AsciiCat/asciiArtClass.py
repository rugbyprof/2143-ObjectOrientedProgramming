import cat
import os


class AsciiImage(object):

    def __init__(self):
        self.width = 0          # width of image
        self.height = 0         # height of image
        self.name = 'cat'       # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'     # format of picture we want


    """
    @Description: 
    - Uses random cat to go get an amazing image from the internet
    - Names the image
    - Saves the image to some location
    @Returns: 
    """
    def getImage(self):
        cat.getCat(directory=self.path, filename=self.name, format=self.format)


    """

    """
    def convertToAscii(self):

        pass

    """
    Converts to grayscale using PIL
    """
    def convertToGrayscale(self):
        pass

    """
    Saves the image to the local file system given:
    - Names
    - Path
    """
    def saveImage(self):
        pass

    """

    """
    def nameImage(self):
        pass

    """
    Gets time stamp from local system
    """
    def getTimeStamp(self):
        pass

    """
    Print the image to the screen
    """
    def printImage(self):
        pass

if __name__=='__main__':
    A = AsciiImage()
    A.getImage()
    