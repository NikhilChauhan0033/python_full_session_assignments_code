#operators

# 1.arithmetic operators
# + - * / // %
a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b) #(you got an decimal values)
print(a//b) #(if you use double // thant you will not get decimal value)
print(a%b) #give a reminder
print(2**3) #{(**) means 2*2*2} [2 raised to the power of 3]

# 2.assignment operators
# = += -= *= /=

c = 10
print("C OUTPUT")

c += 2 #same as c = c+2
print(c)
c -= 2 #same as c = c-2
print(c)
c *= 2 #same as c = c*2
print(c)
c /= 2 #same as c = c/2
print(c)

# 3.comparison operators
# == != > >= < <=

d=10
e=10

print(d == e)
print(d != e)
print(d > e)
print(d >= e)
print(d < e)
print(d >= e)

# 4.logical operators (apply on conditions)
#and 
#or
#not

# in [and] case (if there is a 1 false in the [and] condition then your all condition is false)
# true and true = true
# false and false = false
# false and true = false
# true and false = true

# in [or] case (if there is a 1 true in the [or] condition then your all condition is ture)
# false and false = false
# true and true = true
# false and true = true
# true and false = ture

# in not() case 
#it is give the opposite of your original answer Like if your condition answer is true not(give you false) if your condition answer is false not(give you true)

f = 10
g = 20
print("LOGICAL OPERATORS")

print(f==10 and f>=g)
print(f==10 or f>=g)
print(g == f or f >= 5 and f >= g)
print(not(g == f or f >= 5 and f >= g)) 

#condition statement

#given below use for single statement
# age = int(input("Enter Your Age"))

# if(age>=18):
#     print("You Can Vote")
# else:
#     print("You Can't Vote")


# #given below use for nultiple statement
# num1 = int(input("Enter Your Number"))

# if(num1>=30):
#     print(f"{num1} is greater than 30")
# elif(num1>=20):
#     print(f"{num1} is greater than 20")
# elif(num1>=10):
#     print(f"{num1} is greater than 10")
# else:
#     print(f"{num1} is less than 10")

# num2 = int(input("Enter Your Number"))

# #given below is another method for multiple statement
# if num2>=6 and num2<=10:
#     print(f"{num2} is between 6 to 10")
# else:
#     print(f"{num2} is not in between 6 to 10")

# Task 1

# n1 = int(input("Enter Your 1st Number"))
# n2 = int(input("Enter Your 2nd Number"))

# if(n1>n2):
#     print(f"{n1} greater than {n2}")
# else:
#     print(f"{n1} less than {n2}")

# Task 2

# n3 = int(input("Enter Your Number"))

# if(n3>0):
#     print(f"{n3} is positive number")
# else:
#     print(f"{n3} is negative number")

# Task 3

# n4 = int(input("Enter Your 1st Number"))
# n5 = int(input("Enter Your 2nd Number"))
# n6 = int(input("Enter Your 3rd Number"))

# if(n4>n5 and n4>n6):
#     print(f"{n4} is greater than {n5} and {n6}")
# elif(n5>n4 and n5>n6):
#     print(f"{n5} is greater than {n4} and {n6}")
# elif(n6>n4 and n6>n5):
#     print(f"{n6} is greater than {n4} and {n5}")

# Task 4 (find the middle number)
n = int(input("Enter Your 1st Number"))
o = int(input("Enter Your 2nd Number"))
p = int(input("Enter Your 3rd Number"))

if(n <= o <= p) or (p<= o <= n):
    print(o)
elif(o <= n <= p) or (p <= n <= o):
    print(n)
else:
    print(p)