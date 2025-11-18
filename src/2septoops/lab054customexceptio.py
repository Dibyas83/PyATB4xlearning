
# The code super().__init__(message) in Python is used within the __init__ method of a subclass to call
# the __init__ method of its parent class

"""
 In the context of __init__, it allows you to access the parent class's __init__ method.
.__init__(message): This part calls the __init__ method of the parent class, passing message as an argument.
The message argument would be specific to the parent class's constructor and would be used to initialize
an attribute in the parent class

"""
class ParentClass:
    def __init__(self, name):
        self.name = name
        print(f"Parent class initialized with name: {self.name}")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)  # Calls ParentClass's __init__
        self.age = age
        print(f"Child class initialized with age: {self.age}")

# Create an instance of the child class
child_instance = ChildClass("Alice", 30)


class BalnaceLowException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter the amount you want to withdraw!!"))
if withdraw > balance:
    raise BalnaceLowException("Balance is Low!!")
else:
    print("Remain Bal ", (balance - withdraw))





