# sklearn is use for machine learning
# sklearn also known as scikit-learn
# command for download  sklearn 'pip3 install scikit-learn'
# use this for checl if install or not from 'sklearn.linear_model import LinearRegression' from "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html" in this website there is a code given below from there copy 2nd line
# after that install this command 'pip3 install matplotlib'
# after all the installation run given below 4 

# dowanload the 2 exe file name classes.csv and trycatch.csv from google classroom python batch

# sklearn is use for machine learning [sklearn is also a library]
# LinearRegression and train_test_split it is the library of sklearn

# LinearRegression is also known as prediction means you can predct anything from old data

from sklearn.linear_model import LinearRegression  
from sklearn.model_selection import train_test_split

import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv("trycatch.csv")  #read file using pandas
print(data)  

# always remember use double [[]] for independet data  here independent is distance  and year
m = data[["disatnce","year"]]  #split column distance and year and assign to m variable 
n = data["price"]  #split column price assign to n variable

# X = indipendent data  [always capital X]
# y = dependent data [y in dependent on X]

# usetrain_test_split

X_train,X_test,y_tain,y_test = train_test_split(m,n,test_size=0.2,random_state=1)    
#test_size = here we define the data size that we how much send for test and random_state=1 is that over data is not randomly tested 
print(X_train)
print(X_test)  #here we got only 2 column distance and year that is over m 
print(y_test)   #here we got only price that is over mn

