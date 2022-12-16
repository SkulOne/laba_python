import tkinter as tk
from tkinter import ttk

from dto.department_dto import DepartmentDto
from dto.reviews_dto import ReviewsDto
from dto.staff_dto import StaffDto
from view.staff_view import StaffView
from view.department import DepartmentView

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

if __name__ == "__main__":
    root = tk.Tk()
    department_dto = DepartmentDto()
    reviews_dto = ReviewsDto()
    # staff_dto = StaffDto()
    # staff_dto.insert_staff()
    department = tk.Frame()
    # departamentView = DepartmentView(department)
    root.title("Управление персоналом организации")
    root.geometry("1650x1450")
    root.mainloop()
