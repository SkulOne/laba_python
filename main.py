import tkinter as tk
from tkinter import ttk

from dto.department_dto import DepartmentDto
from dto.reviews_dto import ReviewsDto
from dto.staff_dto import StaffDto
from view.reviews_view import ReviewsView
from view.staff_view import StaffView
from view.department_view import DepartmentView

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

if __name__ == "__main__":
    root = tk.Tk()
    # department_dto = DepartmentDto()
    reviews_dto = ReviewsDto()
    reviews_frame = tk.Frame()
    reviews_view = ReviewsView(reviews_frame)
    # department_frame = tk.Frame()
    # departamentView = DepartmentView(department_frame)
    root.title("Управление персоналом организации")
    root.geometry("1650x1450")
    root.mainloop()
