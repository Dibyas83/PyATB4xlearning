
class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour
    def talk(self):  # NRNG  # self - this , self will be first argument in every behaviour.
        print("I can talk")

    def sleep(self, name):  # Arg with No Return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):  # No Arg with Return
        return "I am walking"


# Create an Object of the Class
# ObjectRef = ClassName() -> Object
tushar = Person()
tushar.name = "tushar"
print(tushar.name)
tushar.talk()


rajyalakshmi = Person()
rajyalakshmi.name = "rajyalakshmi"
print(rajyalakshmi.name)
rajyalakshmi.talk()


class Persons:


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
person1 = Persons()
person1.display_info()








