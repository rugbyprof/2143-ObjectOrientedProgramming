"""
Program "AsciiShop"
Name(s):
  Daniel Tomei
"""

import os
import time
import urllib3, uuid
from PIL import Image
import sys


url = 'http://thecatapi.com/api/images/get'

def getCat(directory=None, filename=None, format='png'):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    http = urllib3.PoolManager()
    r = http.request('GET', downloadlink)
    fp = open(savefile, 'wb')
    fp.write(r.data)
    fp.close()
    return savefile

class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image        
        self.img = None         # Pillow var to hold image


    """ 
    @Name: getImage
    @Description:
    - Uses random cat to go get an amazing image from the internet
    - Names the image
    - Saves the image to some location  
    -If user passed image name, opens that image instead
    @Params: img_name (string) - Used if user wants to pass an image, instead of getting a random one
    @Returns:
    """
    def getImage(self, img_name = None):
        if img_name == None:
            self.name = self.getTimeStamp()
            getCat(directory=self.path, filename=self.name, format=self.format)
            self.img = Image.open(self.name+'.'+self.format)
            
        #User passed image name
        else:
            self.name, self.format = img_name.split('.')
            self.img = Image.open(self.name+'.'+self.format)
            
        self.width, self.heigth = self.img.size
        
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
        seconds,milli = str(time.time()).split('.')
        return seconds 


""" 
The ascii character set we use to replace pixels. 
The grayscale pixel values are 0-255.
0 - 25 = '#' (darkest character)
250-255 = '.' (lightest character)
"""


