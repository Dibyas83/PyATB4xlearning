class Bank:
    def __init__(self):
        self.balance = 0 # publc attribute

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount # protected attribute

    def show_balance(self):
        print(f"Account balance: ", {self.balance})

account = Bank()
account.deposit(1000)
account.withdraw(500)
account.show_balance()


# refactor code to fix indentation
