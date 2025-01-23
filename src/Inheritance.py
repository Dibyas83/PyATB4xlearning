


# acquiring the attributes and behsviour from anather class

# child inheriting from parent,
"""
single inheritance
multiple inheritance
multi level inheritance
heirarchical inh
hybrid inh
"""

class Father:
     key = "2bhk"
     def car(self):
         print("father car ","alto")
         print("father car ",self.key)


class Son(Father):
    key = "3bhk"

    def home(self):
        print("4bhk")


fatherobj = Father()
sonobj = Son()
sonobj.car()

# multilevel inheritence

class Mother:
    gold = "2kg"

    def house(self):
        print("1bhk",self.gold)

class Graandf(Mother):
    diamond = "22crt"

    def bike(self):
        print("honda")


class Father1(Graandf):
    btc = "ibtc"

    def crow(self):
        print("eat")

s = Father1()
d = Graandf()
s.bike()
s.house()

# multiple inheritence

class Wee:

    def wee_money(self):
        return 4

class Zee:

    def zee_money(self):
        return 6

class Son1(Wee,Zee):

    def total(self):
        print(Wee.wee_money(self) + Zee.zee_money(self))


cv = Son1()
cv.total()
print(cv.zee_money())
print(cv.wee_money())




"""

class M:

    def __init__(self,money1):
        self.money11 = money1


        # return 2

class N:
    def __init__(self,money2):
        self.money12 = money2
        #return 3


class O(M, N):

    def __init__(self,money1,money11,money12):
        super().__init__(money11)
        super().__init__(money12)
        self.money1 = money1

    def total(self,money11,money12):
        print(money11 + money12)

tot = O(3,4)
tot.total()

"""







