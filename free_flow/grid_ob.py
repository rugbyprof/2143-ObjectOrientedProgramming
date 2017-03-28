"""
Grid display.  

Displays a rectangular grid of cells, organized in rows and columns
with row 0 at the top and growing down, column 0 at the left and 
growing to the right.  A sequence of unique colors for cells can 
be chosen from a color wheel, in addition to colors 'black' and 'white'
which do not appear in the color wheel. 

Michal Young (michal@cs.uoregon.edu), October 2012, 
for CIS 210 at University of Oregon.  Revised November 2013
for Sudoku with subgrids. 

Uses the simple graphics module provided by Zelle, which in turn 
is built on the Tk graphics package (and which should therefore be 
available on all major Python platforms, including Linux, Mac, and 
all flavors of Windows at least back to XP). 
https://classes.cs.uoregon.edu//15W/cis210/assignments/Assnmt4-Flood.php
"""

from graphics import *    # Zelle's simple OO graphics
from math import sqrt
import json

black = color_rgb(0,0,0)
white = color_rgb(255,255,255)
red = color_rgb(200,0,0)
green = color_rgb(0,200,0)
blue = color_rgb(0,0,200)
grey = color_rgb(100,100,100)
light_grey = color_rgb(200,200,200)

class Grid(object):
    
    def __init__(self):
        
        self.color_wheel = [  color_rgb(255,0,0), color_rgb(0,255,0), color_rgb(0,0,255),
                                color_rgb(255,255,0), color_rgb(255,0,255), color_rgb(0,255,255),
                                color_rgb(127,255,0), color_rgb(0,127,255), color_rgb(127,0,255),
                                color_rgb(255,127,0), color_rgb(0,255,127), color_rgb(255,0,127),
                                color_rgb(127,127,0), color_rgb(127,0,127), color_rgb(0,127,127),
                                color_rgb(255,255,127), color_rgb(255,127,255), color_rgb(127,255,255) ]
        self.cur_color = 0


        self.nrows = 1



    def make(self, rows, cols, width, height ) :
        """Create the grid display, initially all white.
        rows, cols are the grid size in rows and columns.
        width, height are the window size in pixels.
        
        Args: 
            rows:  number of rows of cells in the grid (vertical divisions)
            cols:  number of columns of cells in the grid (horizontal divisions)
            width:  horizontal width of window in pixels
            height: vertical height of window in pixels
        Returns:  nothing
        """
        self.win = GraphWin("Grid", width, height )
        self.win.setCoords(0, 0, rows, cols)
        bkgrnd = Rectangle( Point(0,0), Point(width,height) )
        bkgrnd.setFill( color_rgb(255,255,255) ) # White background
        self.cell_width = width / cols
        self.cell_height = height / rows
        self.nrows = rows 

        print(dir(self.win))

    def get_cur_color(self):
        """Return the currently chosen color in the color wheel.  
        
        The color wheel is a list of colors selected to be contrast with each other. 
        The first few entries are bright primary colors; as we cycle through the color
        wheel, contrast becomes less, but colors should remain distinct to those with 
        normal color vision until the color wheel cycles all the way around in 18 
        choices and starts recycling previously used colors.   The color wheel starts
        out in position 0, so get_cur_color() may be called before get_next_color() has 
        been called. 
        
        Args:  none
        Returns:  
            a 'color' that can be passed to fill_cell
            
        FIXME: The color wheel should produce colors of contrasting brightness
        as well as hue, to maximize distinctness for dichromats (people with 
        "color blindness".  Maybe generating a good color wheel can be part of a 
        project later in CIS 210.   (This is not a required or expected change 
        for the week 4 project.) 
        """
        return self.color_wheel[self.cur_color]

    def get_next_color(self):
        """Advance the color wheel, returning the next available color. 
        
        The color wheel is a list of colors selected to be contrast with each other. 
        The first few entries are bright primary colors; as we cycle through the color
        wheel, contrast becomes less, but colors should remain distinct to those with 
        normal color vision until the color wheel cycles all the way around in 18 
        choices and starts recycling previously used colors. 
        
        Args:  none
        Returns:  
            a 'color' that can be passed to fill_cell    
        """
        self.cur_color += 1
        if self.cur_color >= len(self.color_wheel) :
            self.cur_color = 0
        return self.color_wheel[self.cur_color]

    def fill_cell(self,row, col, color):
        """Fill cell[row,col] with color.
        
        Args: 
            row:  which row the selected cell is in.  Row 0 is the top row, 
            row 1 is the next row down, etc.  Row should be between 0 
            and one less than the number of rows in the grid. 
            col:  which column the selected cell is in.  Column 0 is 
            the leftmost row, column 1 is the next row to the right, etc. 
            Col should be between 0 and one less than the number of columns
            in the grid. 
            color: What color to fill fill the selecte cell with.  Valid colors
            include grid.white, grid.black, and values returned by 
            grid.get_next_color() and grid.get_cur_color()

        """
        left = col
        right = col + 1
        top = self.nrows - (row + 1)
        bottom = self.nrows - row
        mark = Rectangle( Point(left,bottom), Point(right,top) )
        mark.setFill(color)
        mark.draw(self.win)

        
    def label_cell(self,row, col, text, color=''):
        """Place text label on cell[row,col].
        
        Args: 
            row:  which row the selected cell is in.  Row 0 is the top row, 
            row 1 is the next row down, etc.  Row should be between 0 
            and one less than the number of rows in the grid. 
            col:  which column the selected cell is in.  Column 0 is 
            the leftmost row, column 1 is the next row to the right, etc. 
            Col should be between 0 and one less than the number of columns
            in the grid. 
            text: string (usually one character) to label the cell with
            color: Color of text label
        """
        xcenter = col + 0.5
        ycenter = self.nrows - (row + 1) + 0.5
        label = Text( Point(xcenter, ycenter), text)
        label.setFace("helvetica")
        label.setSize(20)  ## Is there a better way to choose text size? 
        label.setFill(color)
        label.draw(self.win)

    def sub_grid_dim(self,rows, cols):
        """Divide each cell into rows x cols for sub-labeling
        (like "pencil marks" in Sudoku).
        Args:
        rows:  The number of rows of sub-cell in a cell.
        cols:  The number of columns of sub-cell in a cell.
        Returns: nothing
        Effects: Affects behavior of sub_label_cell
        """
        self.n_sub_rows = rows
        self.n_sub_cols = cols

    def sub_label_cell(self,row, col, sub_row, sub_col, text, color=black):
        """Place label in subrow, subcol of row, col.
        Args:
            row:  Row of major grid (counting 0 as top row)
            col:  Column of major grid (counting 0 as leftmost column)
            sub_row:  Row in minor (interior) grid of cell
            sub_col:  Column in minor (interior) grid of cell
            text: Label (usually one character) to place there
            color: color of text
        """
        xcenter = col + ((sub_col + 0.5) / self.n_sub_cols)
        ycenter = self.nrows - (row + 1) + ((sub_row + 0.5) / self.n_sub_rows)
        # print("Placing subgrid label at ({},{})".format(xcenter,ycenter))
        label = Text( Point(xcenter, ycenter), text)
        label.setFace("helvetica")
        label.setSize(10)  ## Is there a better way to choose text size? 
        label.setFill(color)
        label.draw(self.win)
        

    def close(self):
        """ Close the graphics window (shut down graphics). 
        
        Args: none
        Returns: nothing
        Effect:  the grid graphics window is closed. 
        """
        self.win.close()

    def load_colors(self,color_file):
        input = open(color_file,'r')
        colors = json.loads(input.read())

        for c in colors:
            r =  c['rgb'][0]
            g =  c['rgb'][1]
            b =  c['rgb'][2]
            self.color_wheel.append(color_rgb(r,g,b))

        print(self.color_wheel)

    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        num_colors = 9
    else:
        num_colors = sys.argv[1]


    G = Grid()
    G.load_colors('colors.json')
    rows = int(sqrt(float(num_colors)))
    cols = int(sqrt(float(num_colors)))
    # print("Testing grid: 3x3 with 3x3 subgrid")
    G.make(rows,cols,500,500)
    # G.sub_grid_dim(rows,cols)
    for row in range(rows):
        for col in range(cols):
            #color = G.get_next_color()
            G.fill_cell(row, col, color_rgb(255,255,255))

    c = Circle(Point(rows//2,rows//2), .5)
    #c.setFill(color_rgb(255,0,0))
    c.draw(G.win)

    null = raw_input("Press enter to exit ")
    G.close()
