import tkinter as tk

def change_theme():
    theme = theme_var.get()
    if theme == "light":
        root.config(bg="white")
        label.config(bg="white", fg="black")
    elif theme == "dark":
        root.config(bg="black")
        label.config(bg="black", fg="white")

root = tk.Tk()
root.title("Переключатель тем")
root.geometry("300x150")

theme_var = tk.StringVar(value="light")  # Значение по умолчанию

# Метка с текстом
label = tk.Label(root, text="Выберите тему", bg="white", fg="black", font=("Arial", 14))
label.pack(pady=10)

# Радиокнопки
rb_light = tk.Radiobutton(root, text="Светлая тема", variable=theme_var, value="light",
                          command=change_theme, bg="white", fg="black", selectcolor="white")
rb_light.pack()

rb_dark = tk.Radiobutton(root, text="Темная тема", variable=theme_var, value="dark",
                         command=change_theme, bg="white", fg="black", selectcolor="white")
rb_dark.pack()

root.mainloop()