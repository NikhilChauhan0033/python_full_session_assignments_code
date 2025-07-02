# CONVERT TEXT TO SPEECH IN PYTHON 

# Text to speech is a process to convert any text into voice. Text tospeech project takes words on digital devices and convert theminto audio with a button click or finger  touch. 

# we are using this library for CONVERT TEXT TO SPEECH IN PYTHON serach on google "python library pyttsx3" and go to official pypi website and run this command for install library pip3 install pyttsx3 

# also you can use another library like gtts but there is no extra function like voice changeing voice slow fast here it is all so dont use that this just for information that there is also another library

import pyttsx3
from tkinter import *

t = Tk()
t.title("Convert Text To Speech")
t.geometry("600x600")

engine = pyttsx3.init()  #object creation

# given code for volum
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# given code for voice like male / female
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female

# UI code
text_Label = Label(text="Enter Text For Speech : ").pack(pady=5)

inp1 = Entry()
inp1.pack(pady=5)

def speech_text():
    text = inp1.get()
    if text:
        noText_label.config(text="")
        engine.say(text)
        engine.runAndWait()
    else:
        noText_label.config(text="Please Enter Some Text To Speech!!")

btn = Button(text="Speak", command=speech_text).pack(pady=10)

noText_label = Label(text="",fg="red")
noText_label.pack(pady=10)


t.mainloop()