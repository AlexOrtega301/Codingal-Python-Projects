from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for displaying warning message
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found. virus is Worm.win32.example")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()

#this is a mockup test for tkinter messagebox functionality, there is no actual virus scanning implemented, nor virus on the system.
