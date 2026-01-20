from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# -------------------- Main Window --------------------
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Image
upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey Alex! Welcome to Denomination Counter Application.",
    bg='light blue'
)
label1.place(relx=0.5, y=340, anchor=CENTER)

# -------------------- Button Action --------------------
def msg():
    messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    topwin()

button1 = Button(
    root,
    text="Let's get started!",
    command=msg,
    bg='brown',
    fg='white'
)
button1.place(x=260, y=360)

# -------------------- Top Window --------------------
def topwin():
    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('600x400')

    # Input
    lbl = Label(top, text="Enter Amount:", bg='grey', fg='white')
    lbl.place(x=140, y=80)

    entry = Entry(top)
    entry.place(x=260, y=80)

    # Denomination Labels
    l1 = Label(top, text="1000 :", bg='grey', fg='white')
    l2 = Label(top, text="500  :", bg='grey', fg='white')
    l3 = Label(top, text="200  :", bg='grey', fg='white')

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    # Output Fields
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    # Calculation Logic
    def calculate():
        try:
            amount = int(entry.get())

            note_1000 = amount // 1000
            amount %= 1000

            note_500 = amount // 500
            amount %= 500

            note_200 = amount // 200

            # Clear previous output
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            # Display result
            t1.insert(END, note_1000)
            t2.insert(END, note_500)
            t3.insert(END, note_200)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer amount")

    # Calculate Button
    btn = Button(
        top,
        text="Calculate",
        command=calculate,
        bg='brown',
        fg='white'
    )
    btn.place(x=240, y=120)

# -------------------- Run App --------------------
root.mainloop()
