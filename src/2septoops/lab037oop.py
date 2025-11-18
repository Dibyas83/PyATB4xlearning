
class Doga: # class Name will always start from the Capital letter
    # A
    name = None
    breed = None
    color = None

    # B
    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("bark")

    def eat(self,food):
        print(food)


dog1 = Doga()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print(" ---- -----------------")


dog2 = Doga()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)

dog3 = dog1

# to set the value automatically we use constructor . it is special function in class  it will automatically called when we create an object
a= 10 # global var


# Constructor
# Special Function in Class,  __init__()
# It will be automatically called when you create an Object

class Dogu:
    species = "Canine"
    name = None # Instance VARIABLE
    age = None
    color = "Black" #- Hardcoded - not generic to all - blueprint?

    def __init__(self, name, age):
        print("Called, Object is created")
        self.name = name
        self.age = age


    def sleep(self):
        local_variable = 10
        print("Sleeping")
        print("Who is sleeping -> ", self.name, self.age)
        return None

print("------------------------dogu")
dog1 = Dogu("chow", 10)
print(dog1.name)  # dog1 is self
dog1.sleep()
print(dog1.color)
print(id(dog1))

dog2 = Dogu("mow", 20)
print(dog2.name)
dog2.sleep()
dog2.color= "red"
print(dog2.color)
print(id(dog2))

k=Dogu(name="",age="")
print(k.name)
#print(name) # error

