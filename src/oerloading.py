

class Mathutils(object):
    #  method overloading not supported
        def add(self,a,b):
            return  a + b

        def add(self, a, b, c=6):
            return a + b + c


math = Mathutils()
sum = math.add(1,2)
print(sum)











