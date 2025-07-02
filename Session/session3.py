#string slicing (using slice you can get a words from full string)
a = "we are learning python"

#positive indexing (enter firstValue as a staring value : endValue)
print(a[0:6])
print(a[3:6])
print(a[3:])
print(a[:6])
#negative indexing
print(a[-2])
print(a[:-1])
print(a[::-1]) #use for reverse the string
print(a[::-2]) #skip 1 value and print next value
print(a[::-3]) #skip 2 value and print next value
print(a[-6:]) #print only python (using negative indexing (negative indexing starting from -1))

#NON - primitive data types (mutable (you can changes))
#1.list = []
#2.tuple = ()
#3.set {}
#4.dict {} 

#1.list = []
li1 = [1,2,"Nikhil",True,0.99] #list is mutable you can change
print(li1)
print(type(li1))
print(len(li1))

#tuple = () [only to list methods tuple have index,count]
tu1 = (1,2,"Nikhil",False,9.0) #tuple is immutable you can not change
print(tu1)
print(type(tu1))
print(len(tu1))


#list slicing
li3 = [10,20,30,40,50]
print(li3)
print(li3[0])
print(li3[0:3])
print(li3[2:4])
print(li3[1:])
print(li3[:4])
print(li3[:-1])
print(li3[::-1]) 

#nested list (means list inside list)
li4 = [10,[20,30],[40],50]
print(li4)
print(li4[0])
print(li4[1])
print(li4[1][1])
print(li4[2])
print(li4[2][0])
print(li4[3])

#list methods

li5 = [10,20,30,40,50,60,30,30]
li5.append(70) #add value at end
li5.insert(1,60) #add at index number (first value is index number and another the value which is you have to add)
li5.pop() #remove the last value
a = li5.pop(2) #remove using indexing pop save the deleted value
# print(li5) #uncomment for check
print(a)
b = li5.remove(30) #enter value which you have to remove
# print(li5) # not sav the value which is reoved #uncomment for check
print(b) #none means no value not save the value which is reoved
print(li5)

del li5[2] #enter indexing number to delete #del is a keyword

# li5.clear() #clear entire list 
print(li5)

# from the below code there is no item in list bcz list is empty bcz of clear() first cmnt clear() then run and run agian
li5.reverse()
print(li5)

c1 = li5.index(30) #give you the index number of the value
print(c1)
d = li5.count(30) #give you the count number of the value
print(d)

print(li5)

li6 = [10,20]
li7 = [30,40]

li6.append(li7)
print(li6)

li8 = [10,20]
li9 = [30,40]

li8.extend(li9)
print(li8)
