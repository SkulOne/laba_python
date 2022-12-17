import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from dto.department_dto import DepartmentDto


class DepartmentView:
    def __init__(self, frame):
        self.root = frame
        self.tree = self.init_table()
        self.init_heading()
        button_frame = tk.Frame()
        self.employees_entry = self.init_entry_employees_count(button_frame)
        self.workplace_entry = self.init_entry_workplace_count(button_frame)
        self.init_search_button(button_frame)
        self.init_cancel_button(button_frame)
        button_frame.pack()
        # self.nameEntry = self.init_entry_name()
        # self.directorEntry = self.init_entry_director()
        # self.button = self.init_button()
        # self.search_employees_count = self.init_employees_count()
        # self.search_workplace_count = self.init_workplace_count()
        # user_dto = DepartmentDto()
        # users = user_dto.select_department()
        # self.set_data_to_table(users)
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
        self.root.pack()


    def init_table(self):
        tree = ttk.Treeview(self.root, column=('ID', 'department_name', 'director', 'number_of_employees', 'number_of_jobs'), height=10,
                            show='headings')
        # tree.bind('<Double-1>', self.route)

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

    def init_heading(self):
        label = ttk.Label(text='Таблица "Отделы"', font=font.Font(size=40))
        label.pack()

    def init_employees_count(self):
        frame = tk.Frame()
        frame.pack(pady=20)
        label = ttk.Label(frame, text='Количество сотрудников')
        label.pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT)
        return entry

    def init_workplace_count(self):
        frame = tk.Frame()
        frame.pack(pady=20)
        label = ttk.Label(frame, text='Количество рабочих мест')
        label.pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT)
        return entry

    def search(self):
        employees_count = self.search_employees_count.get()
        workplace_count = self.search_workplace_count.get()
        department_dto = DepartmentDto()
        searched = department_dto.select_staff_by_name_surname(employees_count, workplace_count)
        self.set_data_to_table(searched)

    def init_search_button(self, frame):
        btn = ttk.Button(frame, text="Поиск", command=self.search)
        btn.pack(side=tk.LEFT)
        return btn

    def cancel(self):
        self.employees_entry.delete(0, 'end')
        self.workplace_entry.delete(0, 'end')
        user_dto = DepartmentDto()
        users = user_dto.select_department()
        self.set_data_to_table(users)

    def init_cancel_button(self, frame):
        btn_cancel = ttk.Button(frame, text="Отменить", command=self.cancel)
        btn_cancel.pack(side=tk.RIGHT)
        return btn_cancel

    def init_entry_name(self):
        frame = tk.Frame()
        ttk.Label(frame, text="Наименование").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_director(self):
        frame = tk.Frame()
        ttk.Label(frame, text="Директор").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_employees_count(self, frame):
        entry_frame = ttk.Frame(frame)
        ttk.Label(entry_frame, text="Количество сотрудников").pack(side=tk.LEFT)
        entry = ttk.Entry(entry_frame)
        entry.pack(side=tk.RIGHT)
        entry_frame.pack()
        return entry

    def init_entry_workplace_count(self, frame):
        entry_frame = ttk.Frame(frame)
        ttk.Label(entry_frame, text="Количество рабочих мест").pack(side=tk.LEFT)
        entry = ttk.Entry(entry_frame)
        entry.pack(side=tk.RIGHT)
        entry_frame.pack()
        return entry

    def save(self):
        user_dto = DepartmentDto()
        name = self.nameEntry.get()
        director = self.directorEntry.get()
        employees_count = self.employees_entry.get()
        workplace_count = self.workplace_entry.get()
        if  employees_count and workplace_count:
            user_dto.insert_department(name, director, employees_count, workplace_count)
            users = user_dto.select_department()
            self.set_data_to_table(users)
            self.nameEntry.delete(0, 'end')
            self.directorEntry.delete(0, 'end')
            self.employees_entry.delete(0, 'end')
            self.workplace_entry.delete(0, 'end')

    def init_button(self):
        btn = ttk.Button(text="Добавить", command=self.save)
        btn.pack(side=tk.RIGHT)
        return btn

    def search(self):
        employees_count = self.search_employees_count.get()
        workplace_count = self.search_workplace_count.get()
        department_dto = DepartmentDto()
        searched = department_dto.select_department_by_employees_count_workplace_count(employees_count, workplace_count)
        self.set_data_to_table(searched)

    def set_data_to_table(self, users):
        print('set')
        print(users)
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i in users:
            self.tree.insert('', 'end',
                             values=(i['id'], i['name'], i['director'], i['employees_count'], i['workplace_count']))