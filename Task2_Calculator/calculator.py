from tkinter import *

def click(text):
    value= entry.get()
    entry.delete(0, END)
    entry.insert(0, value + text)

def clear():
    entry.delete(0, END)

def equal():
    display = entry.get()
    if all(c in "0123456789+-*/.()" for c in display):
        result = eval(display)
        entry.delete(0, END)
        entry.insert(0, str(result))
    else:
        entry.delete(0, END)
        entry.insert(0, "Invalid")

calc = Tk()
calc.title("simple  Calculator")
calc.geometry("300x450")

entry = Entry(calc, width=20, font=('Arial', 14), justify=RIGHT)
entry.pack(pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

for row in buttons:
    frame = Frame(calc)
    frame.pack(pady=2)
    for a in row:
        if a == 'C':
            action = clear
        elif a == '=':
            action = equal
        else:
            action = lambda x=a: click(x)
        Button(frame, text=a, width=5, height=2, font=('Arial', 16), command=action).pack(side=LEFT, padx=3)

calc.mainloop()
