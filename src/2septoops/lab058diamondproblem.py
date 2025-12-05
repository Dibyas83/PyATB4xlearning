


class Wee:

    def money(self):
        return 4

class Zee:

    def money(self):
        return 6

class Son1(Wee,Zee):

    def total(self):
        pass

class Son2(Zee,Wee): # MRO

    def total(self):
        pass


cv = Son1()
cv2 = Son2()
cv.total()
print(cv.money())
print(cv2.money())














