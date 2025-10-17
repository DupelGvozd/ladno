import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Пустая задача", "Введите текст задачи!")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Выбор отсутствует", "Выберите задачу для удаления!")

root = tk.Tk()
root.title("Список дел")
root.geometry("300x350")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

btn_add = tk.Button(root, text="Добавить", width=20, command=add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Удалить", width=20, command=delete_task)
btn_delete.pack(pady=5)

listbox_tasks = tk.Listbox(root, width=40, height=10)
listbox_tasks.pack(pady=10)

root.mainloop()