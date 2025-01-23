
"""
it remembers insertion order or how we entered

"""
from collections import OrderedDict,defaultdict

d= {"addres":"ka","asd":4,"we":5,"qw":7,"dff":77}
print(d)
d["age"] =36
d["id"] = 234
d["name"] = "rahul"
print(d)
od =OrderedDict()
od["age"] =36
od["id"] = 234
od["name"] = "rahul"
print(od)

dd = defaultdict(int)
print(dd)
dd["age"] =36
dd["id"] = 234
dd["name"] = "r"
print(dd)













