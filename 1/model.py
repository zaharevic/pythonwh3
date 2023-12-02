import tkinter as tk

rainbow_colors = {
    "Красный": "#FF0000",
    "Оранжевый": "#FFA500",
    "Желтый": "#FFFF00",
    "Зеленый": "#008000",
    "Голубой": "#42AAFF",
    "Синий": "#0000FF",
    "Фиолетовый": "#8B00FF"
}  # Словарик понадобится далее


class RainbowApp:  # Класс в котором храниться вся логика
    def __init__(self, master):  # Инициализация, класса, по сути что будет написано в master - не важно, но пусть будет
        self.master = master
        self.master.title("Rainbow Colors")  # Задаю шапку приложения

        self.color_label = tk.Label(
            text="Выберите цвет")  # Инициализирую Label, с изначальным текстом, после нажатия будет название цвета
        self.color_label.pack(pady=10)  # Создаю Label, с отступом по y в 10 едениц относительно шапки

        self.color_entry = tk.Entry(
            state="readonly")  # Инициализирую строку где будет выводится код цвета, изначально- пустая и в ней
        # запрещенно писать
        self.color_entry.pack(pady=10)  # Создаю строку, с отступом по y в 10 едениц относительно Label

        self.create_color_buttons()  # Вызываю функцию создающую кнопки

    def create_color_buttons(self):  # Функция создающая кнопки
        for color_name, color_code in rainbow_colors.items():  # Перебираются кнопки, вызываемые из словоря
            button = tk.Button(text="\t\n\t", bg=color_code,
                               command=lambda c=color_code, n=color_name: self.show_color(c, n))
            # Кнопки инициализируются, в text ввел значения, чтоб кнопка не была слишком маленькой, для bg(цвета фона)
            # береться код из словоря, название и номер цвета передаются в переменные n и с соответственно, через
            # лямбда-функцию и передаются в функцию для изменения интерфейса
            button.pack(side=tk.LEFT)  # Создаются конпки с выравниванием по левой стороне

    def show_color(self, color_code,
                   color_name):  # Функция для изменения интерфейса, принимает название и код цвета соответственно
        self.color_label.config(text=color_name)  # Меняет текст Label на название цвета
        self.color_entry.config(state="normal")  # Позволяет записать в строку с кодом
        self.color_entry.delete(0, tk.END)  # Обнуляет значение строки с кодом
        self.color_entry.insert(0, color_code)  # Записывает в строку с кодом новое значение
        self.color_entry.config(state="readonly")  # Запрещает изменение строки с кодом
