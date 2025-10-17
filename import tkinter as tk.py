import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showwarning("Ошибка", "Введите корректное число!")
        return

    attempts += 1
    attempts_label.config(text=f"Попыток: {attempts}")

    if guess < secret_number:
        result_label.config(text="Больше!")
    elif guess > secret_number:
        result_label.config(text="Меньше!")
    else:
        result_label.config(text="Угадали! 🎉")
        messagebox.showinfo("Поздравляем!", f"Вы угадали число {secret_number} за {attempts} попыток!")
        reset_game()

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    attempts_label.config(text="Попыток: 0")
    result_label.config(text="")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Угадай число")
root.geometry("300x200")

secret_number = random.randint(1, 100)
attempts = 0

instruction_label = tk.Label(root, text="Загадано число от 1 до 100. Попробуйте угадать!")
instruction_label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack()

check_button = tk.Button(root, text="Проверить", command=check_guess)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=5)

attempts_label = tk.Label(root, text="Попыток: 0")
attempts_label.pack()

root.mainloop()