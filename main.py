import tkinter as tk

from view.menu_view import MenuView

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

if __name__ == "__main__":
    root = tk.Tk()
    # department_dto = DepartmentDto()
    # reviews_dto = ReviewsDto()
    # reviews_frame = tk.Frame()
    # reviews_view = ReviewsView(reviews_frame)
    # department_frame = tk.Frame()
    # departamentView = DepartmentView(department_frame)
    MenuView()
    root.title("Управление персоналом организации")
    root.geometry("1650x1450")
    root.mainloop()
