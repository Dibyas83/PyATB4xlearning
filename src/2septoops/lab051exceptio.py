
# error handling,unexpectd error,error acceptance and continuing with program
# mentioning reason for error
# default exception(base exception) is given if specific error not understood
"""
:exception - Arithmeticerror - zerodivisionerror
                             - floatingpoointerror
            -Nameeerror
            -:exceptiongroup
            -Valueerror
            :typeerror
            -oserror - permissionerror
                    - filenotfounderror
            -runtimeerror

error is due to mistake in code,/ike syntax or logical flaws
exceptions accur during the execution of program-trying to divide by zero or invalid index in list or incomplete data

"""

#print(int("a")) # valuerror
mylist = [1,2,3,4,5]
# print(mylist[5]) #IndexError: list index out of range
a =int(input())
b=int(input())
c= a/b
print(c)
print("end of program")

# try - except - else - finally

try:
    a = int(input()) # valueerror
    b = int(input())
    c = a / b # zerodivisionerror
    print(c)
except Exception as e: # Exception class prints for any unknown  error

    print(e)
    print("please check inputs ,not string or zero")

print("end of program")

import  math

try:
    math.exp(1000) # Overflowerror : math range error
except Exception as e:
    print(e)
    print("use lower exponent value")



try:
    d=int(input())
    e = int(input())
    t = d/e
except Exception as e:
    print("input should be integer and non zero")





