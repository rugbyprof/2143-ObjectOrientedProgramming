from random import shuffle, randrange, choice, seed
import os, sys
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command


NSBARRIER = "+--"
NSOPEN = "+  "
EWBARRIER = "|  "
EWOPEN = "   "

def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "-cls" if system_name().lower()=="windows" else "clear"

    # Action
    system_call(command)

def terminal_size():
    return (os.popen('stty size', 'r').read().split())

class Cell(object):
    def __init__(self,x=None,y=None):
        self.x = x
        self.y = y
        self.type = 
        self.visited = False
        self.path = False


    def __str__(self):
        return "[ coord:[%d,%d], vis: %s, top: %s, left:%s ]" % (self.x,self.y,self.visited,self.top,self.left)

class Maze(object):
    def __init__(self,w=32,h=16):
        self.width = w
        self.height = h
        self.maze = []
        self.move_stack = []
        self.start = (0,0)
        self.exit = (self.height-1,self.width-1)

        self.__init_maze()
        # self.__walk(randrange(self.width), randrange(self.height))
        # self.__reset_maze()

    def __init_maze(self):
        """Create a new cell for each maze location
        """
        for y in range(self.height):
            self.maze.append([])
            for x in range(self.width):
                self.maze[-1].append(Cell(y,x))

    def __str__(self):
        strmz = ""
        pmaze = []
        for row in self.maze:
            for cell in row:
                top.append(cell.top)
                marker = cell.left
                if cell.path:
                    marker = marker[0] + '# '
                left.append(marker)                
            pmaze.append(top)
            pmaze.append(left)
        for row in pmaze:
            strmz += ''.join(map(str, row)) + '|'
            strmz += '\n'
        strmz += NSBARRIER * self.width + '+'

        return strmz

def print_usage():
    print("Usage: Need a width and height.\ne.g. python maze_gen.py 24 24")

def run_test():
    if len(sys.argv) != 3:
        print_usage()
        h,w = terminal_size()
        print(h,w)
        sys.exit()
    else:
        w = sys.argv[1]
        h = sys.argv[2]

    M = Maze(int(w),int(h))
    # M.maze[1][0].visited = True
    # M.maze[1][0].path = True
    print(M)
    M.traverse_maze()

if __name__ == '__main__':
    #seed(2234)
    clear_screen()
    run_test()
