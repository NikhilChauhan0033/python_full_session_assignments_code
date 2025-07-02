# Q.1 Write a Python Program to convert Tuple to a string.

tu1 = ("Nikhil",12,True,0.5)
print(tu1)
print(type(tu1))
tu2 = str(tu1)
print(tu2)
print(type(tu2))

# Q.2 Write a python program to print following output
# Given :- list1 = ["Name",["John",20,"tom",10],"subject",["Python","PHP"]]
# expected output : Name is john age is 20 and his subject is Python

list1 = ["Name",["John",20,"tom",10],"subject",["Python","PHP"]]
print(list1)
print(list1[0]+" "+"is"+" "+list1[1][0]+" "+"age is"+" "+str(list1[1][1])+" "+"and his"+" "+list1[2]+" "+"is"+" "+list1[3][0])

#Q.3 Read username with the input function and find the length of username

inp = input("Enter Your UserName : ")
print(inp)
print(len(inp))

# Q.4 Write python program to convert list into tuple
# Given :- y = [[["john","tom","taylor","kat","alex"]]]
# expected output : ('john', 'tom', 'taylor', 'kat', 'alex')

y = [[["john","tom","taylor","kat","alex"]]]
print(y)
z = tuple(y[0][0])
print(z)

# Q.5 Write a program to add item 7000 after 6000 in the following Python List
# list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(list2)
list2[2][2].insert(2,7000)
print(list2)

# Qs 6 Write a program to modify the ﬁrst item (22) of a list inside a following tuple to 222
# tuple1 = (11, [22, 33], 44, 55)
# Expected output:tuple1 : (11, [222, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)
print(tuple1)
tuple1[1].pop(0)
tuple1[1].insert(0,222)
print(tuple1)

#edit the tuple 1st item as 100

tuple2 = (10,20,30)
print(tuple2)
li = list(tuple2)
li.pop(0)
li.insert(0,100)
print(tuple(li))



