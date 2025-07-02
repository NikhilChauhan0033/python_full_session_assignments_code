# starting user defined module
# user defined module is known as create over own module

import mymodule
print(dir(mymodule))
mymodule.hello_msg("Nikhil")

li1 = [10,20,30]
li2 = []

ans = mymodule.square(li1,li2)
print(ans)

li3 = [10,20,30,40,50]
li4 = []

res = mymodule.reverse(li3,li4)
print(res)

li5 = [10,20]
res1 = mymodule.sum1(li5)
print(res1)

text = "My Name Is Nikhil"
oldText = "Nikhil"
newText = "Nanu"

rText = mymodule.myReplace(text,oldText,newText)
print(rText)

# another ways to use modules 
from mymodule import hello_msg,square   #import those function from module which need to use
from mymodule import hello_msg as hm,square  #give a sort name hello_msg as hm [after given a sort name use the sortname]
from mymodule import *  #import all the function from module using *

hello_msg("Nik")   #you dont need to write mymodule.hello_msg [bcz you it import from mymodule]
hm("Nik")

li1 = [10,20,3,4,5]
li2 = [] 
ans = square(li1,li2)
print(ans)

import mymodule as mm  #give a sort name mymodule as mm [after given a sort name use the sortname]

mm.hello_msg("Nik")