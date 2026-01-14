from tkinter import *
from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry
root = Tk()
root.title('Image')
root.geometry('400x400')

# Open the image file
upload = Image.open("welcome.png")

# Convert this Image to a Tkinter-compatible image
image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label
label = Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)

# Add text label
label2 = Label(root, text="Image courtesy of tmafe.com, image expample for tkinter")
label2.place(x=40, y=360)

# Run the application
root.mainloop()
