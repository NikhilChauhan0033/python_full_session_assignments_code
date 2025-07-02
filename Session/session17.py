# tkinter is also known as tk-tools
# command for installation pip3 install tk-tools
# tkinter is library 
# tkinter use for create python application
# using tkinter use can create pyton application
# tkinter use for create GUI [Graphics User Interface]
# [use for forms related works]


# for check use below if it is install or not uf (blank then installed otherwise sum error )
from tkinter import *

# rember alaways you have to write a code inside window open and window close 

t = Tk()  # window open  #when run this code there open a one window

t.title("My First Window")  #give title to window
t.geometry("800x800") #define size of window

# always rember when ever you whatever you create using tags alway close that using pack()
# pack is way to close the tags
# rember which tag your closing first it is create first

# given below is opening tag
lbl1 = Label(text = "Enter Your Name : ")
inp1 = Entry()

# create a functio for btn1
def fun1():
    inp2.delete("0",END)
    a = inp1.get()
    inp2.insert("0",a)

    # hellow check in terminal 
    # print("Hello")

btn1 = Button(text="Click Me",command=fun1)
lbl2 = Label(text = "what ever you above input, you will get in below given input")
inp2 = Entry()

# given below is closing tag
lbl1.pack()
inp1.pack()
btn1.pack()
lbl2.pack()
inp2.pack()

# given below is another way close tag
# lbl1 = Label(text = "Enter Your Name : ").pack()

t.mainloop() # window close


