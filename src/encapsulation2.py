# Encapsulation we can bind data variables with the methods or functions
# data members = class  variables.Methods are functions within the class

class Bank:

    public_password = 123# public var
    __private_password = 1234 # privater variable available within class
    _protected_var = 12345 # available from in same package

    def __init__(self,acc_no,balance):
        self.balance = balance
        self.__account_no = acc_no

    def deposit(self,amount):
        self.balance += amount

    def check_balance_accno(self):
        print(self.balance)
        self.__private_method()  # will show acc no

    def show_accno(self,is_auth):
        if is_auth == True:
            print(self.__account_no)
        else:
            print("not allowd")

    def __private_method(self): # only used inside class
        print(self.__account_no)
        self.show_accno(True)

icici = Bank(12345,1000)
icici.deposit(100)
icici.check_balance_accno()
# icici.__private_method()
print(icici.show_accno(True))  # through show_accno we acces acc n0

object_ref = Bank(123,1234)
print(object_ref.public_password)
print(object_ref._protected_var)
# print(object_ref.__private_password) cannot be assesed


print("------------------------------88")















