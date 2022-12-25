import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from dto.department_dto import DepartmentDto

class DepartmentView:
    def __init__(self, frame):
        self.root = frame
        self.search_block = tk.Frame(self.root)
        self.init_heading()

        # Инициализируем блок поиска
        button_frame = tk.Frame(self.root)
        self.search_employees_entry = self.init_search_by_employees_count()
        self.search_workplace_entry = self.init_search_by_workplace_count()
        self.init_search_button(button_frame)
        self.init_cancel_button(button_frame)
        button_frame.pack()

        # Инициализируем таблицу
        self.tree = self.init_table()
        department_dto = DepartmentDto()
        departments = department_dto.select_department()
        self.set_data_to_table(departments)

        # Инициализируем блок добавления
        self.name_entry = self.init_entry_name()
        self.director_entry = self.init_entry_director()
        self.employees_count_entry = self.init_entry_employees_count()
        self.workplace_count_entry = self.init_entry_workplace_count()
        self.add_button = self.init_add_button()
        self.root.pack()
        self.search_block.pack()


    def init_table(self):
        tree = ttk.Treeview(self.root, column=('ID', 'department_name', 'director', 'number_of_employees', 'number_of_jobs', 'edit', 'delete'), height=10,
                            show='headings')
        tree.bind('<ButtonRelease-1>', self.select_item)

        tree.column('ID', width=35, anchor=tk.CENTER)
        tree.column('department_name', anchor=tk.CENTER)
        tree.column('director', anchor=tk.CENTER)
        tree.column('number_of_employees', anchor=tk.CENTER)
        tree.column('number_of_jobs', anchor=tk.CENTER)
        tree.column('edit', anchor=tk.CENTER, width=75)
        tree.column('delete', anchor=tk.CENTER, width=75)


        tree.heading('ID', text='ID')
        tree.heading('department_name', text='Наименование')
        tree.heading('director', text='Руководитель')
        tree.heading('number_of_employees', text='Количество сотрудников')
        tree.heading('number_of_jobs', text='Количество рабочих мест')
        tree.heading('edit', text='Правка')
        tree.heading('delete', text='Удалить')
        tree.pack()
        return tree

    def select_item(self, event):
        cur_item = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)[1]
        method = cur_item['values'][int(col) - 1]
        if method == 'УДАЛИТЬ':
            department_dto = DepartmentDto()
            department_dto.delete_by_id(cur_item['values'][0])
            self.set_data_to_table(department_dto.select_department())
        if method == 'ПРАВКА':
            self.name_entry.insert(0, cur_item['values'][1])
            self.director_entry.insert(0, cur_item['values'][2])
            self.employees_count_entry.insert(0, cur_item['values'][3])
            self.workplace_count_entry.insert(0, cur_item['values'][4])
            self.add_button.config(text='Править', command=lambda: self.update(cur_item['values'][0]))

    def init_heading(self):
        label = ttk.Label(self.root, text='Таблица "Отделы"', font=font.Font(size=40))
        label.pack()

    def init_search_by_employees_count(self):
        entry_frame = ttk.Frame(self.root)
        ttk.Label(entry_frame, text="Количество сотрудников").pack(side=tk.LEFT)
        entry = ttk.Entry(entry_frame)
        entry.pack(side=tk.RIGHT)
        entry_frame.pack()
        return entry

    def init_search_by_workplace_count(self):
        entry_frame = ttk.Frame(self.root)
        ttk.Label(entry_frame, text="Количество рабочих мест").pack(side=tk.LEFT)
        entry = ttk.Entry(entry_frame)
        entry.pack(side=tk.RIGHT)
        entry_frame.pack()
        return entry

    def search(self):
        employees_count = self.search_employees_entry.get()
        workplace_count = self.search_workplace_entry.get()
        department_dto = DepartmentDto()
        searched = department_dto.select_department_by_employees_count_workplace_count(employees_count, workplace_count)
        self.set_data_to_table(searched)

    def init_search_button(self, frame):
        btn = ttk.Button(frame, text="Поиск", command=self.search)
        btn.pack(side=tk.LEFT, padx=0)
        return btn

    def cancel(self):
        self.search_employees_entry.delete(0, 'end')
        self.search_workplace_entry.delete(0, 'end')
        user_dto = DepartmentDto()
        users = user_dto.select_department()
        self.set_data_to_table(users)

    def init_cancel_button(self, frame):
        btn_cancel = ttk.Button(frame, text="Отменить", command=self.cancel)
        btn_cancel.pack(side=tk.RIGHT)
        return btn_cancel

    def init_entry_name(self):
        frame = tk.Frame(self.search_block)
        ttk.Label(frame, text="Наименование").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_director(self):
        frame = tk.Frame(self.search_block)
        ttk.Label(frame, text="Директор").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_employees_count(self):
        frame = tk.Frame(self.search_block)
        ttk.Label(frame, text='Количество сотрудников').pack()
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT)
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_workplace_count(self):
        frame = tk.Frame(self.search_block)
        ttk.Label(frame, text='Количество рабочих мест').pack()
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT)
        frame.pack(side=tk.LEFT)
        return entry

    def save(self):
        department_dto = DepartmentDto()
        name = self.name_entry.get()
        director = self.director_entry.get()
        employees_count = self.employees_count_entry.get()
        workplace_count = self.workplace_count_entry.get()
        if employees_count and workplace_count and employees_count and workplace_count:
            department_dto.insert_department(name, director, employees_count, workplace_count)
            users = department_dto.select_department()
            self.set_data_to_table(users)
            self.name_entry.delete(0, 'end')
            self.director_entry.delete(0, 'end')
            self.search_employees_entry.delete(0, 'end')
            self.search_workplace_entry.delete(0, 'end')

    def init_add_button(self):
        btn = ttk.Button(self.search_block, text="Добавить", command=self.save)
        btn.pack(side=tk.RIGHT)
        return btn

    def search(self):
        employees_count = self.search_employees_entry.get()
        workplace_count = self.search_workplace_entry.get()
        department_dto = DepartmentDto()
        searched = department_dto.select_department_by_employees_count_workplace_count(employees_count, workplace_count)
        self.set_data_to_table(searched)

    def set_data_to_table(self, departments):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i in departments:
            self.tree.insert('', 'end',
                             values=(i['id'], i['name'], i['director'], i['employees_count'], i['workplace_count'], 'ПРАВКА', 'УДАЛИТЬ'))


    def update(self, id):
        department_dto = DepartmentDto()
        name_value = self.name_entry.get()
        director_value = self.director_entry.get()
        employees_value = self.employees_count_entry.get()
        workplace_count_value = self.workplace_count_entry.get()
        if name_value and director_value and employees_value and workplace_count_value:
            department_dto.update(id, name_value, director_value, employees_value, workplace_count_value)
        self.name_entry.delete(0, tk.END)
        self.director_entry.delete(0, tk.END)
        self.employees_count_entry.delete(0, tk.END)
        self.workplace_count_entry.delete(0, tk.END)
        self.add_button.config(text='Добавить', command=self.save)
        self.set_data_to_table(department_dto.select_department())
