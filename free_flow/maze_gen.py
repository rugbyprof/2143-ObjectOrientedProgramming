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

class Cell(object):
    def __init__(self,x=None,y=None):
        self.x = x
        self.y = y
        self.visited = False
        self.top = NSBARRIER
        self.left = EWBARRIER
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
        self.__walk(randrange(self.width), randrange(self.height))
        self.__reset_maze()


    def traverse_maze(self):
        self.maze[self.start[0]][self.start[1]].visited = True
        self.maze[self.start[0]][self.start[1]].path = True
        self.move_stack.append(self.maze[self.start[0]][self.start[1]])

        self.__traverse_maze()

    def __traverse_maze(self):
        clear_screen()
        print(self.__str__())
        if len(self.move_stack) == 0:
            return
        current = self.move_stack.pop()
        current.visited = True
        current.path = True
        #print(current)
        ch = raw_input()

        d = self.__possible_moves(current.x,current.y)
        shuffle(d)

        while len(d) == 0:
            current.path = False
            current = self.move_stack.pop()
            d = self.__possible_moves(current.x,current.y)
            shuffle(d)

        x = d[0][0]
        y = d[0][1]
        self.move_stack.append(self.maze[y][x])
        self.__traverse_maze()

    def __possible_moves(self,x,y):
        possible = []
        if self.__in_bounds(x - 1,y):
            if not self.maze[y][x].left == EWBARRIER and not self.maze[y][x-1].visited:
                possible.append((x - 1,y))
        if self.__in_bounds(x, y + 1):
            if not self.maze[y+1][x].top == NSBARRIER and not self.maze[y+1][x].visited:
                possible.append((x,y+1))
        if self.__in_bounds(x + 1, y):
            if not self.maze[y][x+1].left == EWBARRIER and not self.maze[y][x+1].visited:
                possible.append((x+1,y))
        if self.__in_bounds(x, y - 1):
            if not self.maze[y][x].top == NSBARRIER and not self.maze[y-1][x].visited:
                possible.append((x,y-1))
        return possible

        
    def __reset_maze(self):
        """Mark each cell in maze as not visited.
        """
        for y in range(self.height):
            for x in range(self.width):
                self.maze[y][x].visited = False

    def __init_maze(self):
        """Create a new cell for each maze location
        """
        for y in range(self.height):
            self.maze.append([])
            for x in range(self.width):
                self.maze[-1].append(Cell(y,x))

    def __walk(self,x, y):
        """Walk the maze randomly and knock down walls to create maze.
        """
        self.maze[y][x].visited = True

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if not self.__in_bounds(xx,yy):
                continue
            if self.maze[yy][xx].visited:
                continue
            else:
                if xx == x:
                    if self.__in_bounds(x,max(y, yy)):
                        self.maze[max(y, yy)][x].top = NSOPEN
                if yy == y: 
                    if self.__in_bounds(max(x, xx),y):
                        self.maze[y][max(x, xx)].left = EWOPEN                
            self.__walk(xx, yy)

    def __in_bounds(self,x,y):
        """Test to see if coords are on the maze.
        """
        return (x < self.width and y < self.height) and (x >= 0 and y >= 0)
    
    def __str__(self):
        strmz = ""
        pmaze = []
        for row in self.maze:
            top = []
            left = []
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

    def __is_exit(self,cell):
        return cell.row == self.exit[0] and cell.col == self.exit[1]



def print_usage():
    print("Usage: Need a width and height.\ne.g. python maze_gen.py 24 24")

def run_test():
    if len(sys.argv) != 3:
        print_usage()
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



# class Maze(object):
#     def __init__(self,w=32,h=16):
#         self.width = w
#         self.height = h
#         vis,ver,hor = self.make_maze(self.width,self.height)
#         self.maze = zip(hor,ver)
#         print(len(self.maze[0][0]))
#         print(len(self.maze))


#     # https://rosettacode.org/wiki/Maze_generation#Python
#     def make_maze(self, w, h):
#         vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
#         ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
#         hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
    
#         def walk(x, y):
#             vis[y][x] = 1
    
#             d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
#             shuffle(d)
#             for (xx, yy) in d:
#                 if vis[yy][xx]: continue
#                 if xx == x: hor[max(y, yy)][x] = "+  "
#                 if yy == y: ver[y][max(x, xx)] = "   "
#                 walk(xx, yy)
    
#         walk(randrange(w), randrange(h))

#         return (vis,ver,hor)

#     def print_maze(self):
#         s = ""
#         for row in self.maze:
#             s += ''.join(row[0] + ['\n'] + row[1] + ['\n'])
#         print(s)