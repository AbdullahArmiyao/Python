from math import *

class Circle:
    """
    __init__, __str__ and the others are called dunder methods
    """
    def __init__(self, radius):       #Initialization method
        self.radius = radius
    def __str__(self):      #returns a descriptive string
        return 'This is a circle with radius of {:.2f}'.format(self.radius)
    def __repr__(self):     #returns a formal string
        return 'Circle(radius={})'.format(self.radius)
    def get_area(self):     #Just a function
        return pow(self.radius, 2) * pi
    x=  
c1 = Circle(2.1)
print(c1)
print(c1.get_area())
print(c1.radius)