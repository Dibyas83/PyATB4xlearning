def outer_function():
    var1=30
    def inner_func():
        print(var1)

    def inner_func2():
        print(var1)

    inner_func()
    inner_func2()
outer_function()

my_shopping_list =["bread","milk","butter"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_list):
    more_item=input("Enter the item\n")
    my_list.append(more_item)
    return my_list

i=bring_more_food(my_shopping_list)
print(i)