"""
objects many form
behaviour based on who is calling
allows objects of different classes to be treated as objects of a common superclass
it can be acheived by method overriding,method overloading.
"""

class Shape:

    def area(self):
        print("print the area of shape")

class Rectangle(Shape):

    def __init__(self,lleng,bre):
        self.length = lleng
        self.breadth = bre

    def area(self):
        return self.length*self.breadth

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14*self.radius * self.radius

shape1 = Rectangle(3,4)
print(shape1.area())
shape2 = Circle(5)
print(shape2.area())

print("------------------------------------------777")


class Gf:

    x = 23

class Father(Gf):
    aa = 20

    def home(self):
        # super().x
        print("a")

class Son(Father):
    h =30

    def home(self):
        super().home() # calling father behaviour

        print(super().aa)# calling father behaviour
        print(super().x)
        print("b")
        print(self.h)

pram = Son()
pram.home()










