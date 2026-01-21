import random
import string
import tkinter as tk
from tkinter import messagebox

# --- Password Generator Logic ---
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.a
        symbols = "!@#$%^&*()-_=+[]{};:,.<>/?‽"

        all_chars = lowercase + uppercase + digits + symbols

        password = "".join(random.choice(all_chars) for _ in range(length))
        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive number")

# --- Tkinter UI ---
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("420x240")
root.resizable(False, False)

title = tk.Label(root, text="🔐 Random Password Generator", font=("Arial", 16, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Password length:").grid(row=0, column=0, padx=5)
length_entry = tk.Entry(frame, width=10)
length_entry.grid(row=0, column=1)

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12)
)
generate_btn.pack(pady=10)

result_var = tk.StringVar()
result_entry = tk.Entry(
    root,
    textvariable=result_var,
    font=("Courier", 12),
    width=35,
    justify="center"
)
result_entry.pack(pady=10)

root.mainloop()
