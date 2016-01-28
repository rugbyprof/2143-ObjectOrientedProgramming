import time
import os

"""
NOT COMPLETE!

Code used in class, which we will continue with on Thursday as our introduction to python continues.

Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by over-population.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

class golBoard(object):
    def __init__(self,w=20,h=20):
        self.width = w
        self.height = h

        self.board = [[False] * self.width for row in range(self.height)]

        #self.board = []

        #for i in range(self.height):
        #    row = []
        #    for j in range(self.width):
        #        row.append(False)
        #    self.board.append(row)

        self.board[7][5] = True

    def addValue(self,x,y):
        self.board[x][y] = True


    def printWorld(self):
        string = ""
        for row in self.board:
            for cell in row:
                string += "%d"%(cell)
            string += "\n"
        return string



    def __str__(self):
        return "width:%d height:%d" % (self.width,self.height)


b = golBoard(10,10)

print(b)
print(b.printWorld())
for x in range(50):
    #os.system('cls')
    os.system('clear')
    b.addValue(x%10,x%10)
    print(b.printWorld())
    time.sleep(0.05)
