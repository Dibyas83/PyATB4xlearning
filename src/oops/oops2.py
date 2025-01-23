

class Dog:
    name = None
    age = None

    def __init__(self,name,age):
        print("Called object is created")
        self.name = name
        self.age = age

    def sleep(self):
        #ocal variable = 10
        print("sleeping ->" ,self.name,self.age)
        return None

# directoreis
# package - we can call  file or function to other packages

# how to taake user input


class Person:


    # def __init__(self,name,age):
    def __init__(self):
        print("Called object is created")
        self.name = input("Enter your name") # attributes
        self.age = input("Enter your age")

    def display_info(self):
        print(f"Name is {self.name}",f"Age is {self.age}")
        print(f"Age is {self.age}") # behaviour

    def sleep(self):
       #local variable = 10
        print("sleeping ->" ,self.name,self.age)
        return None

# create an object
person1 = Person()
person1.display_info()







