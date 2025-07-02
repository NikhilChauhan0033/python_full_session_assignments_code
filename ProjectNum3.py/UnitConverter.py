import tkinter as tk
from tkinter import ttk
import requests

# Function to fetch live currency exchange rates
def fetch_currency_rates():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
        data = response.json()
        return data['rates']
    except Exception as e:
        print("Error fetching currency rates:", e)
        return None

# ---------------- Conversion Functions ---------------- #

# Convert temperature between Celsius, Fahrenheit, Kelvin
def convert_temperature(value, from_unit, to_unit):
    try:
        value = float(value)
        if from_unit == to_unit:
            return value
        
        # Convert from any to Celsius first
        if from_unit == "Fahrenheit":
            value = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            value = value - 273.15

        # Convert Celsius to target unit
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        
        return value  # If already in Celsius
    except:
        return "Invalid Input"

# Convert volume between Liters, Milliliters, Gallons
def convert_volume(value, from_unit, to_unit):
    try:
        value = float(value)

        # Convert to liters first
        if from_unit == "Milliliters":
            value = value / 1000
        elif from_unit == "Gallons":
            value = value * 3.78541

        # Convert liters to target unit
        if to_unit == "Milliliters":
            return value * 1000
        elif to_unit == "Gallons":
            return value / 3.78541

        return value  # If already in Liters
    except:
        return "Invalid Input"

# Convert currency using live exchange rates
def convert_currency(value, from_unit, to_unit, rates):
    try:
        value = float(value)

        if from_unit == to_unit:
            return value

        # Convert from any to INR
        if from_unit != "INR":
            value = value / rates[from_unit]

        # Convert INR to target currency
        return value * rates[to_unit]
    except:
        return "Invalid Input"

# ---------------- Main Conversion Function ---------------- #
def convert():
    category = category_var.get()
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()
    value = input_entry.get()

    # Perform the appropriate conversion
    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif category == "Volume":
        result = convert_volume(value, from_unit, to_unit)
    elif category == "Currency":
        rates = fetch_currency_rates()
        if rates:
            result = convert_currency(value, from_unit, to_unit, rates)
        else:
            result = "Error fetching currency rates"
    else:
        result = "Invalid Category"

    result_label.config(text=f"Result: {result}")

# Update the dropdowns when the category changes
def update_units(event):
    category = category_var.get()

    if category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    elif category == "Volume":
        units = ["Liters", "Milliliters", "Gallons"]
    elif category == "Currency":
        units = ["INR", "USD", "EUR"]
    else:
        units = []

    # Update both dropdown menus
    from_unit_var.set(units[0])
    to_unit_var.set(units[1])
    from_unit_menu['menu'].delete(0, 'end')
    to_unit_menu['menu'].delete(0, 'end')
    for unit in units:
        from_unit_menu['menu'].add_command(label=unit, command=tk._setit(from_unit_var, unit))
        to_unit_menu['menu'].add_command(label=unit, command=tk._setit(to_unit_var, unit))

# ---------------- GUI Setup ---------------- #

t = tk.Tk()  # Main Tkinter window (renamed from root to t)
t.title("Unit Converter")
t.geometry("400x350")

# Category selection dropdown
category_var = tk.StringVar()
tk.Label(t, text="Select Category:").pack()
category_menu = ttk.Combobox(t, textvariable=category_var, values=["Temperature", "Currency", "Volume"])
category_menu.current(0)
category_menu.bind("<<ComboboxSelected>>", update_units)
category_menu.pack()

# From unit dropdown
from_unit_var = tk.StringVar()
tk.Label(t, text="From Unit:").pack()
from_unit_menu = tk.OptionMenu(t, from_unit_var, "")
from_unit_menu.pack()

# To unit dropdown
to_unit_var = tk.StringVar()
tk.Label(t, text="To Unit:").pack()
to_unit_menu = tk.OptionMenu(t, to_unit_var, "")
to_unit_menu.pack()

# Input field
tk.Label(t, text="Enter Value:").pack()
input_entry = tk.Entry(t)
input_entry.pack()

# Convert button
tk.Button(t, text="Convert", command=convert).pack(pady=10)

# Result display
result_label = tk.Label(t, text="Result:")
result_label.pack()

# Initialize dropdowns with default units
update_units(None)

# Run the Tkinter main loop
t.mainloop()
