# overriding - between different classes,loading is within a class
# encapsulation hiding internal or my own private attributed,var,fun,abstraction hides
# the classes or class level details and show what is required

from abc import ABC,abstractmethod
class Animal(ABC): # ABC is inherited to complete incomplete methods
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self): # has to def sound compulsorily
        print("bark") # needs to be passed here

husky = Dog("siberian")
husky.sound()

print("-----------------------------------------1")
class Father(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Pramod(Father): # as pramod inherited from father he has to pay loan

    def loan(self):
        print("paid the loan")

pramod = Pramod("1L")
pramod.loan()
print(pramod.name)

print("-------------------------2")

class PyAtb(ABC):
    @abstractmethod
    def payfee(selfself):
        pass

    def enrolled(self):
        print("enrolled")

class Amit(PyAtb):
    def payfee(self): # has to use payfee to acess enrolled
        print("paid")

    def enrolled(self):
        print("enrolled")

subh = Amit()
subh.enrolled()

print("-------------------------------------------------")

from  abc import ABC,abstractmethod


class GearBox(ABC):

    @abstractmethod
    def setGear(self):
        pass

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine): # has to use start stop to drive

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def setGear(self):
        print("Gearbox is ready")

    def drive(self):
        self.start()
        self.setGear()
        self.stop()


car = Car() # engine is hidden, is not known to user
car.drive()




