

# try - except - else - finally

try:
    a = int(input()) # valueerror: fop
    b = int(input())
    c = a / b # zerodivisionerror:dot
    print(c)
except ValueError as e: # Exception class prints for any unknown  error

    print(e)  # default call
    print("please check inputs ,not string or zero")
except ZeroDivisionError as t:
    print(t)  # default call

    print("input should be integer and non zero")
else:
    print(c)
finally:
    print("the result will be executed")




