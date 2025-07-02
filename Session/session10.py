# function in python
# use of function is to you create a function store the code inside function and you can use repeted when ever you want 

# user defined function 

def fun1():   #fuction declaration
    print("Nikhil Hello") 

fun1()  #function call

# parameters and arguments

def add(a,b):    #parameters
    print(a+b)

add(10,20)    #arguments

# using user input

def addd(c,d):
    print(c+d)

c = int(input("Enter num1 :"))
d = int(input("Enter num1 :"))

addd(c,d)

def min(e,f):
    print(e-f)

min(120,20)  #ans 100

def multi(g,h):
    print(g*h)

multi(10,20)   #ans 200

def divi(i,j):
    print(int(i/j))     #use int for remove float[decimal] number

divi(10,5)  #ans 2

# task print the highestnumber
def highestNum(inp1,inp2,inp3):
    if(inp1>inp2 and inp1>inp3):
        print(f"{inp1} is highest number")
    elif(inp2>inp1 and inp2>inp3):
        print(f"{inp2} is highest number")
    else:
        print(f"{inp3} is highest number")

k = int(input("Enter Number 1 : "))
l = int(input("Enter Number 2 : "))
m = int(input("Enter Number 3 : "))

highestNum(k,l,m)


#return keyword 
# remeber when ever you use return keyword its convert your function to a value and always you have store a return function

def add1(a,b):
    return a+b

ans = add1(20,10)    #store the return fun
print(f"sum = {ans}")   #ans is sum = 30

# task find the mid value

def middValue(n,o,p):
    if(n <= o <= p) or (p<= o <= n):
        return o
    elif(o <= n <= p) or (p <= n <= o):
        return n 
    else:
        return p

inp1 = int(input("Enter Number 1 : "))
inp2 = int(input("Enter Number 2 : "))
inp3 = int(input("Enter Number 3 : "))


ans1 = middValue(inp1,inp2,inp3)
print(ans1)

# while True [when to use if you dont no the when to stop the code and you dont no the condition then use]

i = 1
while True:
    if(i == 11):
        break
    print(i) #ans is 10
    i += 1

# create a calculator

def add(a,b):
    return a+b
def sub (a,b):
    return a-b
def multi(a,b):
    return a*b
def divi(a,b):
    return a/b

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
n3 = input("Enter operator (+,-,*,/) : ")

if(n3 == "+"):
    ans = add(n1,n2)
    print(ans)
elif(n3 == "-"):
    ans = sub(n1,n2)
    print(ans)
elif(n3 == "*"):
    ans = multi(n1,n2)
    print(ans)
elif(n3 == "/"):
    ans = divi(n1,n2)
    print(ans)
else:
    print("Invalid operators")


# another code

def add(a,b):
    return a+b
def sub (a,b):
    return a-b
def multi(a,b):
    return a*b
def divi(a,b):
    return a/b

while True:
    n1 = int(input("Enter Number 1 : "))
    n2 = int(input("Enter Number 2 : "))
    n3 = input("Enter operator (+,-,*,/) : ")

    if(n3 == "+"):
        ans = add(n1,n2)
        print(ans)
    elif(n3 == "-"):
        ans = sub(n1,n2)
        print(ans)
    elif(n3 == "*"):
        ans = multi(n1,n2)
        print(ans)
    elif(n3 == "/"):
        ans = divi(n1,n2)
        print(ans)
    else:
        print("Invalid operators")

    res = input("Do you want to continue (press : y) or (press any key to stop )").strip().lower()
    if(res !="y"):
        break