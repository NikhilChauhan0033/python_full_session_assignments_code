# CURRENCY CONVERTER IN PYTHON

# Create a tool to convert the currency use fixer API to get the live conversion rates and convert the corresponding amount With Real Time Data.

from tkinter import *
from tkinter import ttk # Import ttk module for Combobox

import requests

t = Tk()
t.title("Currency Converter")
t.geometry("600x600")

url = "https://api.exchangerate-api.com/v4/latest/INR"

response = requests.get(url)  #checking response if we get 200 or not
# print(response)
data = response.json()  #convert to josn bcz in the api data is in string formate
# print(data)
currencies = list(data["rates"].keys()) #take all the currencies to list
# print(currencies)

# Function to convert currency
def convert_currency():
    # create 3 variable and assign them the user selected values
    amount = float(amount_entry.get())  # Convert input from string to float
    from_curr = from_currency.get()
    to_curr = to_currency.get()

# for {from_curr} written inside the api url Dynamic Currency Conversion The user selects any currency in the "Convert From" dropdown (from_currency), so we need to change the API URL dynamically.

    url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}" 
    response = requests.get(url)
    data = response.json()

    rate = data["rates"][to_curr]
    converted_amount = round(amount * rate, 2)

    result_label.config(text=f"{amount} {from_curr} = {converted_amount} {to_curr}")

Label(t, text="Enter Amount:").pack(pady=5)
amount_entry = Entry(t)
amount_entry.pack(pady=5)

# DropDown
Label(text="Convert From:").pack(pady=5)
from_currency = ttk.Combobox(values=currencies)
from_currency.pack(pady=5)
from_currency.set("Selecte Currency")

Label(text="Convert To:").pack(pady=5)
to_currency = ttk.Combobox(values=currencies)
to_currency.pack(pady=5)
to_currency.set("Selecte Currency")

Button(t, text="Convert", command=convert_currency).pack(pady=10)

result_label = Label(t, text="", fg="blue", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

t.mainloop()