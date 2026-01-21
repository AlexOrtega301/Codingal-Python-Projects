import tkinter as tk
import random

# --- Game Logic ---
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}"
    )

# --- Tkinter GUI ---
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(root, text="🪨📄✂️ Rock Paper Scissors", font=("Arial", 16, "bold"))
title.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=20)

root.mainloop()
