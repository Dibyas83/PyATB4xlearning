a=float(input("enter no a \n"))
b=float(input("enter no b \n"))
c=float(input("enter no c \n"))

if a>=b and a>=c:
    print("max is a")
elif b>=a and b>=c :
    print("max is b")
else:
    print("max is c")

    # grade calculator lab 41
score=int(input("Enter your score \n"))
if score>=90 and score<=100:
     print("grade is"," A")
elif score >=80 and score <=89:
    print("grade is","B")
else:
    print(("grade is F"))



