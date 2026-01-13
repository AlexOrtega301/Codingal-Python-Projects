from tkinter import *

window = Tk()
window.title("A Tkinter app")
window.geometry("300x300")

# Widgets
greeting = Label(window, text="Hello Random Github user", fg="black", bg="white")
button = Button(window, text="Click me, im a button!", bg="black", fg="white")
entry = Entry(window, fg="yellow", bg="blue", width=50)

# Pack widgets
greeting.pack()
button.pack()
entry.pack()

# Frame
frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text="A frame.")
label.pack()

# Textbox
textbox = Text(window, fg="green", bg="yellow", height=5, width=30)
textbox.pack()

# Run the application
window.mainloop() #whithouta this the app crashes?
