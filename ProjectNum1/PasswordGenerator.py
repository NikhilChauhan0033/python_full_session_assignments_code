# PASSWORD GENERATOR
# It is a tool that generates passwords based on the givenguidelines that you set to create an unpredictable strongpassword for your accounts

from tkinter import *
import random
import string

t = Tk()
t.title("Password Generator")
t.geometry("600x600")

# Variables for checkbox states
use_uppercase = BooleanVar()  #BooleanVar() – for True/False  , This will store True/False
use_lowercase = BooleanVar()
use_numbers = BooleanVar()
use_symbols = BooleanVar()

lbl1 = Label(text="Enter the password length : ").pack(pady=5) #pady=5 adds vertical spacing.
inp1 = Entry()
inp1.pack(pady=5)

lbl2 = Label(text="Selecte Criteria : ").pack(pady=5)

# checkbox [These BooleanVar() variables track whether each checkbox is checked (True) or not (False).]
#anchor is like for direction[alignment ] left,right,center
Checkbutton(text="Uppercase", variable=use_uppercase).pack(anchor='s',pady=20) 
Checkbutton(text="Lowercase", variable=use_lowercase).pack(anchor='s',pady=20)
Checkbutton(text="Numbers", variable=use_numbers).pack(anchor='s',pady=20)
Checkbutton(text="Symbols", variable=use_symbols).pack(anchor='s',pady=20)

def password_generator():
    inp2.delete(0, END)

    try:
        length = int(inp1.get())  #convert the user's input to an integer.
    except ValueError:
        inp2.insert(0, "Enter valid number!")  #If it's not a number, shows an error in the output box.
        return

    characters = ""    #Creates an empty string to hold the allowed characters.

    if use_uppercase.get():
        characters += string.ascii_uppercase #same as characters = characters + string.ascii_uppercase
    if use_lowercase.get():
        characters += string.ascii_lowercase
    if use_numbers.get():
        characters += string.digits
    if use_symbols.get():
        characters += string.punctuation

# If the user hasn’t selected any criteria, show a message and stop.
    if not characters:
        inp2.insert(0, "Select at least one option")
        return

# random.choices() picks random characters from the pool.
# ' '.join(...) turns the list of characters into a single string.
    password = ''.join(random.choices(characters, k=length))
    inp2.insert(0, password)

btn1 = Button(text="Generate", command=password_generator).pack(pady=5)

lbl3 = Label(text="Generated Password : ").pack(pady=5)

inp2 = Entry()
inp2.pack(pady=5)

t.mainloop()