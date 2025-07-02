# OOPS concept starting
# oops stand for object oriented programing
# oops is fater

# classes is structure  [blue priint] [you can not see you can not feel]
# object is instence of class [you can see you can feel]
# class and object use for create a libraries and use for backend

# class is connection of data member and functions / methods
# object is instense of that perticular class 

class Car:  #always class first latter is Capital
    length = 10     #data member
    width = 30      #data member
    height = 80     #data member
    color = "red"   #data member

    def drive(self):        #member function / methods   #self refer object [in js there is 'this' here in python there is self]
        print("Driving...")    
    
    def break1(self):       #member function / methods
        print("Breaking...")    

obj1 = Car()   #obj created of class
obj2 = Car()
obj3 = Car()
print(obj1)

print(obj1.color)
obj1.drive()

obj2.color = "green"   #change the value of data member with another obj
print(obj2.color)

li1 = [1,2,3,4,5]
print(type(li1))   #you will get class = "list"

# class with function
class Demo:
    def fun1(self):
        print("Hello")

# print function using object
obj3 = Demo()
obj4 = Demo()
obj5 = Demo()

obj3.fun1()

# print function using class
Demo.fun1(obj4)
obj5.fun1()

# setter and getter mathods
# there is also multiple getter and setter
# setter you take the value from user and set the value
# getter you get the user value from which is set[means you get the set value]

class Demo1:
    def set1(self,name):
        self.a = name
    
    def get1(self):
        return(f"My name is {self.a}")
         
obj6 = Demo1()

obj6.set1("Nikhil")  #call set
print(obj6.get1())   #print get. bcz we return

# contructor 
# without calling conctuctor you can print [ only just you have to create a object]
# on the above example you can see we have to call the set 

class Demo2:
    def __init__(self):   #__init__ [inbuild contructor] you dont have to call a function just create and onject
        print("Hello Nikhil")

obj7 = Demo2()  #object created

# another example
class Demo3:
    def __init__(self,name):
        self.a = name
    
    def get1(self):
        return(f"My name is {self.a}")
         
obj6 = Demo3("Nikhil Hello")   #send the set value from inside the Class(value) 

print(obj6.get1())  


# """
# 1. all books
# 2. get books according to the author name
# 3. get details of a particular book according to the name or year
# 4. get all books whose price is below 300
# 5. get sum of books price
# 6. Get sum of books price whose price is greater than 300
# """

info=[
  {
    "author": "Chinua Achebe",
    "country": "Nigeria",
    "imageLink": "images/things-fall-apart.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
    "pages": 209,
    "title": "Things Fall Apart",
    "year": 1958,
    "price":125
  },
  {
    "author": "Hans Christian Andersen",
    "country": "Denmark",
    "imageLink": "images/fairy-tales.jpg",
    "language": "Danish",
    "link": "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n",
    "pages": 784,
    "title": "Fairy tales",
    "year": 1836,
    "price":225
  },
  {
    "author": "Dante Alighieri",
    "country": "Italy",
    "imageLink": "images/the-divine-comedy.jpg",
    "language": "Italian",
    "link": "https://en.wikipedia.org/wiki/Divine_Comedy\n",
    "pages": 928,
    "title": "The Divine Comedy",
    "year": 1315,
    "price":345
  },
  {
    "author": "Unknown",
    "country": "Sumer and Akkadian Empire",
    "imageLink": "images/the-epic-of-gilgamesh.jpg",
    "language": "Akkadian",
    "link": "https://en.wikipedia.org/wiki/Epic_of_Gilgamesh\n",
    "pages": 160,
    "title": "The Epic Of Gilgamesh",
    "year": -1700,
    "price":500
  },
  {
    "author": "Unknown",
    "country": "Achaemenid Empire",
    "imageLink": "images/the-book-of-job.jpg",
    "language": "Hebrew",
    "link": "https://en.wikipedia.org/wiki/Book_of_Job\n",
    "pages": 176,
    "title": "The Book Of Job",
    "year": -600,
    "price":400
  },
  {
    "author": "Unknown",
    "country": "India/Iran/Iraq/Egypt/Tajikistan",
    "imageLink": "images/one-thousand-and-one-nights.jpg",
    "language": "Arabic",
    "link": "https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights\n",
    "pages": 288,
    "title": "One Thousand and One Nights",
    "year": 1200,
    "price":255
  },
  {
    "author": "Unknown",
    "country": "Iceland",
    "imageLink": "images/njals-saga.jpg",
    "language": "Old Norse",
    "link": "https://en.wikipedia.org/wiki/Nj%C3%A1ls_saga\n",
    "pages": 384,
    "title": "Nj\u00e1l's Saga",
    "year": 1350,
    "price":115
  },
  {
    "author": "Jane Austen",
    "country": "United Kingdom",
    "imageLink": "images/pride-and-prejudice.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Pride_and_Prejudice\n",
    "pages": 226,
    "title": "Pride and Prejudice",
    "year": 1813,
    "price":295
  },
  {
    "author": "Honor\u00e9 de Balzac",
    "country": "France",
    "imageLink": "images/le-pere-goriot.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Le_P%C3%A8re_Goriot\n",
    "pages": 443,
    "title": "Le P\u00e8re Goriot",
    "year": 1835,
    "price":200
  },
  {
    "author": "Samuel Beckett",
    "country": "Republic of Ireland",
    "imageLink": "images/molloy-malone-dies-the-unnamable.jpg",
    "language": "French, English",
    "link": "https://en.wikipedia.org/wiki/Molloy_(novel)\n",
    "pages": 256,
    "title": "Molloy, Malone Dies, The Unnamable, the trilogy",
    "year": 1952,
    "price":150
  },
 
]

class BookInfo:
    def __init__(self,mainData):
        self.data = mainData
#here data is variable  and  # inside the mainData the info the dataset is store #maindata is our parameter
# now mainData is store in the data ,now using data we can solve the questions

# print all the data
    def get3(self):
        print(self.data)

# print all the title
    def getTitle(self):
        li2 = list(map(lambda x:x["title"],self.data)) 
        # print(li2)
        # another way
        return li2
    
    def getAuthorTitle(self,authorUser):
        li3 = list(filter(lambda y : y["author"].lower()==authorUser.lower(),self.data))
        return li3

    def getBookByTitleYear(self,searchValue):
        li5 = list(filter(lambda b:b["title"].lower()==searchValue or b["year"] == searchValue,self.data))
        print(li5)

    def getPrice(self):
        li4 = list(filter(lambda z:z["price"]<300,self.data))
        print(li4)
      
    def getsumPrice(self):
        li5 = sum(map(lambda a:a["price"],self.data))
        print(li5)

    def getSumOfGreater(self):
        li6 = sum(map(lambda c:c["price"], filter(lambda d:d["price"]>300,self.data)))
        print(li6)



obj8=BookInfo(info)  #we send data as [over dataset variable namwe] as a parameter to class
# print all the data
obj8.get3()

# print all the title
# obj8.getTitle()

# another way
ans = obj8.getTitle()
for i in ans:
    print(i) 

# get book accorading to author name
inp1  = input("Enter author name : ")
ans  = obj8.getAuthorTitle(inp1)

for i in ans:
    print(i)

# get Book By Title Year

inp2 = input("Enter Title Or Year For Book : ")
obj8.getBookByTitleYear(inp2)

# get all price below 300
obj8.getPrice()

# get sum of all the price
obj8.getsumPrice()

# get Sum Of Greater 300
obj8.getSumOfGreater()

