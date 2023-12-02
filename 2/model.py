import tkinter as tk


class Calculator:
    def __init__(self, master):  # Инициализация класса
        self.master = master  # Инициализация окна приложения
        self.master.title("Calculator")  # Задаю название окна приложения

        self.entry_num1 = tk.Entry(self.master,
                                   width=20)  # Инициализация окна в который можно записать число(ширина =20)
        self.entry_num1.pack(pady=5)  # Размещение этого окна на 5 едениц ниже верхней границы

        self.entry_num2 = tk.Entry(self.master,
                                   width=20)  # Инициализация окна в который можно записать второе число(ширина =20)
        self.entry_num2.pack()  # Размещение этого окна впритык к прошлому окну

        self.result = tk.Entry(self.master,
                               state="readonly")  # Инициализация окна с ответом изначально заблокированное для ввода
        self.result.pack(pady=5)  # Размещение этого окна на 5 ниже прошлого окна ввода

        self.create_operation_buttons()  # Вызов фуекции создания кнопок

    def create_operation_buttons(self):  # Функция создания кнопок
        plus_button = tk.Button(self.master, text="+", command=self.plus,
                                width=20)  # Инициализация кнопки "+", с шириной 20
        plus_button.pack(pady=5)  # Размещение этой кнпоки на 5 едениц ниже последнего окна

        minus_button = tk.Button(self.master, text="-", command=self.minus,
                                 width=20)  # Инициализация кнопки "-", с шириной 20
        minus_button.pack()  # Размещение этой кнпоки впритык к прошлой

        multiply_button = tk.Button(self.master, text="*", command=self.multiply,
                                    width=20)  # Инициализация кнопки "*", с шириной 20
        multiply_button.pack()  # Размещение этой кнпоки впритык к прошлой

        divide_button = tk.Button(self.master, text="/", command=self.divide,
                                  width=20)  # Инициализация кнопки "/", с шириной 20
        divide_button.pack()  # Размещение этой кнпоки впритык к прошлой

    def plus(self):  # Функция которая сработает после нажатия кнопки "+"
        try:  # Проверка на неправильный ввод чисел
            num1 = float(self.entry_num1.get())  # Берет число из первого окна ввода
            num2 = float(self.entry_num2.get())  # Берет число из второго окна ввода
            res = num1 + num2  # Находит их сумму
            self.print_result(res)  # Вызывает функцию вывода результата
        except ValueError:  # Если число неправильное, выводи ошибку вместо ответа
            self.print_result("Invalid input")

    def minus(self):  # Функция которая сработает после нажатия кнопки "-"
        try:  # Проверка на неправильный ввод чисел
            num1 = float(self.entry_num1.get())  # Берет число из первого окна ввода
            num2 = float(self.entry_num2.get())  # Берет число из второго окна ввода
            res = num1 - num2  # Находит их разность
            self.print_result(res)  # Вызывает функцию вывода результата
        except ValueError:  # Если число неправильное, выводи ошибку вместо ответа
            self.print_result("Invalid input")

    def multiply(self):  # Функция которая сработает после нажатия кнопки "*"
        try:  # Проверка на неправильный ввод чисел
            num1 = float(self.entry_num1.get())  # Берет число из первого окна ввода
            num2 = float(self.entry_num2.get())  # Берет число из второго окна ввода
            res = num1 * num2  # Находит резултат умножения
            self.print_result(res)  # Вызывает функцию вывода результата
        except ValueError:  # Если число неправильное, выводи ошибку вместо ответа
            self.print_result("Invalid input")

    def divide(self):  # Функция которая сработает после нажатия кнопки "/"
        try:  # Проверка на неправильный ввод чисел или деление на 0
            num1 = float(self.entry_num1.get())  # Берет число из первого окна ввода
            num2 = float(self.entry_num2.get())  # Берет число из второго окна ввода
            res = num1 / num2  # Находит резултат деления
            self.print_result(res)  # Вызывает функцию вывода результата
        except ValueError:  # Если число неправильное, выводи ошибку вместо ответа
            self.print_result("Invalid input")
        except ZeroDivisionError:  # Если второе число - 0, выводи ошибку вместо ответа
            self.print_result("Cannot divide by zero")

    def print_result(self, result):  # Функция вывода результата
        self.result.config(state="normal")  # Перевод окно отаета в режим изменения
        self.result.delete(0, tk.END)  # Очищает окно ответа
        self.result.insert(0, result)  # Записывает в окно ответа результат
        self.result.config(state="readonly")  # Закрывает ввод числа в окно ответа
