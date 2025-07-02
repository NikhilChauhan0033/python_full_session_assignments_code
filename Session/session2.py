#concatination + 

firstName = "Nikhil"
lastName = "Chauhan"

print(firstName+" "+lastName)

name = "Nikhil"
print("My Name Is"+" "+name)

#type casting (conversion bettwens data types)
#str()
#int()
#float()
#bool()

name = "Nikhil"
age = 21
print("My Name Is"+" "+name+" "+ "And My Age Is"+" "+ str(age)) #convert the age int to str

a= "10"
b= "20"

#Output 30

print("sum ="+" "+str(int(a)+int(b)))

#another way 

ans = int(a)+int(b)
print("sum ="+" "+str(ans))

#user input  #input is taking by default value in string

name = input("Enter Your Name : ")
print("My Name is" + " " + name)

#addition of 2 numbers
num1 = input("Enter Your 1st Number : ")
num2 = input("Enter Your 2nd Number : ")

print("sum = "+str(int(num1)+int(num2)))

#indexing
c = "Hello"
print(c[4])
print(len(c))

# print last latter of print
inp = input("Enter Your String")
leng = len(inp)-1
print(inp[leng])

#another way
print(inp[len(inp)-1])

#string methods
m = "hello"
print(m.upper())

n = "HELLO"
print(n.lower())

o = "   Hello   "
print(o.strip())    #remove the extra spaces

p = "hallo"
print(p.replace("a","e"))


p = "Hello Nikhil"
print(p.replace("Hello","Hi"))  #replace the full word





