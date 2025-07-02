# # starting module
# # module is a connection of multiple functions
# # library is a connection of module functions
# # framework is a connection of library functions

# # 3 types of module
# # 1. inbuild module
# # 2. user defined module
# # 3. install module

# # take any inbuild function name which is need to use and search of goole and read the documents [seracg like this time.pypi]

# import time #time is inbuild module

# print(type(time))   #type = module

# #igoner the [__something__] part bcz it not part of use
# print(dir(time)) #[open list inside list all the function is available which is time module store] use of dir() is to extract all function from module

# print() #for next line

# # use the inbuld function
# print(time.localtime())

# # use of sleep inbuild function
# print("Nikhil")
# time.sleep(3)    #wait for 3 sec
# print("Chauhan")

# # lockscreen type code if id is true then access otherwise tryagain after 3 attempt 3 second wait then return to enter id
 
# correct_id = "nikhil@gmail.com"
# i = 1
# sleep = 3   #initial sleep value

# while True:
#     id1 = input("Enter Your id : ")

#     if(id1 == correct_id):
#         print("Hey Welcome!!")
#         break
#     elif(i == 3):
#         print("Sleep mode...")
#         time.sleep(sleep)
#         i = 1                           #reinitialize i value reset to  1
#         sleep += 3                      # increment initial sleep value by 3
#     elif(id1 != correct_id):
#         print("Try agian...")
#         i += 1


# new module re

# re = regular expression [use for validation] 

import re
# print(dir(re))  #use of dir() is to extract all function from module
# print()
# re is also known regx [like javascript regx]

x = input("Enter Your Password : ")
y = True

while y:
    if(len(x)<=6 or len(x)>=12):
        break
    elif(not(re.search('[A-Z]',x))):
        break
    elif(not(re.search('[a-z]',x))):
        break
    elif(not(re.search('[0-9]',x))):
        break
    elif(not(re.search('[@$%^&]',x))):
        break
    else:
        print("Valid Password!!")
        y = False

if(y):
    print("Invalid Password!!")


# starting user defined module location [session12 folder]
