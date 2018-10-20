"""Define a class named rectangle which can be constructed by a length and width.we can compute the area"""


#Define class named rectangle
class Rectangle(object):
#use function
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(8,3.5)
#print area
print (aRectangle.area())

