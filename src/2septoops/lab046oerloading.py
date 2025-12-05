
# object is father of every class
# every cass is a object class
class MathUtils(object):  # is- A object - single inheritnace
    # Method - overloading - Not supported!
    # def add(self, a, b):
    #     return a + b
    #
    def add(self, a, b, c):
        return a + b + c

    def add(self, a, b, c=10, d=1): # by using default value method overlosading will be supported
        return a + b + c + d


math = MathUtils()
op1 = math.add(1, 2) # latest def
print(op1)











