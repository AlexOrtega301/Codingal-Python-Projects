from tkinter import *

# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("The Source!")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel(root)
    top.geometry("180x100")
    top.title("Toplevel windows")

    # Adding a label widget to Top Window
    lbl_top = Label(top, text="This is toplevel window, you cant put any windows on top of me!")
    lbl_top.pack()

# Adding a label and button widget to Root (Main) Window

lbl_root = Label(root, text="This is root window")
btn = Button(root, text="Click here to open another window, click me now!", command=topwin)

# Arranging widgets
lbl_root.pack()
btn.pack()

# Entering main event loop
root.mainloop()
