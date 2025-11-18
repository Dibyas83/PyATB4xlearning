
#  Class Variable.
#  Method
#      # Public - Variable - Don't Mention anything
#      # Protected - _
#      # Private - __
# Inheritance
# Polymorphism
# Abstraction,
# Encapsulation
# Static Method
# Variables


# Variables
# 1. Local Variable (within the functionc / block
# 2. global
# 3. instance variable (within the class
# 4. static variable ( in future)

a = 10


class Person:
    b = 11 # Instance - Belong to class
    c = 11 # Instance - Belong to class
    aa = "Hello"
    def print_infor(self):
        global a # Declare it as global
        a = "Hello"
        a += "Hello"
        self.aa += "Hello"
        print(a)
        print(self.aa)
        print(self.b)
        print(self.c)



object_Ref = Person()
object_Ref.print_infor()
object_Ref.print_infor()
object_Ref.print_infor()
object_Ref.print_infor()
print(a)
# print(b)



count = 0


def increament():
    global count
    count = count + 1


increament()
print(count)
increament()
print(count)
increament()
print(count)
increament()
print(count)


