# LEAP YEAR DETECTION SYSTEM

# In this program, you will learn to check whether a year is leap year or not. We will use nested if...else to solve this problem.

from tkinter import *

t = Tk()
t.title("Leap Year Checker")
t.geometry("600x600")

lbl1 = Label(t, text="Enter Year :")
inp1 = Entry(t)

result_label = Label(t, text="", fg="blue")  # Label to display the result

def leap_year():
    year = inp1.get()  # Get the input from the Entry widget
    if year.isdigit():  # Check if the input is a valid number
        year = int(year)  # Convert it to an integer
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  
            result_label.config(text=f"{year} is a Leap Year!", fg="green")
        else:
            result_label.config(text=f"{year} is Not a Leap Year!", fg="red")
    else:
        result_label.config(text="Please enter a valid year", fg="black")

btn1 = Button(t, text="Check", command=leap_year)

lbl1.pack(pady=5)
inp1.pack(pady=5)
btn1.pack(pady=5)
result_label.pack(pady=10)  # Display the result below the button

t.mainloop()
