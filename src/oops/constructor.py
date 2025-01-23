

class Person:
    name ="amit"

    def walk(self,name):
        self.name = name
        print(self.name)


rahul = Person()
pramod = Person()
print(rahul.name)
print(pramod.name)

print("========================12")
class Person:
    name ="amit"

    # def __init__(self, name):# called default variable
    def __init__(self,name): # we need parameterised constructor to assign values to separate instances,to change
        # the values of the  instance variable during creation of object variable
        self.name= name

    def walk(self):
        return self.name

    def run(self,name):
        self.name = name
        print(self.name)


rahul = Person("andy")
pramod = Person("tiwari")
print(rahul.name)
print(pramod.name)
print("who is running with object pramod ",pramod.walk())

print("----------------------------------123")


class Person:
    name ="amit"

    def walk(self,name):
        self.name = name
        print(self.name)


rahul = Person()
pramod = Person()
print(rahul.name)
print(pramod.name)

print("--------------------------------234")

class Car:

    def __init__(self,mame,make ,model): # parameterised constructor
        self.mame = mame
        self.make = make
        self.model = model

    def start_engine(self):
        print("starting a car with the name" + self.mame)
        print("starting a car with the make" + self.make)
        print("starting a car with the model" + self.model)


lambo = Car("sprata","v1","2034")
lambo.start_engine()

xuv = Car("mahindra","v1","2034")
xuv.start_engine()











