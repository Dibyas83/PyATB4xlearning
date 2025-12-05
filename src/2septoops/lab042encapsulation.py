

# Encapsulation -bind the data variables and methods
# Hide the data members(class variables, instance variables) and can only be used by func if necessary
# by using only the methods.
# priv,protected and public

class Car:
    model = None
    name = None
    password = 123

    def __init__(self):
        self.eng="mech"

    def change_password(self):
        self.password= "jk"
        print(self.password)



object_ref = Car()
print(object_ref.password)
object_ref.change_password()


class My_Class:
    deposit = int(input())
    pub_var = "printable in all packages"
    __priv_var= "not_printable"
    __priv_password= int(input())
    __priv_balance= "12345"
    _prot_password= "123printable_in same package"


    def print(self):
        if self.__priv_password == 7890:

            print(self.__priv_var)
            print(self.__priv_password)
            print(self.__priv_balance)
        else:
            print("no")

    def __edit_balance_admin(self): # cannot be accesed outside
        if self.__priv_password == 7890:
            self.__priv_balance += self.deposit
        else:
            print("no")

obj1 = My_Class()
print(obj1.pub_var)
#print(obj1.__priv_var)
#print(obj1.__priv_password)
print(obj1._prot_password)
print(obj1.print())





