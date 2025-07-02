# starting with numpy
# first check using this import numpy as np bcz sometime by default numpy is installed when we install pandas
# if you get an error then install numpy
# comman for instal numpy 'pip3 install numpy'
# numpy use for mathematics 
# numpy stand for numerical python [full form of numpy numerical python]


import numpy as np

li1 = [10,20,30,40]
a = np.array(li1)
print(a)
print(type(li1))
print(type(a))

# sort cut of above code
b = np.array([10,20,30,40])
print(b)

d = np.array([[10],[30],[30],[40]])
print(d)
print(d.shape)  #shape is give your information about rows and columns

c = np.arange(1,25)  #arange same as range but it is numpy arange so that why we called as arange work etc same as range
print(c)

# given below called 2 dimenstionl array also known as 2D array
e = np.arange(1,25).reshape(2,12)
e = np.arange(1,25).reshape(12,2)
print(e)

# given below called 3 dimenstionl array also known as 3D array
f = np.arange(1,25).reshape(2,3,4)
print(f)

# given below called 4 dimenstionl array also known as 4D array
g = np.arange(1,25).reshape(2,3,2,2)
print(g)

h = np.array([[10,20],[30,40]])
print(np.max(h))    #find max from aaray
print(np.max(h))    #find min from aaray
print(np.sum(h))    #find sum from aaray

i = np.ones((2,4))
i = np.ones((2,4))
i = np.eye(4)
i = np.full((3,4),8)
print(i)

#maxium = 32D aaray min = 1D array [range is from 1 to 32]
j = np.array([1,2,3,4,5],ndmin = 1)
# j = np.array([1,2,3,4,5],ndmin = 12)
# j = np.array([1,2,3,4,5],ndmin = 22)
# j = np.array([1,2,3,4,5],ndmin = 32)
print(j)



# cheatsheet given by Dev sir for numpy use that and learn more about numpy