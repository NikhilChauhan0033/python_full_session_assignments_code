# inp1 = input("Enter Your Name : ")  #enter hello
# # output
# # o
# # l
# # l
# # e
# # h

# for i in range(len(inp1)-1,-1,-1):
#     print(inp1[i])


# inp2 = input("enter a word : ")

# for b in range(len(inp2)):
#     if(b % 2 == 0):
#         print(inp2[b],end="")   #using end=" " for one line
# print()
# print()


# # # using filter and lambda frint number less than 20
# # li1 = [1,2,3,4,5,6,7,8,9,0,11,1111,222,33,456,78,9098,66]   

# # li2 = list(filter(lambda a:a<20,li1))
# # print(li2)


# # li3 = [sum(map(lambda b:b,li1))]
# # print(li3)


name = ["nikhil chauhan","krutik chauhan","aadi chauhan"]
print(name[0])

# if you want only nikhil that is first name 

name = ["nikhil chauhan","krutik chauhan","aadi chauhan"]
fname = []

for i in name:
    fname.append(i.split()[0])
    print(fname)