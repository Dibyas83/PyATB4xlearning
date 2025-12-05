
# OrderedDict
# Dictionary that remembers insertion order'
from collections import OrderedDict, defaultdict

d = dict() #Normal Dict order not maintained
d["age"] = 78
d["name"] = "pramod"
d["id"] = 43
d["address"] = "KA"
print(d)

od = OrderedDict()
od['banana'] = 2
od['apple'] = 1
od['pear'] = 3
print(od)
print(od[2])

dd = defaultdict(int)
print(dd)

# OrderedDict maintains the sequence exactly as elements were added. This is particularly useful in
# applications such as JSON serialization, form field processing or displaying logs, where the order of
# items carries semantic meaning








