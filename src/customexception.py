


class Mycustomexception(Exception): # parent of all exception

    def __init__(self,msg):
        self.message = msg
        super().__init__(msg) # calling parents constructor --of  Exception

balance = 100
withdraw = int(input("amt to withdraw"))
if withdraw > balance:
    raise Mycustomexception("balance is low")
else:
    print(balance - withdraw)








