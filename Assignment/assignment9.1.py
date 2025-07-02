# this all 3 given by ChatGPT

#  Task 3: Celsius to Fahrenheit Converter

from tkinter import *

# Create main window
t = Tk()
t.title("Celsius to Fahrenheit Converter")
t.geometry("400x300")

# Labels and input fields
Label(t, text="Enter Temperature in Celsius:").pack(pady=5)
celsius_input = Entry(t)
celsius_input.pack(pady=5)

Label(t, text="Temperature in Fahrenheit:").pack(pady=5)
fahrenheit_output = Entry(t)
fahrenheit_output.pack(pady=5)

# Function to convert Celsius to Fahrenheit
def convert():
    try:
        celsius = float(celsius_input.get())
        fahrenheit = (9 / 5) * celsius + 32
        fahrenheit_output.delete(0, END)
        fahrenheit_output.insert(0, f"{fahrenheit:.2f}")
    except ValueError:
        fahrenheit_output.delete(0, END)
        fahrenheit_output.insert(0, "Invalid Input")

# Convert button
Button(t, text="Convert", command=convert).pack(pady=10)

t.mainloop()



# Task 4: Simple To-Do List

from tkinter import *

# Create main window
t = Tk()
t.title("Simple To-Do List")
t.geometry("400x400")

# Task input field
Label(t, text="Enter Task:").pack(pady=5)
task_input = Entry(t)
task_input.pack(pady=5)

# Listbox to display tasks
task_list = Listbox(t, width=40, height=10)
task_list.pack(pady=10)

# Function to add task
def add_task():
    task = task_input.get()
    if task:
        task_list.insert(END, task)
        task_input.delete(0, END)

# Function to remove selected task
def remove_task():
    try:
        selected = task_list.curselection()[0]
        task_list.delete(selected)
    except IndexError:
        pass

# Buttons
Button(t, text="Add Task", command=add_task).pack(pady=5)
Button(t, text="Remove Task", command=remove_task).pack(pady=5)

t.mainloop()


# Task 5: Rock, Paper, Scissors Game

from tkinter import *
import random

# Create main window
t = Tk()
t.title("Rock, Paper, Scissors Game")
t.geometry("400x400")

# Choices
choices = ["Rock", "Paper", "Scissors"]

Label(t, text="Choose Rock, Paper, or Scissors:").pack(pady=5)
user_choice = StringVar()
user_choice.set(choices[0])  # Default value
OptionMenu(t, user_choice, *choices).pack(pady=5)

result_label = Label(t, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Function to play the game
def play():
    computer_choice = random.choice(choices)
    user = user_choice.get()
    
    if user == computer_choice:
        result = "It's a Tie!"
    elif (user == "Rock" and computer_choice == "Scissors") or \
         (user == "Paper" and computer_choice == "Rock") or \
         (user == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    result_label.config(text=f"Computer: {computer_choice}\n{result}")

# Play button
Button(t, text="Play", command=play).pack(pady=10)

t.mainloop()
