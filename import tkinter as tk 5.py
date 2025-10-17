import tkinter as tk

def button_click(value):
    current = entry.get()
    if value == "=":
        try:
            # Вычисляем выражение
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Ошибка")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Простой калькулятор")

entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Кнопки цифр и операций
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                    command=lambda val=text: button_click(val))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()