

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











