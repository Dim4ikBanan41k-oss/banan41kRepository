import tkinter as tk
import random

# Переменная со ссылкой на GitHub-репозиторий
git_hub = "https://github.com/Dim4ikBanan41k-oss/banan41kRepository"

# Список интересных фактов
facts = [
    "Бананы радиоактивны и излучают небольшое количество гамма-излучения.",
    "Человек может обойтись без пищи до 2 месяцев, а без воды — всего несколько дней.",
    "Голубые киты ежедневно потребляют около 4 тонн пищи.",
    "Пчёлы могут распознавать лица людей.",
    "Существует 6 000 видов бананов, а не только один."
]

def show_random_fact():
    """Выбирает случайный факт из списка и обновляет метку"""
    random_fact = random.choice(facts)
    fact_label.config(text=random_fact)

# Создаём главное окно
root = tk.Tk()
root.title("Случайные интересные факты")
root.geometry("600x250")
root.resizable(False, False)

# Метка для вывода факта (изначально пустая или с приветствием)
fact_label = tk.Label(
    root,
    text="Нажмите кнопку, чтобы узнать интересный факт",
    wraplength=550,
    font=("Arial", 12),
    justify="center",
    relief="solid",
    padx=10,
    pady=20
)
fact_label.pack(pady=30)

# Кнопка "Показать факт"
show_button = tk.Button(
    root,
    text="Показать факт",
    command=show_random_fact,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
)
show_button.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()
