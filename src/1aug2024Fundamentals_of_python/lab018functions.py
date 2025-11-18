#lab61
#functions built in functions,user defined functions


#definition
def greet():
    print("hello!")

#calling
greet()

def greet_by_name(name):
     print("hello,",name.upper())
name=input("enter name\n")

greet_by_name(name)

def sum_of_two_no_default(num1=100,num2=200):
    return num1 + num2
def sum_of_two_no(num1,num2):
    return num1+num2
result=sum_of_two_no_default()
print(result)
result=sum_of_two_no(num1=20,num2=33)
print(result)