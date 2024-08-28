# continue statement skips the current iteration of a loop and moves to the next iteration

for number in range(10):
    if number%2==0:
        continue
    else:
        print(number)

#match statement match the op and execute

browser_name =input("Enter the name of browser\n")
browser_name=browser_name.lower()
match browser_name:
    case "firefox":
        if browser_name=="firefox":
            print("hello firefox")
    case"chrome":
            print("hello chrome")
    case _:
        print("browser not found!")

user_type=input("Enter the user type,admin,guest,manager\n")
user_type=user_type.lower()
match user_type:
    case "admin"|"manager":
        print("hello sir")
    case "guest":
        print('hello,guest')
    case _:
        print("hello,there")


