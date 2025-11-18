#chaining decorators

def decorator1(func):
    def wrapper():
        print("decorator 1")
        func()
        print("decorat")
    return wrapper()

def decorator2(func):
    def wrapper():
        print("decorator 2")
        func()
    return wrapper()


@decorator1
@decorator2
def say_hello():
    print("hello!")




