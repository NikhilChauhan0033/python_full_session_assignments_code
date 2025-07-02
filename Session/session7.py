# for loop
# by default for loop increment

for i in range(10):
    print(i)

for j in range(1,11): #give start position and end position
    print(j)

for a in range(1,11,2): #give start position and end position and give steps then means it jump if you give value 2 it is print 1+2=3 , 3+2=5...........
    print(a)

for b in range(11,0,-1):
    print(b)

# read list using for loop

li1 = [10,20,30,40]
for c in li1:
    print(c)

#another way

li3 = [10, 20, 30, 40, 50, 60]
for d in range(len(li3)):
    print(li3[d])

# read list using while loop
li2 = [10, 20, 30, 40,50]
i = 0 

while(i < len(li2)):  
    print(li2[i])  
    i += 1  

# sum of 1st ten naturals number [naturals number start from 1]

sum1 = 0

for e in range(1,11):
    sum1 = sum1+e

print(sum1) #ans is 55

# multiplication of list numbers

li = [10, 20, 30 ,40 ,50]

mul = 1

for f in li:
    mul = mul*f

print(mul)

#print highest  number
 
li4 = [10,2,3,0,77,0,99,249]

h = li4[0]

for g in li4:
    if(g>h):
     h=g

print(h)

#print lowest  number

li5 = [10,2,3,77,99,249,-1]

k = li5[0]

for l in li5:
    if(l<k):
     k=l

print(k)

# print the 1st and last index of 3. [code need to be dynamic]
li6 = [3,4,5,33,55,23,2,44,3,7,6,3]

li7 = []

for m in range(len(li6)):
    if(li6[m] == 3):
        print(m) #here u can get all 3 index number
        li7.append(m)


print(li7)
print(li7[0]) #here you u can find       first and last
print(li7[-1]) #is known as len(li7)-1
