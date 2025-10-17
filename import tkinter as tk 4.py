import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Открыть файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            text_field.delete("1.0", tk.END)
            text_field.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")

def save_as_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
        title="Сохранить файл как"
    )
    if file_path:
        try:
            content = text_field.get("1.0", tk.END)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("Успех", "Файл успешно сохранён")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")

root = tk.Tk()
root.title("Текстовый редактор")
root.geometry("600x400")

# Меню
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as_file)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

# Большое текстовое поле
text_field = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_field.pack(expand=True, fill=tk.BOTH)

root.mainloop()