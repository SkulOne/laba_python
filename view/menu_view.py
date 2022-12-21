import tkinter as tk

from view.department_view import DepartmentView
from view.reviews_view import ReviewsView
from view.staff_view import StaffView


class MenuView:
    def __init__(self):
        self.root = tk.Frame()
        self.view = None
        self.menu_item('Отзывы', ReviewsView)
        self.menu_item('Отделы', DepartmentView)
        self.menu_item('Сотрудники', StaffView)
        self.exit_button = None
        self.root.pack()

    def menu_item(self, name, view):
        button = tk.Button(self.root, text=name, command=lambda: self.create_view(view))
        button.pack()
        return button

    def create_view(self, view):
        self.root.destroy()
        self.view = view(tk.Frame())
        self.exit_button = self.init_exit_button()

    def init_exit_button(self):
        btn = tk.Button(text='Выйти', command=self.exit)
        btn.place(relx=0.70)
        return btn

    def exit(self):
        self.exit_button.destroy()
        self.root.destroy()
        self.view.root.destroy()
        self.__init__()
