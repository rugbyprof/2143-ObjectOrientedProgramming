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
    def __init__(self,row=None,col=None):
        self.row = row
        self.col = col
        self.visited = False
        self.top = NSBARRIER
        self.left = EWBARRIER
        self.path = False 

    def __str__(self):
        return "[ [row:%d, col:%d], vis: %s, top: %s, left:%s ]" % (self.row,self.col,self.visited,self.top,self.left)
        

class Maze(object):
    def __init__(self,w=32,h=16):
        self.width = w
        self.height = h
        self.maze = []
        self.move_stack = []

        
        self.log = open('log.txt','w')
        self.log.close()

        self.__init_maze()
        #self.__walk(randrange(self.height), randrange(self.width))
        self.__reset_maze()

        self.start = self.maze[0][0]
        self.exit = self.maze[self.height-1][self.width-1]


    def traverse_maze(self):
        self.start.visited = True
        self.start.path = True
        self.move_stack.append(self.start)

        self.__traverse_maze()

    def __traverse_maze(self):
        clear_screen()
        print(self.__str__())
        if len(self.move_stack) == 0:
            return False
        

        current = self.move_stack.pop()

        current.visited = True
        current.path = True

        if current == self.exit:
            return True
            
        d = self.__possible_moves(current.row,current.col)
        shuffle(d)

        self.__log(d)

        ch = raw_input()

        if len(d) == 0:
            current.path = False
            self.move_stack.pop()
            print("popping")
        else:
            self.move_stack.append(d.pop())
            print("adding")

        self.__traverse_maze()

    def __log(self,m):
        self.log = open('log.txt','a')
        if type(m) is list:
            for i in m:
                i = i.__str__()
                self.log.write(i+'\n')
            self.log.write('\n')
        else:
            self.log.write(m+'\n')
            self.log.write('\n')
        self.log.close()

    def possible_moves(self,row,col):
        self.__log( self.__possible_moves(row,col))
        return self.__possible_moves(row,col)

    def __possible_moves(self,row,col):
        possible = []
        if self.__in_bounds(row - 1,col):
            if not self.maze[row][col].left == EWBARRIER and not self.maze[row][col-1].visited:
                self.__log("%s"%('Left'))
                possible.append(self.maze[row][col-1])
        if self.__in_bounds(row, col + 1):
            if not self.maze[row+1][col].top == NSBARRIER and not self.maze[row+1][col].visited:
                self.__log("%s"%('Down'))
                possible.append(self.maze[row+1][col])
        if self.__in_bounds(row + 1, col):
            if not self.maze[row][col+1].left == EWBARRIER and not self.maze[row][col+1].visited:
                self.__log("%s"%('Right'))
                possible.append(self.maze[row][col+1])
        if self.__in_bounds(row, col - 1):
            if not self.maze[row][col].top == NSBARRIER and not self.maze[row-1][col].visited:
                self.__log("%s"%('Up'))
                possible.append(self.maze[row-1][col])
        return possible

        
    def __reset_maze(self):
        """Mark each cell in maze as not visited.
        """
        for row in range(self.height):
            for col in range(self.width):
                self.maze[row][col].visited = False

    def __init_maze(self):
        """Create a new cell for each maze location
        """
        for row in range(self.height):
            self.maze.append([])
            for col in range(self.width):
                self.maze[-1].append(Cell(row,col))

    def __walk(self,row,col):
        """Walk the maze randomly and knock down walls to create maze.
        """
        self.maze[row][col].visited = True

        d = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
        shuffle(d)
        for (rr, cc) in d:
            if not self.__in_bounds(rr,cc):
                continue
            if self.maze[rr][cc].visited:
                continue
            else:
                if rr == row:
                    if self.__in_bounds(row,max(col, cc)) and row > 0:
                        self.maze[max(row, rr)][col].top = NSOPEN
                if cc == col: 
                    if self.__in_bounds(max(row, rr),col) and col>0:
                        self.maze[row][max(col, cc)].left = EWOPEN                
            self.__walk(rr, cc)

    def __in_bounds(self,row,col):
        """Test to see if coords are on the maze.
        """
        return (row < self.height and col < self.width) and (row >= 0 and col >= 0)
    
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
        return cell.row == self.exit.row and cell.col == self.exit.col



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
    print(M.possible_moves(4,0))
    #M.traverse_maze()

if __name__ == '__main__':
    seed(2234)
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