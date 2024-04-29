import tkinter
from tkinter import *

# create the main window
root = Tk()
root.title("CIPHER APPS")
root.geometry("400x550")

# set the font for the title label
title_font = ("Arial", 20)

# create the title label
title_label = Label(root, text="CIPHER APPS", font=title_font)
title_label.pack(pady=20)


def open_caesar_cipher():
  import Caesar.py

def open_vigenere_cipher():
  import Vigenere.py

def open_playfair_cipher():
  import Playfair.py

def open_vernam_cipher():
  import Vernam.py

# Define the function to exit the app
def exit_app():
  root.destroy()


# set the font for the buttons
button_font = ("Arial", 18)

# create the buttons
caesar_button = Button(root,
                       text="Caesar Cipher",
                       command=open_caesar_cipher,
                       font=button_font,
                       width=20,
                       height=2)
vigenere_button = Button(root,
                         text="Vigenere Cipher",
                         command=open_vigenere_cipher,
                         font=button_font,
                         width=20,
                         height=2)
playfair_button = Button(root,
                         text="Playfair Cipher",
                         command=open_playfair_cipher,
                         font=button_font,
                         width=20,
                         height=2)
vernam_button = Button(root,
                       text="Vernam Cipher",
                       command=open_vernam_cipher,
                       font=button_font,
                       width=20,
                       height=2)
exit_button = Button(root,
                     text="Exit",
                     command=exit_app,
                     font=button_font,
                     width=20,
                     height=2)

# add the buttons to the window
caesar_button.pack(pady=10)
vigenere_button.pack(pady=10)
playfair_button.pack(pady=10)
vernam_button.pack(pady=10)
exit_button.pack(pady=10)

# start the event loop
root.mainloop()