import tkinter as tk
import random

root = tk.Tk()
root.title("Party Time 🥳")
root.geometry("450x350")
root.resizable(False, False)

# ===== Clean Joyful Background =====
canvas = tk.Canvas(root, width=450, height=350, bg="#ffe4e1", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Optional: Add subtle circles for a fun vibe 🎉
for _ in range(10):
    x = random.randint(20, 400)
    y = random.randint(20, 300)
    r = random.randint(10, 30)
    canvas.create_oval(x, y, x+r, y+r, fill="#ffb6c1", outline="")

# ===== Message =====
label = tk.Label(
    root,
    text="😍 Hey \nWill you give me Birthday Party? 🎉🥳",
    font=("Segoe UI Emoji", 16),
    fg="#8b0000",
    bg="#ffe4e1",
    justify="center"
)
canvas.create_window(225, 90, window=label)

# ===== Button Functions =====
def yes_clicked():
    label.config(text="🎊 Yayyy! Party confirmed! 😄🎂")
    yes_btn.config(state="disabled")
    no_btn.config(state="disabled")

def move_button(event):
    x = random.randint(50, 380)
    y = random.randint(180, 300)
    canvas.coords(no_window, x, y)

# ===== Buttons =====
yes_btn = tk.Button(
    root,
    text="Yes 🎉",
    font=("Segoe UI Emoji", 12, "bold"),
    bg="#ff69b4",
    fg="white",
    activebackground="#ff1493",
    width=10,
    command=yes_clicked
)

no_btn = tk.Button(
    root,
    text="No 😅",
    font=("Segoe UI Emoji", 12, "bold"),
    bg="#db7093",
    fg="white",
    width=10
)

yes_window = canvas.create_window(140, 230, window=yes_btn)
no_window = canvas.create_window(300, 230, window=no_btn)

no_btn.bind("<Enter>", move_button)

root.mainloop()