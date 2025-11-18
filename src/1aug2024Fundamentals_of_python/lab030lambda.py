
import math

# A lambda in Python is a small, anonymous, single-expression function that can take any
# number of arguments but only has one expression

def triple_me(num):
     return num ** 3
print(triple_me(4))

o = lambda num: num ** 3
print(o(10))

# Using a lambda function to double a number
double = lambda x: x * 2
print(double(5))  # Output: 10

# Using a lambda function with filter to get only odd numbers
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5]

oo = lambda a, b: a * b
print(oo(3, 4))

check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(11))

odfil = list(filter(lambda v:v%2==0 and  v<5,numbers))
print("odfil",odfil)

c = lambda e: "o" if e%2 != 0 else "e"
print(c(44))

op2 = lambda : math.pow(int(input("Enter the the number\n")),2)
print(op2())

op1 = lambda: math.pow(int(input("enter the Dragon: \n")),3)
print(op1())

# The function returns e raised to the power of x
ot = lambda: math.exp(int(input("enter the Dragon: \n")))
print(ot())
print(math.exp(8))

ot1 = lambda: math.comb(int(input("enter the Dragon: \n")),3)
print(ot1())

# converts an angle from radians to degrees. * 57
ot2 = lambda: math.degrees(int(input("enter the Dragon: \n")))
print(ot2())


