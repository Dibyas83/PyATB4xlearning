
# Inheritance

class Father:
    key = "2BHK"
    def car(self):
        print("Father Car!!", "ALTO",self.key)


class Son(Father):
    key2 = "3BHK"

    def home(self):
        print("3BHK")

    def truck(self):
        print("Truck")


father_obj = Father()
father_obj.car()
#print(father_obj.key2)
#father_obj.truck()

son_obj = Son()
son_obj.car()
print(son_obj.key2)
print(son_obj.key)


# Multilevel Inheritance

class GrandFather:
    gold = "2kg"

    def bhk1(self):
        print("1BHK")


class Father1(GrandFather):
    diamond = "22 karat"

    def bhk2(self):
        print("2BHK")


class Son1(Father1):
    btc = "1BTC"

    def bhk3(self):
        print("3BHK")


s = Son1()
f = Father1()
gf = GrandFather()

s.bhk3()
s.bhk2()
s.bhk1()

# Multiple Inheritance
class Father2:
    key = "ABC"
    __passowrd = "private"

    def __show_password(self):
        print(self.__passowrd)
    def father_money(self):
        return 5

    def home(self):
        return "This is from the Father"

    def show_everything(self):
        self.__show_password()



class Mother2:
    def mother_money(self):
        return 2

    def home(self):
        return "This is from the Mother"


class Son2(Mother2, Father2):  # MRO - Method resolution Order
    pass


class Son3(Father2, Mother2):
    pass


s = Son2()
s2 = Son3()
print(s.father_money())
print(s2.father_money())
print(s.mother_money())
print(s.home())
print(s2.home())

print(s.key)
s.show_everything()


# Hierarchical Inheritance , hybrid

class Father:
    def BHK1(self):
        print("1BHK")
    def jk(self):
        print("l")
    def h(self):
        print("o")

class Pramod(Father):
    def BHK2(self):
        print("2BHK")
    def jk(self):
        print("p")

class Amit(Father):
    def BHK3(self):
        print("3BHK")
    def jk(self):
        print("a")

class Lucky(Pramod,Amit):
    def no_house(self):
        print("NO house")
    #def jk(self):
       # pass

pramod = Pramod()
pramod.BHK1()
pramod.BHK2()

amit = Amit()
amit.BHK1()
amit.BHK3()
# amit.BHK2()? This belong to Pramod

luck = Lucky()
luck.no_house()
luck.BHK1()
luck.jk()
luck.h()
