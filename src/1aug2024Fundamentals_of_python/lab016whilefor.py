#lab50

i=0
while i< 10 :
    i = i + 1  # condition for next i changing or incrementing if not 0 be printed continiously
    print(i, end="") #1-10 last no is 10
b=0
while b<10:
    print("b",b)
    b=b+1 # 0-9 last no is 9

for i in range(0,10):
    print(i)
    if i==5:
        break

for t in range(10):
   if t==6:
    print(t)
   else:
       print("no o/p")

for n in range(0,20,1):
    if n==4  or n==3 or n % 2==0 :
        print(n)
    else:
        pass
