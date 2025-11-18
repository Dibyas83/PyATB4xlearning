#lab 68
num1=int(input("enter the no 1"))
num2=int(input("enter the no 2"))
num3=int(input("enter the no 3"))
def sum_of_three_no(num1,num2,num3):
    return num1+num2+num3
result1=sum_of_three_no(num1,num2, num3)
print(result1)
num1=int(input("enter the no 1"))
num2=int(input("enter the no 2"))
num3=int(input("enter the no 3"))
result2=sum_of_three_no(num1,num2,num3)
print(result2)

def sum_of_three_no(a=5,b=4,c=8):
    return a+b+c
result1=sum_of_three_no(c=11)
print(result1)

result2=sum_of_three_no(a=22,b=33,c=44)
print(result2)

