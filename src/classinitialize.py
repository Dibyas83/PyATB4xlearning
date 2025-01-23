class Dog:
    species = "Canine"

    def __init__(self,name,age): # initializes the name and age attributes when a new object is created
        self.name = name
        self.age = age

dog1 = Dog("budy",4)
print(dog1.name)
print(dog1.age)