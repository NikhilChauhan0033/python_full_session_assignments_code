# Four pillars of oops

# 1. Inheritence  => Parent and child replationship [you can inherit your function to another function and you can access that data]
# 2. Abstraction => Process Hiding
# 3. Encapsulation => Data hiding [hiding the password etc]
# 4. Polymorphism => same method name but diffrent functionality


# Inheritance:

# # 1. Simple inheritance [single level] [one parent one child]
# class Parent():
#     def fun1(self):
#         print("I am Parent 1")


# class Child(Parent):  #inherit Parent
#     def fun2(self):
#         print("I am Child 1")


# obj1 = Child()
# obj1.fun2()
# obj1.fun1()


# 2. Multi-level Inheritance [parent, child,grand parent,grand child]

# class Parent():
#     def fun1(self):
#         print("I am Parent 1")


# class Child(Parent):  #inherit Parent
#     def fun2(self):
#         print("I am Child 1")

# class GrandChild(Child):  #inherit child #Grand child
#     def fun3(self):
#         print("I am Grand Child")

# obj2 = GrandChild()

# obj2.fun1()
# obj2.fun2()
# obj2.fun3()


# 3. Multiple Inheritance [Multiple parent , single child]

# class Parent1():
#     def fun1(self):
#         print("I am Parent 1")

# class Parent2():
#     def fun2(self):
#         print("I am Parent 2")


# class Child(Parent1,Parent2):  #inherit multiple Parent
#     def fun3(self):
#         print("I am Child 1")


# obj2 = Child()

# obj2.fun1()
# obj2.fun2()
# obj2.fun3()

# 4. Hierarchical Inheritance [one parent , multiple child]

# class Parent1():
#     def fun1(self):
#         print("I am Parent 1")

# class Child1(Parent1):  #inherit  Parent
#     def fun2(self):
#         print("I am Child 1")

# class Child2(Parent1):  #inherit  Parent
#     def fun3(self):
#         print("I am Child 2")


# obj2 = Child1()
# obj3 = Child2()

# obj2.fun1()
# obj3.fun1()

# 5. Hybrid Inheritance [multiple parent,multiple child]
# serach on google and find the solution


# setter and getter with inheritance
# if i want to call something from parent so i need to use super function super()

# class Parent():
#     def __init__(self,name):  #constructor
#         self.name = name   #set name

# class Child(Parent):

# # without creating a constructor we can access the parent value bcz of inheritance no need to create an contuctor for child

#     def get(self):
#         return f"My Name Is {self.name}"  #get the name value here using constructor in a

# obj1 = Child("Nikhil")  #a value
# print(obj1.get())

# set 2 value to child and access at the univercity

# class Parent():
#     def __init__(self,name):
#         self.name = name

#     def get4(self):   #get the value from child using same object 
#         print(self.age)

# class Child(Parent):
#     def __init__(self,a,age):
#         super().__init__(a)
#         self.age=age

#     def get1(self):
#         return f"My Name Is {self.name}" 

#     def get2(self):    #store only in child [set in child only ]
#         return f"My Age Is {self.age}"        

# obj1 = Child("Nikhil",21)
# print(obj1.get1())
# print(obj1.get2())

# print(obj1.get4())   #using same object we can access the child data toh parent 


# Abstraction: [Process hiding] [means hiding the process from user for anything] [hiding the background process] [any process]
# we are private over data members [variable]

class Employee():
    __count = 0   #[private the variable using dounble underscore __] [using double underscore __ you can hide the variable]

    def __init__(self):
        Employee.__count = Employee.__count + 1  #set using Class name [not using object]

    def get(self):
        print(f"Employess Count {Employee.__count}")
        

obj1 = Employee()
obj2 = Employee()
obj3 = Employee()

obj1.get()

