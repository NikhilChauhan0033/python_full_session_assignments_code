# printing
#     *     
#   *   *   
# *       *
#   *   *
#     *

for a in range(1,6):
    for b in range(1,6):
        if(a+b == 4 or a-b == 2 or b-a==2 or a == b == 4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

# https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
# it is a ascii table
# there are numbers of your keyborad keys [keyborads values]

# if you want to find a ascii number using python use this 
# 2 ways to find 
# enter a key value like a,b,c,1,2,#,$
# or enter ascii number like 12 11 33 27 87

# give below you enter a keyborad key values you will get a ascii number.
print(ord("a"))
print(ord("1"))
print(ord("("))

# give below you enter a ascii number you will get keyborad key values.
print(chr(66))
print(chr(69))
print()

# k = 88 #you can with using ascii numbers
k = ord("A")  #you can with using latters
for c in range(1,6):
    for d in range(1,c+1):
        print(chr(k),end=" ")
        k += 1
    print()
print()  #for next line

# task sum of all the numbers which given in string
# ans is 21
# numbers range in ascii numbers from 48 ascii numbers to 57 ascii numbers

str1 = "abc123Nik456"

sum1 = 0

for i in range(0,len(str1)):
    j = ord(str1[i])   #convert string to ascii number
    if(j>=48 and j<= 57): #using condition get numbers using numbers of ascii numbers 
        k = chr(j) #convert ascii  numbers to main values like numbers
        l = int(k)  #convert to int
        sum1 = sum1+l  #sum of all numbers
print(sum1)    #ans 21
print()

# break and continue
# break is terminate if the condition is satisying
# continue is skip the condition is satisying 

z = "javascript"

for y in z:
    if(y == "s"):
        break #brack here bcz condition is satisfying 
    print(y)

z1 = "javascript"

for y in z1:
    if(y == "s"):  #skip the s and print rest of latters
        continue
    print(y)
print()

# task print square of numbers and if there is a numbers which module by 5 print there sorry and break
s = int(input("Enter a number"))
s1 = 1
while(s1 <= s):
    if(s1 % 5 == 0):
        print("sorry")
        break
    print(s1**2)
    s1 += 1
    
# task print square of numbers and if there is a numbers which module by 5 print there sorry and continue
# here 2 iterate

s = int(input("Enter a number"))
s1 = 1
while(s1 <= s):
    if(s1 % 5 == 0):
        print("sorry")
        s1 += 1 #itrate 1
        continue
    print(s1**2)
    s1 += 1 #itrate 2

# another way here only one iterate

# s = int(input("Enter a number"))
# s1 = 1
# while(s1 <= s):
#     s1 += 1  #iterate
#     if(s1 % 5 == 0):
#         print("sorry")
#         continue
#     print(s1**2)

