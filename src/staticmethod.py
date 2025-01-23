
# staticmethod

class Mathoperation:

    def div(self,a,b):
        return  a/b
    @staticmethod
    def sum(d,e):
        return d+e

class op:

    @staticmethod
    def sum(y,h):
        return y+h

out = Mathoperation()
output = out.div(4,2)
print(output)
print(Mathoperation.sum(4,5)) # called directly ,cannot call div.static belongs to class not object so no self required
print(op.sum(6,8))

print("-----------------------------1")

class Excelreader:

    @staticmethod
    def readexcelfile():
        print("read from excel")

class Mysqlreader:

    @staticmethod
    def readsql():
        print("read from sql")

class Tci:

    def runTci(self):
        Excelreader.readexcelfile()
        Mysqlreader.readsql()

tci = Tci()
tci.runTci() # can be done without inheritng Excelreader. generally staticmethod is used when common method like sum  and Excelreaderis used.








