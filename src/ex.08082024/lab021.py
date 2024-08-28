#def print_arguments(*args):
#*arg=multiple argument with no limit,->list
#  print(args[0])
#for i in args:
    #print(i)

def make_pizza(*topings):
     for topin in topings:
         print(topin)

print("program started")
pramod=make_pizza("tomato","cheese","mushroom")
virat=make_pizza("cheese","olives","paneer")
print("program end")