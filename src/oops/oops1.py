
class Dog:
    name = None
    breed = None
    color = None

    def __init__(self,name):
        print(" i will be automatically called when you create an object")
        self.name = name
    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("barking")

dogy1 = Dog()
print(dogy1.sleep())
print(dogy1.name)
dogy1.name = "ramu"
print(dogy1.name)

# to set the value automatically we use constructor . it is special function in class  it will automatically called when we create an object





















