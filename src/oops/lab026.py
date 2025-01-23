def add_before_after(custom_function_where_you_want_extra_function):

    def wrapper():
        print("before running ui")
        print("start the browser")
        custom_function_where_you_want_extra_function()
        print("ending ui")
        print("quit the browser")

    return wrapper()
@add_before_after
def test_ui():
 print("i will test the ui")