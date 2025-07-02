# file handling
# means you can add , delete, read, write the files using python 
# you have to write code inside the opening and closing tags
# rember what ever task you want to perform for your txt file first check mode and cha nge the mode according to your task

# given below is mode of file handling
# r => read 
# w => write
# a => append
# r+ => read and write both [but you can use at time one operation that is read or write [so it is not more usable]]

# enter below  file name [inside open("filename.txt", "mode")]
# here is the mode "r" is by default mode means by default you can read file 
f = open("demo1.txt","r")    #opening tag

# first set mode to "r" for read

# a = f.read()         # if you want to read the file use this 
# print(a)   

# another way without storing
# print(f.read())  # if you want to read the file use this 

# if you want 1st 3 latters use this 
# print(f.read(3))  

# now here it is give first 3 and after 3 latters it is gives 6 means not first 6 after which present from there 6 latters
# print(f.read(3))  
# print(f.read(6))  

# given below read 1st line only
# print(f.readline())

# given below is read all the line [it is display in array bcz we read multiple lines]
# [\n stand for next line it show bcz of in txt file File after 1st line we press the enter key for next line]
# print(f.readlines())


# now we change mode for write [change mode at opening of file] ["w" mode]

# if you use write "w" mode then it is remove your all the old data[infromation] from the txt file 
# so when ever you use write first create multiple copy of txt file then write 
# rember once data is removed from txt file that not return means you can not undo or cntol+z nothing 
# it is permanently removed the data 
''''
# given below is old data 
Hello Nikhil
Hii Nikhil
Hello World
now we write inside demo1.txt then this data is removed and what ever you write it is uodated there 
'''
# f.write("Hello Chauhans")
# now check after run this command in the terminal you will get black and check your txt file you all the old data is removed and new data is inserted using write

# change mode for read
# print(f.read())

# rember when your mode "r" and you try to write then all the data removed from txt file and also your mode is "w" and you try to read then also your all the data is removed from the txt file also this apply for append to 

# now if tou want to write and you also want your old data too then you can use append
# append set mode to "a" before use of append 
# append not delete your old data it is aapend the new data to old data
# if your append then you have to only change only the mode "a" that sit there is no fuch as append function or method 

# f.write("\nHello world")   #\n for next line 
# now you can chheck at txt file you old data is also present and new data also updated

print(f.read())


f.close()                #closing tag