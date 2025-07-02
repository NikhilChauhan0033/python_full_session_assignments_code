# question to ask sir my we create the mydb , why create this inside mydb  database= "sess19" wht if i need to use another databse, why we use inside values(%s,%s), sir kya hum database and tabel vagera sab ka sab workbench peh bana liya or sirf insert yaha se karege toh chalega na ??

import mysql.connector  

mydb = mysql.connector.connect(
    host="localhost",       
    port=3306,             
    user="root",            
    password="Nikhil@03",  
    database= "sess19"      
)

# print(mydb)

cur = mydb.cursor()

# cur.execute("show databases;")
# cur.execute("create database sess19;")
# cur.execute("create table stud(name varchar(100),age int(10));")


# cur.execute("insert into stud values('dev',34);")
# cur.execute("insert into stud values('manan',33),('nikhil',56);")
# mydb.commit()
# cur.execute("select * from stud;")

# print(cur)

a = input("name: ")
b = input("age: ")

# query  = "insert into stud (name,age) values(%s,%s);"
# ans = (a,b)

# cur.execute(query,ans)

cur.execute("insert into stud (name,age) values(%s,%s);",(a,b))
mydb.commit()

# for i in cur:
#     print(i)
