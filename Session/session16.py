# pandas 
# pandas installation command pip3 install pandas
# if you want to changes in excel sheet you can do with pandas 
# using pandas you can change, add, fetch this type of task you can do in excel
# extension excel files is csv and tsv
# student1.csv is excel file  [students1.csv]

import pandas as pd #given sort name to pandas [pd]

data = pd.read_csv("students1.csv")
print(data)

# given below given you column names
print(data.columns.values)
# if nothing write inside .tail() you will get first 5 values
print(data.head())
# how many did you want you can write you will get give you first 7 values
print(data.head(7))
# if nothing write inside .tail() you will get bottom 5 values
print(data.tail())
# how many did you want you can write you will get give you bottom 3 values
print(data.tail(3))
# data.info give the data typw which which type of this data
data.info()

# if you want only perticular column data use given bwelow
print(data["physics"])

# if you want multiple column data use given below
a = ["physics","chemistry","maths"]
print(data[a])

# or you can write like this to [just you have to write inside the list if you want prit a multiple columns]
print(data[["physics","chemistry","maths"]])

# add the column name total and print the 3 columns totals
# here we create first data['total] means new column created after assign the values
data['total'] = data["physics"] + data["chemistry"] + data["maths"]
print(data)

# print the pass if total values is greateethen 220 or fail
def fun1(m):
    return "pass" if m>220 else "fail"
data["result"] = data["total"].apply(fun1)

# same using lambda function [print the pass if total values is greateethen 220 or fail]
data["result"] = data["total"].apply(lambda m:"pass" if m>220 else "fail")
print(data)

# here you can create a new excel.csv file store the updated data 
# [given below is way to create a new excel.csv and update data]
# if you want to store the data in existing file give existing file name
data.to_csv("students2.csv")

# given below we read the students2.csv 
data1 = pd.read_csv("students2.csv")
print(data1)
