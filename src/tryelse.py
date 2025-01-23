
try:
    a = int(input())
    b = int(input())
    c = a / b

except ValueError as ve:
    print("dont print string")
except ZeroDivisionError as z:
    print("dont print  0 ")
else:
    print(c)
finally:
    print("end of program")

print("------------------------------------------------1")
try:
    file = open('example.txt', 'w')
    file.write("finally")
    file = open('example.txt', 'r')
    print(file.read())
    ty = open("rt.txt", 'r')
    print(ty.read())
except FileNotFoundError as fnfe:
    print("file not found")
finally:
    try:
        file.close()
    except NameError as n:
        print(n)

print("--------------------------------------------2")

import os
try:
    full_path = os.getcwd()
    full_path_file = full_path + "/example.txt"
    print(full_path_file)

    file = open(full_path_file, 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("file not found")
finally:
    try:
        file.close()
    except NameError as n:
        print(n)

















