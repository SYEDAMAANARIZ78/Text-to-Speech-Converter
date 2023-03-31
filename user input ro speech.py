from gtts import gTTS
import os
from tkinter import *


root = Tk()
canvas = Canvas(root, width = 400, height = 300)
canvas.pack()

def textToSpeech():
    text =entry.get()
    language = 'en'
    output = gTTS(text =text, lang=language,slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")
lable = Label(root, text="Enter The Scentence")
canvas.create_window(200,100,window=lable)
lable_entry = Entry(root)
canvas.create_window(200,100, window=lable_entry)

button = Button(text="convert", command =textToSpeech)
canvas.create_window(200,230, window=button)

root.mainloop()