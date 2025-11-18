

import time

# Now you can use time module functions, for example:
# This will pause the script for 5 seconds
time.sleep(5)
print("Hello after 5 seconds!")

def time_decorator(func):

    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("time taken by function(end_time-start_time)")

    return wrapper()

@time_decorator
def best_ui_1():
    print("time taken by function")
    time.sleep(2) # wait

@time_decorator
def best_ui_2():
    print("time taken by function2")
    time.sleep(6)



# def test_ui_2(): does not work due to keyword test
