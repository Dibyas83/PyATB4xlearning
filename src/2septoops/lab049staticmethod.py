
# Static Methods
# A static method is a method that belongs to a
# class rather than an instance of the class.
class Op:
    @staticmethod
    def sum(a, b):
        return a + b


class MathOperations(Op):

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


# Non Static in Nature - Object creation is mandatory
object_ref = MathOperations()
output = object_ref.div(10, 5)
output2 = object_ref.mul(10, 5)
output3 = object_ref.sum(10, 5)
output4 = object_ref.sub(10, 5)
print(output)
print(output2)
print(output3)
print(output4)

# Static methods can be called direclty without the Object.
print(MathOperations.sum(4, 5))
print(MathOperations.sub(4, 5))
print(Op.sum(4, 5))



class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")


class TC1:
    def runTC(self):
        ExcelReader().readExcelFile()
        MYSQLDBConnection.readMySQLFile()


tc1 = TC1()
tc1.runTC()





