import tkinter as tk
from tkinter import messagebox

todo_aap=tk.Tk()
todo_aap.title("To-Do List")
todo_aap.geometry("300x500")

tasks=[]

def add_task():
    task=entry.get()
    if not task:
        messagebox.showinfo("ALERT","Please enter a task")
    else:
        tasks.append(task)
        update_listbox()
        entry.delete(0,tk.END)
        
def delete_task():
    selected=listbox.curselection()
    if selected:
        task_index=selected[0]
        tasks.pop(task_index)
        update_listbox()
    else:
        messagebox.showinfo("ALERT","Please select the task to delete")

def update_listbox():
    listbox.delete(0,tk.END)
    for task in tasks:
        listbox.insert(tk.END,task)

heading=tk.Label(todo_aap, text="My To-Do List", font=("Arial",20,"bold"))
heading.pack(pady=10)

entry = tk.Entry(todo_aap, font=("Arial",18), width=25)
entry.pack(pady=10)

add_btn = tk.Button(todo_aap, text="Add Task", command=add_task, bg="light blue", fg="black", width=25)
add_btn.pack(pady=10)

listbox = tk.Listbox(todo_aap, font=("Arial", 18), width=25, height=15)
listbox.pack(pady=10)

del_btn = tk.Button(todo_aap, text="Delete Selected Task", command=delete_task, bg="red", fg="black", width=30)
del_btn.pack(pady=10)

todo_aap.mainloop()
