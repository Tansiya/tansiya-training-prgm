"""Define a class named circle which can be constructed by a radius.the circle class has a method can compute the area"""

#Use def to define a method

class Circle(object):

#use function
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)

print (aCircle.area())


