def make_pizza(*topings,base):
    print(topings,base)

def make_pizza2(*topping,base):
    print(base,topping)

make_pizza("mushroom","tomato","cheese",base="thin crust")
make_pizza2("dddd","ffff","gddd",base="crust")