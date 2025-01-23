#decorators in python
#two parts wrapper and call
def add_security(func):

    def wrapper():
      print("1.before the function is called")
      print("2.Add helmet,gloves ,guard")
      #drive bike
      func()
      print("3.after function is called")
      print("4.secure driving")

    return wrapper()
@add_security
def drive_scooty():
    print("normal function")

