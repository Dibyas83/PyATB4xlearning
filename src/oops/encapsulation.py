# Encapsulation we can bind data variables with the methods or functions
# data members = class  variables.Methods are functions within the class

class Car:
    model = None
    name = None
    password = 123

    def __init__(self):
        #self.password ="pram"
        print("dc")


    def change_password(self):
        self.password = "pramod"
        return self.password


object_ref = Car()
print(object_ref.password)
print(object_ref.change_password())

print("------------------------------88")

class Car:
    model = None
    name = None
    password = 123

    def __init__(self):
        #self.password ="pram"
        print("dc")

    @classmethod
    def change_password(cls):
        password = "pramod"
        return password


object_ref = Car()
print(object_ref.password)
print(object_ref.change_password())

print("--------------555")
class Car:
    name = None
    password = 123

    def __init__(self):
        print("dc")


    def user(self):
        self.password = "pramod"
        return self.password

    def admin(self):
        self.password = "pram"
        return self.password


object_ref1 = Car()
# print(password)
print(object_ref1.password)
print(object_ref1.admin())
print(object_ref1.user())

print("---------------------------5666")

class Car:
    model = None
    name = None
    password = 123

    def __init__(self):
        self.password ="pram" # encapsulation



    def change_password(self):
        #self.password = "pramod"
        return self.password


object_ref = Car()
print(object_ref.password)
print(object_ref.change_password())














