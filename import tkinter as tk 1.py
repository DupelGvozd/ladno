import tkinter as tk

def say_hello():
    name = entry.get()
    if name.strip():
        greeting_label.config(text=f"Привет, {name}!")
    else:
        greeting_label.config(text="Пожалуйста, введите имя.")

root = tk.Tk()
root.title("Простое приветствие")

# Поле ввода имени
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Кнопка
button = tk.Button(root, text="Поздороваться", command=say_hello)
button.pack(pady=5)

# Метка для вывода приветствия
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=10)

root.mainloop()