maindata = [
 {
 "title":"Oranges",
 "price":50,
 "status":"out of stock",
 "soldQuantity":"1000",
 "category":"Fresh Produce",
 "description":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, ipsam?",
 },
 {
 "title":"White bread",
 "price":100,
 "status":"available",
 "soldQuantity":"250",
 "category":"Bread",
 "description":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, ipsam?",
 },
 {
 "title":"Crackers",
 "price":50,
 "status":"available",
 "soldQuantity":"150",
 "category":"Snacks",
 "description":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, ipsam?",
 },
 {
 "title":"Eggs",
 "price":200,
 "status":"out of stock",
 "soldQuantity":"500",
 "category":"Meat/Protein",
 "description":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, ipsam?",
 },
 {
 "title":"Potatoes",
 "price":250,
 "status":"out of stock",
 "soldQuantity":"2000",
 "category":"Fresh Produce",
 "description":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, ipsam?",
 },
 {
 "title":"Sugar",
 "price":350,
 "status":"available",
 "soldQuantity":"1800",
 "category":"Baking goods",
 "description":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, ipsam?",
 },
 {
 "title":"Cinnamon",
 "price":250,
 "status":"available",
 "soldQuantity":"2000",
 "category":"Condiments/spices",
 "description":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, ipsam?",
 },
 {
 "title":"Tomatoes",
 "price":50,
 "status":"Coming Soon",
 "soldQuantity":"0",
 "category":"Fresh Produce",
 "description":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, ipsam?",
 },
 {
 "title":"Coconut Oil",
 "price":200,
 "status":"Coming Soon",
 "soldQuantity":"0",
 "category":"Oils",
 "description":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque, ipsam?",
 }
 ]


#  Findout:
#  1.total available items name
#  2.total available items amount
#  3.items which are out of stock
#  4.all items (including out of stock)
#  5.particular item detail by their name
#  6.total item sold
#  7.item rate greater then 100 rupees
#  8.item rate lesser then 100 rupees
#  9.item according to their type(which means biscuits, chocolate,etc)


class Items:
    def __init__(self,info):
        self.data = info
        
    def getAll(self):
        print(self.data)

#  1.total available items name
    def getAvailableItems(self):
        li1 = list(filter(lambda a:a["status"]=="available",self.data))
        print(li1)

# 2.total available items amount
    def getAvailableItemsPrice(self):
        li2 = sum(map(lambda b:b["price"],filter(lambda c:c["status"]=="available",self.data)))
        print(li2)

#  3.items which are out of stock
    def getOutOfStockItems(self):
        li3 = list(filter(lambda d:d["status"]=="out of stock",self.data))
        print(li3)

obj1 = Items(maindata)

# print the all the data
obj1.getAll()

# print available items
obj1.getAvailableItems()

# print sum of all availble items price
obj1.getAvailableItemsPrice()

# print out of stock items
obj1.getOutOfStockItems()

# for more practice continue from question number 4

students = [
       {
         "name": "abc",
         "email": "abc@gmail.com",
         "contact": 5598,
         "subject": "js",
         "marks": 20,
       },
       {
         "name": "pqr",
         "email": "pqr@gmail.com",
         "contact": 8800,
         "subject": "js",
         "marks": 70,
       },
       {
         "name": "xyz",
         "email": "xyz@gmail.com",
         "contact": 8799,
         "subject": "python",
         "marks": 30,
       },
       {
         "name": "mno",
         "email": "mno@gmail.com",
         "contact": 5765,
         "subject": "js",
         "marks": 60,
       },
       {
         "name": "abc",
         "email": "opq@gmail.com",
         "contact": 8687,
         "subject": "python",
         "marks": 40,
       },
     ]

# Find Out : 
# Name of all the students
# Contact no of all students
# Name of subjects students are enrolled in 
# Collect only the student data (i.e. array of object with name, email, contact No)
# Details of students based on their name
# Name of students with marks above 50
# Details of students based on their subject
# Contact No and name of students with marks below 50
# Average of the class
# Name of the students who scored above the average 
