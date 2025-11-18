

# try - except - else - finally
# file
import os

try:
    full_path  = os.getcwd() # The line full_path = os.getcwd() in Python gets the current
    # working directory and stores its absolute path as a string in the variable full_path.
    # This is done by first importing the os module and then calling its getcwd() function, which
    # returns the full path from the system's root directory.
    full_path_file = full_path + "/example.txt"
    print(full_path_file)

    file = open(full_path_file,"r") # Filenotfounderror
    print(file.read())
except Exception as fnfe:
    print("File not found")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)

# operating system - files, path related to the OS

# print(os.name) # posix - unix based - system mac or linus, windows - nt
# if os.name == 'posix':
#     print("using mac")
# else:
#     print("windows")

# print(os.getcwd())
# os.chdir("/Users/promode/Downloads/postman_collections/project1")
# print(os.getcwd())
# os.mkdir('new_directory')
# os.makedirs('parent/child/grandchild')
# print(os.listdir('.'))
# for file in os.listdir('.'):
#     print(file)


# os.remove('example.txt')
# os.rmdir('new_directory')

# os.rename('old_name.txt', 'new_name.txt')

full_path = os.path.join('/Users/promode/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024', 'file.txt')
# "/Users/promode/PycharmProjects/PyATB4xLearning/src/Sept/ex_10092024/file.text"


print(full_path)

print(os.path.exists('file.txt'))

print(os.path.isfile('file.txt'))

print(os.path.isdir('directory_name'))


class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number\n"))
        except Exception as e:
            print("Enter int only value of a")
        else:
            print(a)
        finally:
            print("FINALLY : Anyhow I will be printed")


x = XYZ()
x.f1()
