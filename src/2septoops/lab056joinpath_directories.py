import os

full_path_file = os.path.join("/Users/lenovo/PycharmProjects/PyATB4xLearning/src/2septoops", "pramod.txt")

file = open(full_path_file,'r')
content = file.read()
print(content)


#os.path.join() is a Python function that concatenates multiple path components into a single path in a way
# that is compatible with the operating system on which the code is running

path = os.path.join('C:\\Users\\user', 'documents', 'file.txt')
print(path)

"""
with open(...) as file:: This is a context manager in Python. It ensures that the file is properly closed 
after its block of code is executed, even if errors occur. This is a recommended practice for file handling 
as it prevents resource leaks
"""
try:
    with open("TestData.txt", "w+") as file:
        file.write("Hello How are you")
        file.seek(0)
        content = file.readlines()
        print(content)
        for col in content:
            print(col[0], col[1], sep="|")
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    try:
        file.close()
    except NameError as ne:
        print("NE")


"""
'w+': Opens a file for both writing and reading. If the file exists, its contents are erased. If the file 
does not exist, it is created.
'r+': Opens an existing file for both reading and writing. If the file does not exist, a FileNotFoundError 
is raised.
file.seek(0): After writing, the file pointer is at the end of the file. You must use file.seek(0) to reset 
the pointer to the beginning before you can read the file's contents.
with open(...) as file:: Using with is the recommended way to handle files, as it automatically closes the 
file for you, even if errors occur. 

"""
print("--------------------------------------------2")
try:
    with open("TestData.txt", "a") as file:
        file.write("Hello How are you")
    with open("TestData.txt", "r") as file:
        file.seek(0)
        content1 = file.readlines()
        print(content1)
        file.seek(0)
        print("----------------------")
        for col in content1:
            print(col[0], col[1], sep="|")
        print("--------------------------")
        file.seek(0)
        lines = file.readlines()
        for line in lines:
            print(line, end="")
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    try:
        file.close()
    except NameError as ne:
        print("NE")


