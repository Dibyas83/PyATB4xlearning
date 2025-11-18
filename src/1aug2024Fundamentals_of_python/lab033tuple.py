


#t = tuple("h","m", "hi")
# TypeError: tuple expected at most 1 argument, got 3
t = tuple()
t1 = tuple("y")
print(t)
print(t1)

# Conversion List to Tuple
t1 = tuple(["pramod","amit","manisha"])
print(t1)

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
new_tuple = (hero1,hero2)
print(new_tuple)
print(new_tuple[0]) # ("Batman", "Bruce Wayne")
print(new_tuple[0][0]) # "Batman"
print(new_tuple[1][1]) # "Diana Prince"


# Search in Tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("New Delhi" in cities)


t = (12, 34, 56)
# t.append(12) # r: 'tuple' object has no attribute 'append'
my_list = list(t)
my_list.append(4)
t = tuple(my_list) # reassignment
print(t)
print(type, t)
print(type(t))


my_tuple = t + (4,)
print(my_tuple)

newtuple = my_tuple +(7,)
print(newtuple)

env_api_urls=(["abc.com/get"],["asd.com/post"],["vbv.com/put"])
print(env_api_urls)





