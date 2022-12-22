import datetime
import tkinter as tk

from tkcalendar import DateEntry
from view.menu_view import MenuView

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

if __name__ == "__main__":
    root = tk.Tk()
    MenuView()
    root.title("Управление персоналом организации")
    root.geometry("1650x1450")
    root.mainloop()
