import tkinter as tk
import random

def generate():
    length = int(entry.get())
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''
    for i in range(length):
        password += random.choice(letters)
    result.config(text=password)

pswd = tk.Tk()
pswd.title("Password Generator")

tk.Label(pswd, text="Enter Length:").pack()
entry = tk.Entry(pswd)
entry.pack()

tk.Button(pswd, text="Generate Password", command=generate).pack()
result = tk.Label(pswd, text="")
result.pack()

pswd.mainloop()
