import tkinter as tk
from tkinter import ttk

from dto.staff_dto import StaffDto
from view.staff_view import StaffView
from view.department import DepartmentView

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

if __name__ == "__main__":
    root = tk.Tk()
    department = tk.Frame()
    departamentView = DepartmentView(department)
    root.title("Управление персоналом организации")
    root.geometry("1650x1450")
    root.mainloop()
