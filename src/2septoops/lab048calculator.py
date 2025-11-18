


class Calculat:


    def __init__(self):
        print("Calculator")

    def sum(self,a,b):
        return a + b

    def multi(self,a,b):
        return a * b

    def div(self,a,b):
        return a / b


object_ref = Calculat()
a = int(input())
b = int(input())
output_sum = object_ref.sum(a,b)
# output_sum = object_ref.sum(3,6)
output_div = object_ref.div(a,b)
# output_div = object_ref.div(5,6)
print(output_sum)
print(output_div)

print("----------------------------3222")

class Calcu:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("Calculator")

    def sum(self):
        return self.a + self.b

    def multi(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


object_ref = Calcu(3,4)
output_sum = object_ref.sum()
output_div = object_ref.div()
print(output_sum)
print(output_div)

print("----------------------------aa")
h = 10

class Sumation:
    b = 11

    def __init__(self,h,c):
        self.h = h
        self.c = c
        #self.b = b it is class var

    def sumat(self):
        print(self.h + 5)
        print(self.b + 5)
        print(self.c + 5)

ref = Sumation(h,6)
ref.sumat()


print("---------------------------------------1")

h = 10

class Summation:
    b = 11

    def __init__(self,c):
        #self.h = h
        self.c = c
        # self.b = b # it is class var

    def sumat(self):
        print(h + 5)
        print(self.b + 5)
        print(self.c + 5)

ref = Summation(6)
ref.sumat()
ref.sumat()
print("--------------------------------------2")

h = 10

class Sumation:
    b = 11

    def __init__(self,h,c):

        self.c = c


    def sumat2(self):
        global h
        h = h+2
        print(h)
        #print(b + 5)
        print(self.b + 5)
        #print(self.b + 5)

        print(self.b)
        print(self.c + 5)

ref = Sumation(h,6)
ref.sumat2()
























