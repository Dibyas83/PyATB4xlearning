class VWOloginpage:

    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg


    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "pass1234":
            print(" login successful")
        else:
            print("not allowed")


email = input("email dd = ")
password = input("password=")
vwo_obj = VWOloginpage(email,password)
vwo_obj.login_confirm()
xyz = VWOloginpage("pramod@gmail.com","pass1234")
ayz = VWOloginpage("prad@gmail.com","pass1234")
xyz.login_confirm() # object can call atrribute like class attribute and functions also
ayz.login_confirm()


