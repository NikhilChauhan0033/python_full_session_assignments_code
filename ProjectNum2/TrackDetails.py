from tkinter import *
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# phonenumbers: Library to analyze phone numbers.
# geocoder: Gets the country/state.
# carrier: Gets the SIM provider name.
# timezone: Gets the time zone for the number.

def getDetails():
    number = inp1.get()

    if not number.startswith('+'):
        number = '+' + number

    try:
        phone_number = phonenumbers.parse(number)  #parse(number): Converts string into a phonenumbers object.
        
        #for 'en' It tells the phonenumbers library which language to use for the returned text.
        # For example: 'en' = English' , fr'French ,'hi' = Hindi
        location = geocoder.description_for_number(phone_number, 'en') #write hi for hindi initiate of en
        sim = carrier.name_for_number(phone_number, 'en') #write hi for hindi initiate of en
        time = timezone.time_zones_for_number(phone_number)
        valid = phonenumbers.is_valid_number(phone_number)

        result = f"""📍 Location: {location}
📶 SIM/Carrier: {sim}
🕒 Timezone: {time}
✅ Valid: {valid}"""

    except:
        result = "❌ Invalid phone number format!"

    output_label.config(text=result)


# --- GUI Setup ---
t = Tk()
t.title("📱 Track Phone Number Details")
t.geometry("500x400")

Label(t, text="Enter Phone Number with Country Code", font=("Arial", 12)).pack(pady=10)

inp1 = Entry(t, font=("Arial", 14), width=30)
inp1.pack(pady=5)

btn1 = Button(t, text="Get Details", command=getDetails, font=("Arial", 12), bg="blue", fg="white")
btn1.pack(pady=10)

output_label = Label(t, text="", font=("Arial", 12), justify=LEFT, fg="green")
output_label.pack(pady=10)

t.mainloop()
