from random import shuffle, randrange


class Cell(object):
    def __init__(self):
        pass

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
                if vis[yy][xx]: continue
                if xx == x: hor[max(y, yy)][x] = "+  "
                if yy == y: ver[y][max(x, xx)] = "   "
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

class Maze(object):
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
                if vis[yy][xx]: continue
                if xx == x: hor[max(y, yy)][x] = "+  "
                if yy == y: ver[y][max(x, xx)] = "   "
                walk(xx, yy)
    
        walk(randrange(w), randrange(h))

        return (vis,ver,hor)

    def print_maze(self):
        s = ""
        for row in self.maze:
            s += ''.join(row[0] + ['\n'] + row[1] + ['\n'])
        print(s)

 
if __name__ == '__main__':
    M = Maze2(32,16)
    M.print_maze()
    M.set_visited(3,4)
    for row in M.maze:
        print(row[0])
        print(row[1])
        print()
    M.print_maze()

