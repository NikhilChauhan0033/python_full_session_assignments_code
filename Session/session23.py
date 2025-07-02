# Encapsulation [hiding the password etc]

class Computer:
    __price = 900   #private the variable using [__]

    def __init__(self):
        print(self.__price)

    def get1(self):
        print(f"Selling Price = {self.__price}")


comp1 = Computer()

comp1.__price = 1000 #here i am trying to set the price of Computer but it not set [here i dont get a error bcz i am trying to set not print [if i print then the error will generate]]
# print(comp1.__price)   # here  we get an error bcz we are printing 

comp1.get1()


# Polymorphism   [same method name but functionallity diffrent [use most time at inheritance time]]


# class Parent:
#     def hobby(self):   #same method
#         print("Dancing")  #different functinallity 

# class Child(Parent):      #inherite the parent
#     def hobby(self):    #same method
#         super().hobby()  #access the parent hobby [another way create another obj for each class. create another obj for parent]
#         print("Coding")   #different functinallity


# c1 = Child()
# c1.hobby()


# here we check how we can accesss the child and parent in child on 2nd function [if there is a different name of function then]
class Parent:
    def get1(self):    #parent function
        print("Dancing")  

class Child(Parent):

    def get3(self):      #child function
        print("Hello")
    
    def get2(self):       #child function
        self.get3() #if you want to access the child function then use self
        super().get1()  #if you want to access the parent function then use supper
        print("Coding")  


c1 = Child()
c1.get2()

