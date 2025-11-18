# Encapsulation we can bind data variables with the methods or functions
# data members = class  variables.Methods are functions within the class
from rq.cli import worker


class Office:
    model = None
    name = None
    password = 123

    def __init__(self):
        #self.password ="pram"
        print("dc")


    def change_password(self):
        self.password = "pramod"
        return self.password


object_ref = Office()
print(object_ref.password)
print(object_ref.change_password())

print("------------------------------88")

class Office2:
    model = None
    name = None
    password = 12

    def __init__(self):
        #self.password ="pram"
        print("dc")

    @classmethod
    def change_password(cls):
        password = "pramod"
        return password


object_ref = Office2()
print(object_ref.password)
print(object_ref.change_password())

print("--------------555")
class Car:
    name = None
    worker_password = None

    password = 123

    def __init__(self):
        print("dc")


    def user(self):
        self.password = "pramod"

        return self.password

    def admin(self):
        self.password = "pram"

        return self.password

    def workers(self):
        self.password = input()
        if self.admin() == "pram":
            self.worker = "admin"
        if self.user() == "pramod":
            self.worker = "user"
        print(self.worker)


object_ref1 = Car()
# print(password)
print(object_ref1.password)
print(object_ref1.admin())
print(object_ref1.user())
print(object_ref1.workers())

print("---------------------------5666")

class Office3:
    model = None
    name = None
    password = 123

    def __init__(self):
        self.password ="pram" # encapsulation



    def change_password(self):
        #self.password = "pramod"
        return self.password


object_ref = Office3()
print(object_ref.password)
print(object_ref.change_password())














