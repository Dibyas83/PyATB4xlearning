pb_global_b=12 #global variable
g="rr"
def my_function():
    pb_a=10
    g="ty"
    print(pb_a)
    print(pb_global_b)
    print(g)

def f1():
    print(pb_global_b)
    print(g)

my_function()
print(pb_global_b)
print(g)
f1()