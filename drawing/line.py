from point import Point


class Line(object):
    def __init__(self,p1,p2):

        if type(p1) is Point:
            self.p1 = p1
        elif type(p1) is tuple:
            self.p1 = Point(p1)
        else:
            raise("oops")
            
        if type(p2) is Point:
            self.p2 = p2
        elif type(p2) is tuple:
            self.p2 = Point(p2)
        else:
            raise("oops")
            
    def __str__(self):
        return "<%s , %s>" % (self.p1,self.p2)

           
if __name__=='__main__':

    L1 = Line(Point(3,4),Point(6,7))
    L2 = Line((8,4),(-1,-2))
    
    print(L1)
    