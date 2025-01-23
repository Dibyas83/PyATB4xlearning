"""
w -new create
a - append
b - binary
+ = update
readline - single line
readlines - all line

"""
import os

file = open('example.txt','r')
# file = open(/Users\a2z\PycharmProjects\PyATB4xlearning/src/new directory','r') giving path if in other directory
# full_path = os.path.join(":\Users\a2z\PycharmProjects\PyATB4xlearning\src\new directory",'example.txt') or give full path
# file = open(full_path,'r')
content = file.read()
content1 = file.readlines()
for line in content1:
    print(line,end=" ")
print(content)















