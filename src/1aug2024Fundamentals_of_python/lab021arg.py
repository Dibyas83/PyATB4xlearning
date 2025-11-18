def print_arguments(*args):
   #*arg = multiple_argument with no limit,->list,'args' is a tuple containing all positional arguments passed to the function
    print(args[0])
    for i in args:
        print(i)
i = print_arguments(1,2,3)

def make_pizza(*topings):
     for topin in topings:
         print(topin)

print("program started")
pramod=make_pizza("tomato","cheese","mushroom")
virat=make_pizza("cheese","olives","paneer")
print("program end")


def make_pizza1(*topings,base):
    print(topings,base)

def make_pizza2(*topping,base):
    print(base,topping)

make_pizza1("mushroom","tomato","cheese",base="thin crust")
make_pizza2("dddd","ffff","gddd",base="crust")



