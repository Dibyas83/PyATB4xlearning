import time


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
def test_ui_1():
    print("time taken by function")
    time.sleep(2)#wait


@time_decorator
def test_ui_2():
    print("time taken by function")
    time.sleep(6)][]



