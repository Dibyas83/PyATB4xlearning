
"""
to use module - import
to use anaher package - from xpackage import ymodule
built ins are standard library by default in python
pip install/uninstal matlab selenium
pip list
only available to project

pip freeze > requirements.txt
pip install -r requirements.txt
req.txt is like pom.xml in java
pip --help
pypi.org  gives all packages
openai  to work with ai

"""

"""
Collections- premade data structure -imports
 python provide collections  as 
 deque -for double ended que,FIFO, same as list with endpoint
 defaultDict
 namedtuple 
 Counter
 OrderedDict
 Chainmap

"""


from  collections import deque

d = deque()
d = deque([1,2,3,4])
print(d)
# we can add element from left and right
d.appendleft(1)
d.append(5)
d.extend([6,7,8]) # it adds a list
print(d)
d.popleft()
print(d)






