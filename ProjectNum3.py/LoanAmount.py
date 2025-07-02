from tkinter import *
from tkinter import ttk
import math

# Create the main window
t = Tk()
t.title("Mortgage Calculator")
t.geometry("500x500")

# === Input Section ===

# Label and input for Loan Amount
Label(text="Loan Amount (₹)").pack(pady=5)
loan_entry = Entry()
loan_entry.pack(pady=5)

# Label and input for Annual Interest Rate
Label(text="Annual Interest Rate (%)").pack(pady=5)
interest_entry = Entry()
interest_entry.pack(pady=5)

# Label and input for Loan Term in Years
Label(text="Loan Term (Years)").pack(pady=5)
years_entry = Entry()
years_entry.pack(pady=5)

# Dropdown for Compounding Option (Monthly, Weekly, etc.)
Label(text="Compounding Type").pack(pady=5)
compound_var = StringVar()
compound_dropdown = ttk.Combobox(textvariable=compound_var)
compound_dropdown['values'] = ("Monthly", "Weekly", "Daily", "Continually")
compound_dropdown.current(0)  # Default selected option
compound_dropdown.pack(pady=5)

# Label to display the result (monthly payment, total interest, etc.)
result_label = Label(text="", font=("Arial", 10), justify=LEFT)
result_label.pack(pady=10)

# === Mortgage Calculation Function ===
def calculate_mortgage():
    # Get user inputs from entry fields
    P = float(loan_entry.get())  # Principal loan amount
    annual_rate = float(interest_entry.get()) / 100  # Convert percentage to decimal
    years = int(years_entry.get())

    # Get selected compounding type
    compounding = compound_var.get()

    # Handle compounding frequency
    if compounding == "Monthly":
        n = 12
    elif compounding == "Weekly":
        n = 52
    elif compounding == "Daily":
        n = 365
    elif compounding == "Continually":
        # For continuous compounding, use A = Pe^(rt)
        A = P * math.exp(annual_rate * years)  # Total amount payable
        total_interest = A - P  # Interest = Total - Principal
        monthly_payment = A / (years * 12)  # Monthly payment
        # Format and show result
        result = f"Total Payment: ₹{A:.2f}\nTotal Interest: ₹{total_interest:.2f}\nMonthly Payment: ₹{monthly_payment:.2f}"
        result_label.config(text=result)
        return  # Exit function after continuous compounding calculation

    # For regular compounding (Monthly/Weekly/Daily), calculate EMI
    r = annual_rate / n  # Periodic interest rate
    total_payments = n * years  # Total number of payments

    # EMI formula
    emi = (P * r * (1 + r) ** total_payments) / ((1 + r) ** total_payments - 1)

    total_payment = emi * total_payments  # Total payment = EMI × number of payments
    total_interest = total_payment - P  # Interest = Total - Principal

    # Format and show result
    result = f"Monthly Payment (EMI): ₹{emi:.2f}\nTotal Payment: ₹{total_payment:.2f}\nTotal Interest: ₹{total_interest:.2f}"
    result_label.config(text=result)

# === Submit Button ===

# When clicked, this button will run the mortgage calculation function
Button(t, text="Calculate Mortgage", command=calculate_mortgage).pack(pady=10)

# Start the GUI loop
t.mainloop()
