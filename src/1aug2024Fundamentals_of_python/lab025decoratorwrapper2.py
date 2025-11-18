

"""
In Python, a "wrapper" is typically a function that takes another function as an argument and returns a new function. This new function, called a decorator, can modify or extend the behavior of the original function without changing its source code. Wrappers are commonly used to add functionality like logging, error handling, or performance timing to a function before or after it executes.
How wrappers work
Define a decorator function: This outer function accepts one argument, which is the function to be wrapped.
Define a wrapper function: Inside the decorator, a new function is defined. This is the function that will be returned.
It includes the new behavior you want to add (e.g., printing a message before the original function runs).
It calls the original function, which was passed as an argument.
It can include additional behavior after the original function runs.
If the original function accepts arguments, the wrapper function should use *args and **kwargs to pass them along correctly.
Return the wrapper function: The decorator function returns the inner wrapper function.
Apply the decorator: You can use the decorator on a function by placing @decorator_name directly above the function definition. This is syntactic sugar for my_function = decorator_name(my_function).

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Call the decorated function
say_hello("Alice")

Output:
Something is happening before the function is called.
Hello, Alice!
Something is happening after the function is called.

Common use cases
Logging: Add a wrapper to log function calls, arguments, and return values for debugging.
Error handling: Use a try...except block within the wrapper to handle exceptions consistently across multiple functions.
Timing execution: Calculate and log the execution time of a function.
Access control: Restrict access to a function based on certain conditions.

"""
#decorators in python
#two parts wrapper and call
def add_security(func):

    def wrapper():
      print("1.before the function is called")
      print("2.Add helmet,gloves ,guard")
      #drive bike
      func()
      print("3.after function is called")
      print("4.secure driving")

    return wrapper()
@add_security
def drive_scooty():
    print("normal function")

@add_security
def drive_bullet():
    print("big function")


