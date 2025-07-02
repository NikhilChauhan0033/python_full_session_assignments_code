for i in range(1,11):
    print(i,end="") #for output in one line
    
for i in range(1,11):
    print(i,end=" ") #give space inside end=" "

for i in range(1,11):
    print(i,end="-")  #give -


# start pattern (*)

for a in range(1,6):        #outer loop (row)
    for b in range(1,6):     #inner loop (column)
        print("*",end=" ")  #start
    print()                  #for next line


#task 1 print pattern
# *
# **
# ***
# ****
# *****

for c in range(1,6):
    for d in range(1,c+1):
        print("*",end=" ")
    print()


#task 2 print pattern
# *****
# ****
# ***
# **
# *

for e in range(6,1,-1):
    for f in range(1,e):
        print("*",end=" ")
    print()

# another way for 2 #this 2 code give you a blank output
n1 = 10
for g in range(1,n1):
    for h in range((n1-1),0,g):
        print("*",end=" ")
    print()

# another way for 2
n2 = 5
for k in range(1,n2+1):
    for l in range(1,(n2+2),-k):
        print("*",end=" ")
    print()

# printing 
# 1
# 22
# 333
# 4444
# 55555

for m in range(1,6):
    for n in range(1,m+1):
        print(m,end=" ")
    print()

# printing
# 1
# 12
# 123
# 1234
# 12345

for m in range(1,6):
    for n in range(1,m+1):
        print(n,end=" ")
    print()

#task 3 print
# 1
# 12
# 121
# 1212
# 12121

for o in range(1,6):
    for p in range(1,o+1):
        if(p % 2 ==0):
            print(2,end=" ")
        else:
            print(1,end=" ")
    print()

#task 4 print
# 1
# 23
# 456
# 78910

n3 = 1
for q in range(1,5):
    for r in range(1,q+1):
        print(n3,end=" ")
        n3 += 1
    print()

#task 5 print
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

for s in range(1,6):
    for t in range((6-s),0,-1):
        print(" ",end="")    #space
    for y in range(1,s+1):
        print("*",end=" ")   #star
    print()

#           *
#         * *
#       * * *
#     * * * *
#   * * * * *

for s in range(1,6):
    for t in range((6-s),0,-1):
        print("  ",end="")  #double space
    for y in range(1,s+1):
        print("*",end=" ")  #star
    print()

# printing
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *


for s in range(5,0,-1):
    for t in range((6-s),0,-1):
        print(" ",end="")  #double space
    for y in range(1,s+1):
        print("*",end=" ")  #star
    print()

