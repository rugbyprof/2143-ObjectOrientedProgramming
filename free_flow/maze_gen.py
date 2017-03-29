from random import shuffle, randrange, choice


class Cell(object):
    def __init__(self,row=None,col=None):
        self.row = row
        self.col = col
        self.visited = False
        self.top = "+--"
        self.left = "|  "

    def __str__(self):
        return "[ coord:[%d,%d], vis: %s, top: %s, left:%s ]" % (self.row,self.col,self.visited,self.top,self.left)

class Maze3(object):
    def __init__(self,w=32,h=16):
        self.width = w
        self.height = h
        self.maze = []
        self.init_maze()
        
    def init_maze(self):
        for y in range(self.height):
            self.maze.append([])
            for x in range(self.width):
                self.maze[-1].append(Cell(y,x))
    
    def do_walk(self):
        self.walk(randrange(self.width), randrange(self.height))

    def walk(self,x, y):
        self.maze[y][x].visited = True

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if xx >= self.width or yy >= self.height:
                continue
            if self.maze[yy][xx].visited:
                continue
            else:
                if choice(['top','left']) == 'top':
                    self.maze[yy][xx].top = "+  "
                else:
                    self.maze[yy][xx].top = "   "                   
            self.walk(xx, yy)
    
    def __str__(self):
        strmz = ""
        pmaze = []
        for row in self.maze:
            top = []
            left = []
            for cell in row:
                top.append(cell.top)
                left.append(cell.left)
            pmaze.append(top)
            pmaze.append(left)
        for row in pmaze:
            strmz += ''.join(map(str, row)) + '|'
            strmz += '\n'
        strmz += '+--' * self.width + '+'
        return strmz


class Maze2(object):
    def __init__(self,w=32,h=16):
        self.width = w
        self.height = h
        vis,ver,hor = self.make_maze(self.width,self.height)
        self.maze = zip(hor,ver)
        print(len(self.maze[0][0]))
        print(len(self.maze))


    # https://rosettacode.org/wiki/Maze_generation#Python
    def make_maze(self, w, h):
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
        hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
    
        def walk(x, y):
            vis[y][x] = 1
    
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]: 
                    continue
                if xx == x: 
                    hor[max(y, yy)][x] = "+  "
                if yy == y: 
                    ver[y][max(x, xx)] = "   "
                walk(xx, yy)
    
        walk(randrange(w), randrange(h))

        return (vis,ver,hor)

    def set_visited(self,r,c):
        self.maze[r][1][c] = "| *"

    def print_maze(self):
        s = ""
        for row in self.maze:
            s += ''.join(row[0] + ['\n'] + row[1] + ['\n'])
        print(s)

 
if __name__ == '__main__':
    # M = Maze2(32,16)
    # M.print_maze()
    # M.set_visited(3,4)
    # for row in M.maze:
    #     print(row[0])
    #     print(row[1])
    #     print()
    # M.print_maze()

    M = Maze3(16,8)
    print(M)
    M.do_walk()
    print(M)

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