import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from dto.department_dto import DepartmentDto


class DepartmentView:
    def __init__(self, frame):
        self.tree = self.init_table()
        user_dto = DepartmentDto()
        users = user_dto.create_table()
        self.root = frame
        # self.init_heading()
        # self.search_surname = self.init_search_surname()
        # self.search_name = self.init_search_name()
        # self.init_search_button()
        # self.init_cancel_button()
        # self.tree = self.init_table()
        # user_dto = DepartmentDto()
        # users = user_dto.select_staff()
        # self.set_data_to_table(users)
        # self.surnameEntry = self.init_entry_surname()
        # self.nameEntry = self.init_entry_name()
        # self.patronymicEntry = self.init_entry_patronymic()
        # self.phoneEntry = self.init_entry_phone()
        # self.emailEntry = self.init_entry_email()
        # self.button = self.init_button()
        # self.root.pack()


    def init_table(self):
        tree = ttk.Treeview(self.root, column=('ID', 'department_name', 'director', 'number_of_employees', 'number_of_jobs'), height=10,
                            show='headings')
        tree.bind('<Double-1>', self.route)

        tree.column('ID', width=35, anchor=tk.CENTER)
        tree.column('department_name', anchor=tk.CENTER)
        tree.column('director', anchor=tk.CENTER)
        tree.column('number_of_employees', anchor=tk.CENTER)
        tree.column('number_of_jobs', anchor=tk.CENTER)

        tree.heading('ID', text='ID')
        tree.heading('department_name', text='Наименование')
        tree.heading('director', text='Руководитель')
        tree.heading('number_of_employees', text='Количество сотрудников')
        tree.heading('number_of_jobs', text='Количество рабочих мест')
        tree.pack()
        return tree

