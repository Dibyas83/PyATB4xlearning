
"""
Single underscore (_)
This is a convention, not a strict rule, to signal that a variable is for internal use only.
The variable can still be accessed from outside the class, but it is considered bad practice.
Example: _my_variable.

Double underscore (__)
This is a stronger convention that engages Python's "name mangling" feature.
Name mangling changes the variable's name to include the class name, making it harder to access
accidentally from outside.
This is often used to prevent name clashes in subclasses, but it does not make the variable truly
inaccessible.
Example: __my_variable becomes _ClassName__my_variable

"""
a = 10
class Myclass:

    # public var (instance)
    public_var = "I am PUBLIC"
    __balance = 100

    # Private variable
    __private_var = "I am private."
    __password = "1234"
    # Protected variable
    _protected_var = "I am protected."
    b = 10
    _c = 20
    __d = 45
    college = "ABC"
    pramod =  "TTA"
    __pramod_bank =  100000000000
    print(__balance)


object = Myclass()
print(object.public_var)
print(object._protected_var)
#print(object.__balance)
# print(object.__private_var)
# print(object.__password)

print("-----------------------------------bank")

class Bank:
    is_auth=None

    def __init__(self, account_number, balance, password):
        self.balance = balance
        self.__account_number = account_number
        self.password = password


    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def login(self):

        if self.password =="ff12":
            self.is_auth = True
            return self.is_auth
        else:
            self.is_auth=False
            return self.is_auth

    def show_me_account_number(self):
        if self.login() == True:
            print(self.__account_number)
        else:
            print("Not Allowed!")

    def __internal_method(self):
        print("Private Method")
        print(self.__account_number)
        self.show_me_account_number()

    def priv_method(self):
        self.__internal_method()



icici = Bank(9876543210, 100, password=input())
# icici.__init__()
icici.deposit(100)
icici.check_balance()
icici.show_me_account_number()
icici.show_me_account_number()
icici.deposit(100)
icici.check_balance()
icici.priv_method()

# icici.__internal_method() - Error









