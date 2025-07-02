#Advanced python

#list comprehension 
#write 1 to 100 inside list give below method is right but to long using  ist comprehension  you can do in easy way

li1 = []
for i in range(1,101):
    li1.append(i)

print(li1)

# using list comprehension write a 1 to 100 inside list
# output is known as print part means what ever you write inside the print you have to write
li2 = [i for i in range(1,101)]  #here first you have to write the print means what you have to print #write output first
print(li2)
print()

li2 = [10 for i in range(1,101)]   #here print 10 100 times
print(li2)
print()

li2 = ["*" for i in range(1,101)]  #here print * 100 times
print(li2)
print()

li3 = list(range(1,101))   #another way using range() function you can direct write range inside function 
print(li3)
print()

# ternory operator
#left side output and right side condition 

age = 12
ans = "you can vote" if(age<= 18) else "you can't vote"
print(ans)
print()


#task 
li4 = [2,4,3,5,34,8,11]

# li5 = [2,4,9,25,34,8,121] #output will be this
        #output                     #condition
li5 = [j**2 if(j % 2 != 0) else j for j in li4 ]    #first we write output then condition then loop
print(li5)
print()

# lambda function / anonymous frunction [single line function] [use for only sort [small] function]
#lambda function always return a value so store it

def fun1(name):
    return f"Hello {name}"
print(fun1("Nikhil"))
print()

# using lambda function
# abc is my function name 
# initiate of def we write lambda after that patameters and print part
abc = lambda name: f"Hello {name}"
print(abc("Nikhil Chauhan"))
print()


# addition of 2 number using lambda from user

add = lambda num3,num4 : num3+num4   #parameter

num1 = int(input("Enter Number 1st : "))
num2 = int(input("Enter Number 2nd : "))
print(f"sum = {add(num1,num2)}")   #argument
print()

# map and filter

#filter use for condition
# map is use for performance like add multi etc for all number
# input length == output length then use map 
# otherwise use filter [means if input length is not  equal to output lengthuse filter]

#filter

li6 = [10,3,4,55,52,12,5]

# given below is normal way 

# def fun2(m):
#     return m >= 20
# li7 = list(filter(fun2),li6)

# using filter
# printing greater than 20
li7 = list(filter(lambda n : n >= 20,li6))
print(li7)
print()

# map
# square of all [10,3,4,55,52,12,5]
li8 = list(map(lambda m:m**2,li6))
print(li8)
print()

# squre only which is even from [10,3,4,55,52,12,5]
li9 = list(map(lambda p:p**2 if(p%2==0) else p,li6))
print(li9)
print()


# given below is assignment [which completed in class]

li9 = [
    {"name":"Nikhil","email":"Nik03@gmail.com","marks":100},
    {"name":"Krutik","email":"Krutik03@gmail.com","marks":90},
    {"name":"Aadi","email":"Aadi03@gmail.com","marks":40},
    {"name":"Satish","email":"Satish03@gmail.com","marks":30}
]

# print only name from this list
li10 = list(map(lambda m:m["name"],li9))
print(li10)
print()

li11 = list(filter(lambda n:n["marks"]>=50,li9))
li12 = list(map(lambda j:j["email"],li11))
print(li12)
print()
# another way write in one line only 
li12 = list(map(lambda j:j["email"],filter(lambda n:n["marks"]>=50,li9)))
print(li12)





# # task for practice [given by nikhil]
# # sum of the numbers 

# li1 = [1,2,3,4,5,6,7,8,9,0,11,1111,222,33,456,78,9098,66]   

# # ans with list
# li3 = [sum(map(lambda b:b,li1))]
# print(li3)

# # another way  [ans without list]
# li1 = [1,2,3,4,5,6,7,8,9,0,11,1111,222,33,456,78,9098,66]
# li3 = sum(map(lambda b: b, li1))
# print(li3)

# #  Simplest version without map() using sum() function

# li1 = [1,2,3,4,5,6,7,8,9,0,11,1111,222,33,456,78,9098,66]
# li3 = sum(li1)
# print(li3)