from tkinter import *

t = Tk()
t.title("Find Cost of Tile")
t.geometry("600x600")

# Width input
Label(text="Enter The Width Of Area (in foot)").pack(pady=5)
widthInp = Entry()
widthInp.pack(pady=5)

# Height input
Label(text="Enter The Height Of Area (in foot)").pack(pady=5)
heightInp = Entry()
heightInp.pack(pady=5)

# Cost input
Label(text="Enter The Cost Of Tile In ₹ (per square foot)").pack(pady=5)
costInp = Entry()
costInp.pack(pady=5)

# Label to display the result
costLbl = Label(text="")
costLbl.pack(pady=10)

# Function to calculate total cost
def area():
    w = int(widthInp.get())
    h = int(heightInp.get())
    c = int(costInp.get())

    areaWH = w * h
    totalCost = areaWH * c

    costLbl.config(text=f"Total Cost Of Tile is ₹{totalCost}")

# Submit button
Button(text="Submit", command=area).pack(pady=5)

t.mainloop()
