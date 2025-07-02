list1 = []

inp1 = input("Enter Some text : ")
# print(inp1)

inp2 = input("You want add y/n : ")

def fun1():
    if(inp2 == "y"):
        list1.append(inp1)
        print("added")
    else:
        list1.clear()
        print("not added")

fun1()
print(list1)

inp3 = input("Do yo want to delete any text y/n : ")
inp4 = int(input("Enter index number  : "))


def fun2():
    if(inp3 == "y"):
        list1.pop(inp4)
        print("removed")
    else:
        print("not removed")

fun2()
print(list1)




