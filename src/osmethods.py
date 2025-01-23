
import os
# helpsto work with files ,path related to os

print(os.name) # posix- unix based system,Nts -windows
if os.name == 'posix':
    print('using max')
else:
    print('windows')

print(os.getcwd())
#os.mkdir("new directory")
# os.makedirs('parent/child/grandchild')
# os.chdir("/user/a2z/collection")
print(os.listdir())
# os.removedirs("new directory")
# os.remove('example.txt')
full_path = os.path.join('/Users/a2z/PycharmProjects/PyATB4xlearning/src','example.txt')
full_path2 = os.path.join('/Users/a2z/PycharmProjects/PyATB4xlearning/src/basic py','example.txt')
print(full_path)
print(os.path.exists('example.txt'))








