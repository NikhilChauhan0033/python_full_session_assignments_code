# assignment take number from user and sum that number 
# using tkinter

from tkinter import *

t = Tk()

t.title("Take number from user and sum that numbe")
t.geometry("800x800")

lbl1 = Label(text = "Enter First Number : ")
lbl1.pack()

inp1 = Entry()
inp1.pack()

lbl2 = Label(text = "Enter Second Number : ")
lbl2.pack()

inp2 = Entry()
inp2.pack()

lbl6 = Label(text="Answer")
lbl6.pack()
inp3 = Entry()
inp3.pack()

def add():
    try:
        a = int(inp1.get())
        b = int(inp2.get())
        c = a+b        #sum
        # c = a-b      #minus
        # c = a/b      #division
        # c = a*b      #multiplication
        inp3.delete("0", END)
        inp3.insert("0",str(c))
    except ValueError:  #ValueError occure when converting a string to an integer
         inp3.delete(0, END)
         inp3.insert(0, "Invalid Input")

btn1 = Button(text="Sum" , command=add)
btn1.pack()
# below create an empty label for space [for next line]
lbl3 = Label(text=" ").pack()


# task 2
# Build a calculator that can perform addition, subtraction, multiplication, and division based on a selected operation.

lbl4 = Label(text="Enter 1st Number : ")
lbl4.pack()

inp4 = Entry()
inp4.pack()

lbl5 = Label(text="Enter 2nd Number : ")
lbl5.pack()

inp5 = Entry()
inp5.pack()

lbl6 = Label(text="Answer")
lbl6.pack()

inp6 = Entry()
inp6.pack()

def addition():
    try:
        d = int(inp4.get())
        e = int(inp5.get())
        f = d+e
        inp6.delete("0" , END)
        inp6.insert("0" , f)
    except ValueError:
        inp6.delete("0" , END)
        inp6.insert("0" , "Invalid Input")

def minus():
    try:
        d = int(inp4.get())
        e = int(inp5.get())
        f = d-e
        inp6.delete("0" , END)
        inp6.insert("0" , f)
    except ValueError:
        inp6.delete("0" , END)
        inp6.insert("0" , "Invalid Input")

def division():
    try:
        d = int(inp4.get())
        e = int(inp5.get())
        f = d/e
        inp6.delete("0" , END)
        inp6.insert("0" , f)
    except ValueError:
        inp6.delete("0" , END)
        inp6.insert("0" , "Invalid Input")

def multiplication():
    try:
        d = int(inp4.get())
        e = int(inp5.get())
        f = d*e
        inp6.delete("0" , END)
        inp6.insert("0" , f)
    except ValueError:
        inp6.delete("0" , END)
        inp6.insert("0" , "Invalid Input")


addition = Button(text= "+" ,command=addition)
minus = Button(text= "-" ,command=minus)
division = Button(text= "/" ,command=division)
multiplication = Button(text= "*" ,command=multiplication)

addition.pack()
minus.pack()
division.pack()
multiplication.pack()

t.mainloop()

