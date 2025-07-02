# exception handling / error handling
# exception handling use for handle error or exception
# how given below code is run if try does not found the a then it will error but the hello will run it is know as the error handling 
# if in website there is a minor then you whole website will crash so we have handel that minor error we use exception handling
# [if try part does not run else also not run] but finally run both side if try found a or not

# a = "nikhil" #uncomment for remove error  #after uncomment, comment for error handling

try:
    print(a)
except:
    print("Error mag")  #this is custom error msg

print("Hello")

# else [else run when only try run otherwise else doesn't run]

# a = "nikhil"  #uncomment for remove error  #after uncomment ,comment for error handling

try:
    print(a)
except:
    print("Error mag")  #this is custom error msg
else:
    print("hi")

print("Hello")

# finally [finally use bot side if there is error then also final run or no error then also run]
# a = "nikhil"  #uncomment for remove error

try:
    print(a)
except:
    print("Error mag")  #this is custom error msg  #after uncomment, comment for error handling
else:
    print("hi")
finally:
    print("Hello")

print("Hello")


# if you dont want custom error you can use python eror as msg

# b = "Krutik"  #uncomment for remove error #after uncomment comment for error handling

try:
    print(b)
except Exception as err:
    print(err)

print("Chauhan")

# there is 4 / 0 is not give error bcs you can divide 4 by 0 
# (if user enter 2nd value 0 so automatic give error to user bcz by default it is not true)
# but you can divide 0 by 4 ans = 0

d = int(input("Enter number 1 : "))
e = int(input("Enter number 2 : "))

try:
    print(d/e)
except Exception as err:
    print(err)



# find the greatest of 2 and if user enter str then give error

f = input("Enter num1 : ")
g = input("Enter num2 : ")

try:
    if(int(f) >int(g)):
        print(f"{f} is greater than {g}")
    else:
        print(f"{g} is greater than {f}")
except:
    print("Enter Number Only!!!")

