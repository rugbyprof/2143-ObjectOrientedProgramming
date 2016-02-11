import cat
import os
import time

class randomCat(object):

    def __init__(self):
        self.width = 0          # width of image
        self.height = 0         # height of image
        self.name = ''          # name of image
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
        self.name = self.getTimeStamp()
        cat.getCat(directory=self.path, filename=self.name, format=self.format)
        
    """
    Saves the image to the local file system given:
    - Names
    - Path
    """
    def saveImage(self):
        pass      


    """
    @Description:
        Gets time stamp from local system. The format returned is 1455208995.19
        so I cast the timestamp into a string, then split off the milliseconds.
    @Params:
        None
    @Returns:
        (string) seconds
    """
    def getTimeStamp(self):
        ts = str(time.time())
        seconds,milli = ts.split('.')
        return seconds

class AsciiCat(randomCat):
        
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

    """
    def nameImage(self):
        pass


    """
    Print the image to the screen
    """
    def printImage(self):
        pass

if __name__=='__main__':
    A = AsciiCat()
    A.getImage()
    