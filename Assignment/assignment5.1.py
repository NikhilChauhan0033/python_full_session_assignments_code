# printing
#  * * * * * 
#   * * * * 
#    * * *
#     * *
#      *

for a in range(5,0,-1):
    for b in range((6-a),0,-1):
        print(" ",end="")
    for c in range(1,a+1):
        print("*",end=" ")
    print()

print()

# printing
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *

for d in range(5,0,-1):
    for e in range((6-d),0,-1):
        print("  ",end="")
    for f in range(1,d+1):
        print("*",end=" ")
    print()

print()

# printing
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *

for g in range(1,6):
    for h in range((6-g),0,-1):
        print("  ",end="")
    for i in range(1,g+1):
        print("*",end=" ")
    print()
print()

# printing
#      1
#     2 3
#    4 5 6
#   7 8 9 10
n1 = 1
for j in range(1,5):
    for k in range((6-j),0,-1):
        print(" ",end="")
    for l in range(1,j+1):
        print(n1,end=" ")
        n1 += 1
    print()

print()

# printing 
# *
# * *
# *   *
# *     *
# * * * * *

n2 = 5

for y in range(1,n2+1):
    for z in range(1,y+1):
        if(z == 1 or y == n2 or y == z):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

# printing
#      *
#     * *
#    *   *
#   *     *
#  * * * * *

for m in range(1,6):
    for n in range((6-m),0,-1):
        print(" ",end="")
    for o in range(1,m+1):
         if(o == 1 or m == 5 or m == o):
            print("*",end=" ")
         else:
            print(" ",end=" ")
    print()
print()


# printing 
# * * * * * *
# *       *
# *     *
# *   *
# * *
# *

for p in range(5,0,-1):
    for q in range(1,p+1):
        if(q == 1 or p == 5 or p == q):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
