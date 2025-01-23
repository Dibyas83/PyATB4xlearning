class A:

    def methodA(self):
        return "Methoda"


class B(A):

    def methodB(self):
        return "Methodb"


class C(A):

    def methodC(self):
        return "Methodc"


class D(B,C):

    def methodD(self):
        return "Methodd"


zx = D()
print(zx.methodA())



