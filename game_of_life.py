import time
import os
import random

"""
NOT COMPLETE!

An introduction to python using the game of life as a problem to solve in class.
Not the most pythonic or succinct solution, but it's not meant to be.

Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by over-population.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

class golBoard(object):
    def __init__(self,w=20,h=20,populate=False,Density=.25):
        random.seed(234234)
        self.width = w
        self.height = h

        if populate:
            self.currentGen = self.initRandGen(Density)
        else:
            self.currentGen = self.initGen()

    def __str__(self):
        return "width:%d height:%d" % (self.width,self.height)      

        
    """
    @function: makeAlive
    @description: Adds a life to specified location 
    @param: int x - Column to add life
    @param: int y - Row to add life
    @returns: None
    """  
    def makeAlive(self,x,y):
        self.currentGen[x][y] = True
        
    """
    @function: computeNextGen
    @description: Computes the next generation our cellular automata 
    @param: None
    @returns: None
    """        
    def computeNextGen(self):
        nextGen = self.initGen()
        for x in range(self.width):
            for y in range(self.height):
                self.liveOrDie(x,y)
        
    """
    @function: liveOrDie
    @description: Calculates whether a cell lives or dies based on Game of Life rules
    @param: int x - Column to check
    @param: int y - Row to check
    @returns: Int : 0 = nothing changes , -1 = dies , 1 = birth
    """   
         
    def liveOrDie(self,x,y):
        neighbors = []
        alive = self.currentGen[x][y]
        neighbors.append(self.currentGen[x-1][y-1])      # upper left
        neighbors.append(self.currentGen[x][y-1])        # upper middle   
        neighbors.append(self.currentGen[x+1][y-1])      # upper right
        neighbors.append(self.currentGen[x+1][y])        # right
        neighbors.append(self.currentGen[x-1][y])        # left 
        neighbors.append(self.currentGen[x-1][y+1])      # bottom left
        neighbors.append(self.currentGen[x][y+1])        # bottom middle 
        neighbors.append(self.currentGen[x+1][y+1])      # bottom right
           
        count = neighbors.count(True)
        
        if(alive):
            if count < 2 or count > 3:
                return -1 
            else:
                return 0
        else:
            if count == 3:
                return 1
            else:
                return 0                  
                 
    """
    @function: initGen
    @description: Initializes a single generation 
    @param: None
    @returns: list - 2D list containing False
    """         
    def initGen(self):
        #return [[False] * self.width for row in range(self.height)]
        board = []
        for i in range(self.height):
           row = []
           for j in range(self.width):
               row.append(False)
           board.append(row) 
        return board      
    
    
    """
    @function: initRandGen
    @description: Initializes a random generation 
    @param: float - density (how many lives to create)
    @returns: list - 2D list containing False and True
    """        
    def initRandGen(self,density):
        gen = self.initGen()
        
        numberOfLives = int(self.width * self.height * density)
        
        for i in range(numberOfLives):
                x = random.randint(0, self.width-1)
                y = random.randint(0, self.height-1)
                gen[y][x] = self.randomLife()       # ??
        return gen
        
    """
    @function: randomLife
    @description: Generates a random life (zero or one)
    @param: none
    @returns: bool - zero or one (alive or dead)
    """
    def randomLife(self):
        if random.random() > .5:
            x = True
        else:
            x = False
        return x

    """
    @function: stringifyWorld
    @description: Creates a string version of the 2D list representing our world
    @param: none
    @returns: string - a string version 
    """
    def stringifyWorld(self):
        string = ""
        for row in self.currentGen:
            for cell in row:
                if cell == False:
                    string += ' .'
                else:
                    string += ' '+ u'\u265B'   # 07F7        2735  2620
            string += "\n"
        return string



#b = golBoard(50,30,True,.25)
b = golBoard(50,30)
os.system('clear')
time.sleep(0.05)