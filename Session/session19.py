'''
starting with mysql in python
mysql is a query language
we create database using mysql query , database is a collection data and data tables

first intall mysql 
serach on google mysql go to official website after that go to download after that go down and click on MySQL Community (GPL) Downloads after click that click on MySQL Community Server after that Windows (x86, 64-bit), MSI Installer	9.2.0	118.7M click on button Download 

after this download mysql worekbench, workebench is a mysql code editor serach on google mysql workbench download for windows go to official website click on Windows (x86, 64-bit), MSI Installer	8.0.41	42.0M click on button Download

after that we install mysql python mysql connector serach on google python mysql connector pypi go to oofial website 
using this command you can download connecter of between mysql and python "pip3 install mysql-connector-python"
given below there is sample code you can take as a example
'''

import mysql.connector  #after download run this for check if download or not [if blank then succesfully install]

# Connect to server mysql
mydb = mysql.connector.connect(
    host="localhost",       #set host nname as localhost
    port=3306,              #set port as 3306
    user="root",            #set your mysql username [when install there is a you will set the your username]
    password="Nikhil@03",   #set your mysql password [when install there is a you will set the your password]
    database= "sess19"      #we create database here bcz 
)

'''after this all print mydb if you get something like this <mysql.connector.connection_cext.CMySQLConnection object at 0x00000264FE566270> then you successfully conected with mysql'''
# print(mydb)

'''now we create cursor we want a cursor to execute mysql querys [do not comment cur never bcz if you comment then you will be not able to execute any queries]'''
cur = mydb.cursor()

'''after creating cursor we execute first we check show databases bcz we can not repeat the database name
if only run the cur.execute("show databases;") then you will get blank bcz there is lot of databasese so that why you have to apply a loop
rember always at time only one execute query will run so that why 
we create a databases at the coonection time [database= "sess19"]
so when you run first comment the previouse query'''
# cur.execute("show databases;")

'''after apply the loop you will get your all the databses '''
# for i in cur:
#     print(i)

'''now we create a new database'''
# cur.execute("create database sess19;")
'''after created database we will create table inside the over database sess19
here we can not use [cur.execute("use sess19")] like this bcz here at time only one query is execute so that also why we create over database at coonection time '''

'''after this above all we create we wil create table'''
# cur.execute("create table stud(name varchar(100),age int(10));")

'''we check if over table is created or not [if you run only this then you will get blank bcz you not apply the loop bcz there is a lot of table inside one database so we havve to apply the loop]'''
# cur.execute("SHOW TABLES")
'''after apply loop you will get all the tabel which you will created'''
# for i in cur:
#     print(i)  

'''after creating table we insert over data into the tabel or in the databse tabel'''

# cur.execute("insert into stud values('nik',34);")
'''always remember whenever you insert the data to table or you run or execute insert qery use this mydb.commit() bcz we have close that query also use for Save over Changes like When you modify the database (insert, update, delete), the changes are not permanent [or updated at table or database] until you commit them.'''
# mydb.commit()
'''after run this you will get blank means sucsessfully your data is inserted to your table'''
'''for check use the data is inserted or not use'''
# cur.execute("select * from stud;")
# for i in cur:
#     print(i)

'''if you try to print cur so whatever you write inside the cur you will get'''
# print(cur)

'''you can add multiple values at a time like given below'''
# cur.execute("insert into stud values('manan',33),('nikhil',56);")
# cur.execute("select * from stud;")

'''using user input we insert values at database like given below'''

'''1st we create user inputs'''
# a = input("name: ")
# b = input("age: ")

'''after created inputs we execute insert query like we create 2 variable one for query and another for userinputs 
inside query variable we write over insert query like insert into [over table name] stud [after 2 variable this variable is a table variable like table column names use that(name,age) [after that values this %s this values use for it keeps SQL queries safe from injection,It allows dynamic values in queries like this %s,%s] values(%s,%s);  after that for we create another variable name "ans" for user inputs variable to store use values [ask chatGPT to more information]'''
# query  = "insert into stud (name,age) values(%s,%s);"   
# ans = (a,b)

# cur.execute(query,ans)
# mydb.commit()

'''sort way to write the above code [ we write in single line the userinputs values store in databse]'''
              #here is over query path                     #here over user input variable name
# cur.execute("insert into stud (name,age) values(%s,%s);",(a,b))
# mydb.commit()

# for i in cur:
#     print(i)
