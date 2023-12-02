from model import Calculator
import tkinter as tk

def main():  # Просто запуск model
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
