import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def edit_task():
    try:
        index = listbox.curselection()
        task = entry.get()
        task = listbox.get(index)
        entry.delete(0, tk.END)
        entry.insert(tk.END, task)
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to edit.")


window = tk.Tk()
window.title("To-Do List")
window.config(bg="#000000")
window.geometry('550x450')
window.resizable(True, True)

heading_font = ("Times", 15, "underline", "bold")
label_font = ("Helvetica", 12, "bold")

heading = tk.Label(window, text="To-Do List", bg="#000000",
                   fg="#ffffff", font=heading_font)
heading.pack(pady=15)

listbox = tk.Listbox(window, height=10, width=50, bg="#222222",
                     fg="#ffffff", selectbackground="#4c6a9c", font=label_font)
listbox.pack(pady=10)

scrollbar = tk.Scrollbar(window)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

entry = tk.Entry(window, font=label_font, bg="#ffffff", fg="#000000")
entry.pack(pady=10)

button_frame = tk.Frame(window, bg="#000000")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task",
                       command=add_task, background="#808080", font=label_font)
add_button.grid(row=0, column=0, padx=5)

edit_button = tk.Button(button_frame, text="Edit Task",
                        command=edit_task, background="#808080", font=label_font)
edit_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task",
                          command=delete_task, background="#808080", font=label_font)
delete_button.grid(row=0, column=2, padx=5)

window.mainloop()
