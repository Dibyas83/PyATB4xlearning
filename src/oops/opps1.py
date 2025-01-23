

# to set the value automatically we use constructor . it is special function in class  it will automatically called when we create an object
a= 10 # global var

class Dog:
    name = None # instance variable initiated
    breed = None
    color = None
    # color ="white" it will be applied to all as a class attribute

    def __init__(self,name):
        print(" i will be automatically called when you create an object")
        self.name = name
        # constructor is required to initialize the value of attributes
    def sleep(self):
        a= 10 # local variable
        print("Sleeping -> " + self.name)

    def bark(self):
        print("barking")

dogy1 = Dog("chow")
print(dogy1.name)
dogy2 = Dog("mhow")
print(dogy2.name)
print(dogy2.sleep())


