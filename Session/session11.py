# recursion function
# recursion function call itself till condition is not satishfied

# def fun1():
#     print("Hello")
#     fun1()                #call itself

# fun1()

def countdown(n):
    if n == 0:  # Base case (stopping condition)
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)  # Recursive call (function call itself)

countdown(5)


# guess the number task

li1 = []

def guess_num(count):
    
    inp1 = int(input("Enter Number : "))
    ans = 34
    count -= 1
    if(count == 0):
        print("GAME OVER!!")
    else:
        print(f"Remaining Chances {count}")
        if(inp1 > ans ):
            print("Number is greater.")
            li1.append(inp1)
            print(li1)
            guess_num(count)
        elif(inp1 < ans):
            print("Number is less.")
            li1.append(inp1)
            print(li1)
            guess_num(count)
        else:
            print("Number is correct.")
            li1.append(inp1)
            print(li1)

guess_num(10)


# factorial [5*4*3*2*1 = 120]   [by default fact 0 value is 1]

def fact(num):
    if(num > 0):
        return num * fact(num-1)
    else:
        return 1
    
print(fact(5))

# # another way
# def fact(a):
#     if(a==1 or a == 0):
#         return 1
#     return fact(a - 1)*a 

# fact1 = fact(5)
# print(fact1)


