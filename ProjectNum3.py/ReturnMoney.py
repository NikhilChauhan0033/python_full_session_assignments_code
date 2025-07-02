from tkinter import *

# Create the main Tkinter window
root = Tk()
root.title("Change Return Program")
root.geometry("500x600")  # Set window size

# User Input: Total Cost
Label(root, text="Enter Total Cost (₹)").pack(pady=5)  # Label for cost
cost_entry = Entry(root)  # Entry field to input total cost
cost_entry.pack(pady=5)

# User Input: Amount Paid
Label(root, text="Enter Amount Paid (₹)").pack(pady=5)  # Label for amount paid
paid_entry = Entry(root)  # Entry field to input paid amount
paid_entry.pack(pady=5)

# Label to Show Final Output
result_label = Label(root, text="", font=("Arial", 10), justify=LEFT)
result_label.pack(pady=10)

# Denominations in Paisa
# We convert ₹1 to 100 paisa, ₹2000 to 200000 paisa, etc.
denominations = [200000, 50000, 20000, 10000, 5000, 2000, 1000,
                 500, 200, 100, 50, 25, 10, 5, 1]

# Mapping of values to readable labels
names = {
    200000: "₹2000",
    50000: "₹500",
    20000: "₹200",
    10000: "₹100",
    5000: "₹50",
    2000: "₹20",
    1000: "₹10",
    500: "₹5",
    200: "₹2",
    100: "₹1",
    50: "50 paisa",
    25: "25 paisa",
    10: "10 paisa",
    5: "5 paisa",
    1: "1 paisa"
}

# Function to Calculate the Change
def calculate_change():
    try:
        # Get values from user input
        cost = float(cost_entry.get())   # Convert cost to float
        paid = float(paid_entry.get())   # Convert paid amount to float

        # Check if the amount paid is less than cost
        if paid < cost:
            result_label.config(text="Not enough money paid.")
            return

        # Calculate change in paisa (₹1 = 100 paisa)
        change = round((paid - cost) * 100)

        # Text to display result
        result_text = f"Total Change: ₹{change / 100:.2f}\n\nBreakdown:\n"

        # Loop through each denomination
        for d in denominations:
            count = change // d  # How many times the denomination fits in change
            if count > 0:
                result_text += f"{names[d]} x {int(count)}\n"  # Append result
                change = change % d  # Update remaining change

        # Show result in the GUI
        result_label.config(text=result_text)

    except ValueError:
        # If user entered invalid input (non-numeric), show error
        result_label.config(text="Please enter valid numbers.")

# Button to Trigger Calculation
Button(root, text="Calculate Change", command=calculate_change).pack(pady=10)

# Run the GUI Loop
root.mainloop()
