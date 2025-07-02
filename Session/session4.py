#set {}
#set is unorder
#not store duplicate values !important
#you can not changes using indexing (indexing does not support)

s1 = {10,20,30,"Nikhil",10}
print(s1)
print(type(s1))
print(len(s1))

#set methods

s2 = {10,20,30,40,50,60}
print(s2)

s2.add(70)
print(s2)
s2.update({80,90})
print(s2)
# you can use any brackets (),{},[]
s2.update([100,110])
print(s2)
s2.update((120,130))
print(s2)


s2.pop()
print(s2)
s2.remove(40)
print(s2)
# s2.remove(140) #here it is give a error bcz there no value 140 is not present in set 
print(s2)
s2.discard(40)
print(s2)
s2.discard(140) #here not present but not give you a error bcz there is no value you enter then it is not give a error it is printing the other values
print(s2)

del s2 #delete all the values #del is a keyword
# s2.clear() #delete all the values
# print(s2) #give you a error bcz we delete the all the values and variable then printing

#dict {} key value (key+value=pair)

di1 = {
    # key   #value 
    "name":"Nikhil", #pair (combination of key and values as known as pair)
    "age":21,
    "email":"nik03@gmail.com",
    1:"chauhan",
    "1":"satish"
}

print(di1)
print(type(di1))
print(len(di1))

print(di1["name"])  #if you want to print only name (enter a key)
print(di1["age"])  #if you want to print only age (enter a key)
print(di1[1])  #(enter a key as you writen)
print(di1["1"]) #(enter a key as you writen)

di1["name"] = "Nik"  #value update using key (if you wamt to update value use key)
print(di1)

#dict method
di1.update({"hobby1":"coding","hobby2":"dancing"}) #if you want to add a multiple data or a single data use this
print(di1)

di1.popitem() #delete the last item
print(di1)

di1.pop("age") #you can delete using key name
print(di1)

# di1.clear()
# print(di1)

a = di1.items() #if you want a all the key and values use this
print(a)
a = di1.keys() #if you want a all the only key use this
print(a)
a = di1.values() #if you want a all the only values use this
print(a)

#task when ever you have to insert values using empty set first define that it is set bcz when you try to create empty set it creatd by default a empty dictionary  
set1 = set() #define that this is set
print(type(set1))
inp1 = input("Enter Your Name")
inp2 = input("Enter Your LastName")

set1.update({inp1,inp2})
print(set1)