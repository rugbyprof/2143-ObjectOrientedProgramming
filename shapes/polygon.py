from line import Line

class Polygon(object):
    def __init__(self):
        self.map={}
        self.sides = 0
        
    def add_line(self, l1):
        if len(self.map) ==0:
            self.map[l1.p1]=l1
            self.sides += 1
        else:
            if not l1.p1 in self.map.keys():
                self.map[l1.p1] = l1
                self.sides += 1 
    def iscomplete(self):
        if l1.p2 is 
        return True
                    
    
        