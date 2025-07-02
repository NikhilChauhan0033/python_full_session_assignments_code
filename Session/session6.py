#control statements [loops]

#there are 2 types of loops
# 1.while loop
# 2.for loop

# while loop
# 3 steps to write a while loop
# 1. initilize
# 2. condition
# 3. iteration

i = 1 #initilize
while(i <= 10): #condition
    print(f"Nikhil {i}")
    i += 1 #iteration / [increment]

#print number revers
l = 5
while(l >= 1):
    print(l)
    l -= 1

#task (print 15 table)
j = 1
while(j <= 10):
    print(15*j)
    j += 1

# task 2

a = 1
b = 4
while(a <= 5 and b<=8):
    print(f"{a},{b}")
    a += 1
    b += 2

#another way
c = 1
while(c <= 5):
    print(f"{c},{c+3}")
    c += 1


# task 
# *
# **
# ***
# ****
# *****

d = 1
while(d <= 5):
    print("*" * d)  #multiply star with the number
    d += 1

#task print odd number

e = 1
while(e <= 50):
    if(e % 2 != 0):
        print(e)
    e += 1

# task 
str1 = "nikhil"
f = 0
while(f < len(str1)):
    print(str1[f])
    f += 1

# task print reverse string
str2 = input("Enter a string : ")
k = len(str2) - 1 
while(k >= 0):
    print(str2[k])
    k -= 1

# task print odd task like 
# *
# ***
# *****

inp1 = int(input("Enter a number : "))
l = 1
while(l <= inp1):
    if(l % 2 != 0):
        print(l*"*")
    l += 1

