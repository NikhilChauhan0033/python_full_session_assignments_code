# whenever there is use of len() in loop is only for string not for integer

# for strings
# using for loop

inp1 = input("Enter Your Name : ")

for a in range(len(inp1)):
    print(inp1[a])

# # Another way

inp2 = input("Enter Your Name : ")

for b in inp2:
    print(b)

# printing numbers using for loop

inp3 = int(input("Enter a number : "))

for c in range(1,inp3+1):
    print(c)

# printing numbers using for loop

inp6 = int(input("ENter number : "))

for n in str(inp6):
        print(n)

# using while loop

inp4 = input("Enter Your Name : ")

d = 0
while(d < len(inp4)):
    print(inp4[d])
    d += 1

# printing numbers using while loop

inp5 = int(input("Enter a number : "))

e = 1
while(e <= inp5):
    print(e)
    e += 1

