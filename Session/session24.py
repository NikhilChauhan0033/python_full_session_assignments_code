# starting with LinearRegression and matplotlib
# LinearRegression means prediction 

from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split

import pandas as pd

# matplotlib use for graph [using matplotlib you can create graph according to data]
import matplotlib.pyplot as plt    #use for graph 

# given below code is for matplotlib
# inside "classes.csvthere is bike data available 
data = pd.read_csv("classes.csv")
print(data)

plt.scatter(data["distance"],data["price"])
# plt.bar(data["distance"],data["price"])
# plt.stem(data["distance"],data["price"])
# plt.step(data["distance"],data["price"])
# plt.hist2d(data["distance"],data["price"])
# given above is different types of graphs you can use multiple types at a time or single

# after running one new window is open there is see your graph [there is many button given below left side save and all so you can save graphs using saqve button]

plt.xlabel("Distance Of Bike")
plt.ylabel("Price Of Bike")
# plt.show()     # uncomment for graph

# Linear regression

# always remember use double [[]] for independet data  here independent is distance 
m = data[["distance"]]  #split column distance and assign to m variable #independet data  #this my X independent
n = data["price"]  #split column price assign to n variable  #this my y dependent

# print(m,n)

reg = LinearRegression()
reg.fit(m,n)

print(reg.predict([[10]]))   #here we can get predicted value like over machine use over old data and analysis it and give a around value not accurate value here i will get price of my bike i enter 10 is distance of my bike
