import tkinter as tk
from model import RainbowApp

# Просто запуск всего)
def main():
    root = tk.Tk()
    app = RainbowApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
