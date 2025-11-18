
# Method overriding
# says that, Child or subclass can have same name method as the parent or super class


class Shape:
    def area(self):
        print("Print the AREA of the shape")


class Rectangle(Shape): # IS-A - Single Inheritance
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3,4)
print(shape1.area())


shape2 = Circle(10)
print(shape2.area())


# Method Overriding - Same name in the parent and child
# child always override the parent functions
# super means call my parent function
class GrandFather:
    x = 11
    def home(self):
        print("Old Home")

class Father(GrandFather):
    a = 12
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):
    b = 13
    def home(self):
        super().home() # Father Behaviour by super()
        print(super().a) # Father Asttributes by super()
        print("No House")
        print(self.b)


        # self - me
        # super() - Parent, Super class, Father


pramod = Son()
pramod.home()
print(pramod.x)