class AsciiImage(RandomCat):

    def __init__(self,new_width="not_set"):
        super(AsciiImage, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0
            
        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.imageAsAscii = []
        self.matrix = None
        
        
    """
    Your comments here
    """
    def convertToAscii(self):
    
        if self.newWidth == "not_set":
            self.newWidth = self.width
            
        self.newHeight = int((self.heigth * self.newWidth) / self.width)
            
        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height
            
        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(all_pixels,self.newWidth)
        

        for pixel_value in all_pixels:
            index = pixel_value // 25 # 0 - 10
            self.imageAsAscii.append(self.asciiChars[index])

    """
    @Name: printImage
    @Description:
        This method prints the ascii image to the screen.
    @Params: image_to_print (string) - the image that the method will print. Defaulted to self.imageAsAscii
    @Returns:
    """
    def printImage(self, image_to_print = "original"):
        #Incase image was flipped incorrectly
        if image_to_print == None:
            return
        
        #The second parameter was added because flip and insert return their own string,
        #instead of modifying self.imageAsAscii
        if image_to_print == "original":
            image_to_print = self.imageAsAscii
            
        self.image_to_print = ''.join(ch for ch in image_to_print)
        for c in range(0, len(self.image_to_print), self.newWidth):
            print (self.image_to_print[c:c+self.newWidth])

    
    """
    @Name: flip
    @Description:
        This method will flip an image horizontally, or vertically. 
        Vertically means all pixels in row 0 => row N, row 1 => row N-1, ... row N/2 => row N/2+1
        Horizontally means all pixels in col 0 => col N, col 1 => col N-1, ... col N/2 => col N/2+1
    @Params: direction (string) - [horizontal,vertical] The direction to flip the cat.
    @Returns: (string) - Flipped ascii image.
    """
    def flip(self, direction):
        if direction != "horizontal" and direction != "vertical":
            print("Incorrectly called flip function")
            return None
        
        elif direction == "horizontal":
            flipped_ascii = []
            
            """
            Idea for list[::-1] taken from
            http://stackoverflow.com/questions/3705670/best-way-to-create-a-reversed-list-in-python
            (Alex Martelli's response)
            """      
            temp_2D_list = listToMatrix(self.imageAsAscii, self.newWidth)
            for col in temp_2D_list:
                for item in col[::-1]:
                    flipped_ascii.append(item)
                
            return flipped_ascii
            
        #direction is vertical
        else:
            flipped_ascii = self.imageAsAscii[::-1]
            return flipped_ascii
    
    """
    @Name: invert 
    @Description:
    This method will take all the lightest pixels and make them the darkest, next lightest => next darkest, etc..
    @Params: None
    @Returns: (string) - Inverted ascii image.
    """
    def invert(self):
        inverted_ascii = []
        for symbol in self.imageAsAscii:
            #inverse_index = 10 - index
            inverted_symbol_index = len(self.asciiChars) - 1 - self.asciiChars.index(symbol)
            inverted_symbol = self.asciiChars[inverted_symbol_index]
            inverted_ascii.append(inverted_symbol)
        
        return inverted_ascii

"""
Convert to 2D list of lists to help with manipulating the ascii image.
Example:
    
    L = [0,1,2,3,4,5,6,7,8]
    
    L = to_matrix(L,3)
    
    L becomes:
    
    [[0,1,2],
    [3,4,5],
    [6,7,8]]
"""
def listToMatrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
 
"""
@Name: userMenu
@Description:
-Used to receive and direct user input.
-Either restarts loop, 
    exits loop,
    or calls imageProcessing() before restarting loop
@Params: None
@Returns:   True-Keep looping
            False-Stop looping
"""   
def userMenu():
    user_input = input("\n\nWould you like to (1)-Get a random image, (2)-Input an image name, or (3)-Exit the program?\n")
    if user_input == "3":
        print("Exiting program")
        return False
    
    #if input is invalid restart loop
    elif user_input != "1" and user_input != "2":
        print("Please input the number corresponding to your choice.\nTry again\n")
        return True
    
    #Getting random image
    elif user_input == "1":
        awesomeCat.getImage()
        imageProcessing(awesomeCat)
        return True
        
    #Getting image by name
    #image has to be in script directory    
    elif user_input == "2":
        user_input_image_name = input("Enter the full name of the image you would like to use\n")
        
        #if file exists
        if os.path.isfile(user_input_image_name):
            awesomeCat.getImage(user_input_image_name)
            imageProcessing(awesomeCat)
            return True
            
        #if file doesn't exist restart loop
        else:
            print("Please input a correct file name. Make sure you include the image format.\nTry again\n")
            return True

"""
@Name: imageProcessing
@Description:
-Called by userMenu()
-Outputs image as ascii to screen
-Outputs inverted image as ascii to screen
-Calls flipPrompt()
@Params: obj_ascii_img (AsciiImage)-image to be processed
@Returns:
"""  
def imageProcessing(obj_ascii_img):
    obj_ascii_img.convertToAscii()
    
    print("\nPrinting original image.\n")
    obj_ascii_img.printImage()
    
    print("\nPrinting inverted image.\n")
    obj_ascii_img.printImage(obj_ascii_img.invert())
    
    #Proceeding to flipping part of program
    flipPrompt(obj_ascii_img)
    
    
"""
@Name: flipPrompt
@Description:
-Called by imageProcessing()
-Asks user if they want to flip image
-Asks user which direction to flip
-Outputs flipped image as ascii to screen
@Params: obj_ascii_img (AsciiImage)-image to be processed
@Returns:
"""       
def flipPrompt(obj_ascii_img):
    user_input = input("Would you also like to flip the original image?\n(1)-Yes, (2)-No\n")
    #Not flipping -> exit function
    if user_input == "2":
        return
    
    #flipping
    elif user_input == "1":
        user_input_direction = input("Would you like to flip (1)-Horizontally, or (2)-Vertically?\n")
        #Horizontally
        if user_input_direction == "1":
            print("Printing horizontally flipped image.\n")
            obj_ascii_img.printImage(obj_ascii_img.flip("horizontal"))
            return
            
        #Vertically    
        elif user_input_direction == "2":
            print("Printing vertically flipped image.\n")
            obj_ascii_img.printImage(obj_ascii_img.flip("vertical"))
            return
            
        else:
            print("Please input the correct number corresponding to your choice.\nTry again\n")
            return    
            
    #Input is invalid        
    else:
        print("Please input the correct number corresponding to your choice.\nTry again\n")
        return
     
     
if __name__=='__main__':
    """
    Looping user menu.
    Resetting awesomeCat object every iteration
    Loop exits if userMenu() returns False
    """
    menu_loop = True
    while menu_loop == True:
        awesomeCat = AsciiImage(150)
        menu_loop = userMenu()

                