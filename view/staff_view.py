import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from dto.staff_dto import StaffDto


class StaffView:
    def __init__(self):
        self.init_heading()
        self.search_name = self.init_search_name()
        self.search_surname = self.init_search_surname()
        self.init_search_button()
        self.init_cancel_button()
        self.tree = self.init_table()
        user_dto = StaffDto()
        users = user_dto.select_staff()
        self.set_data_to_table(users)
        self.surnameEntry = self.init_entry_surname()
        self.nameEntry = self.init_entry_name()
        self.patronymicEntry = self.init_entry_patronymic()
        self.phoneEntry = self.init_entry_phone()
        self.emailEntry = self.init_entry_email()
        self.button = self.init_button()

    def init_table(self):
        tree = ttk.Treeview(column=('ID', 'Surname', 'Name', 'Patronymic', 'Phone', 'Email'), height=10,
                            show='headings')

        tree.column('ID', width=35, anchor=tk.CENTER)
        tree.column('Surname', anchor=tk.CENTER)
        tree.column('Name', anchor=tk.CENTER)
        tree.column('Patronymic', anchor=tk.CENTER)
        tree.column('Phone', anchor=tk.CENTER)
        tree.column('Email', anchor=tk.CENTER)

        tree.heading('ID', text='ID')
        tree.heading('Surname', text='Фамилия')
        tree.heading('Name', text='Имя')
        tree.heading('Patronymic', text='Отчество')
        tree.heading('Phone', text='Телефон')
        tree.heading('Email', text='Email')
        tree.pack()
        return tree

    def init_heading(self):
        label = ttk.Label(text='Таблица "Заголовки"', font=font.Font(size=40))
        label.pack()

    def init_search_name(self):
        frame = tk.Frame()
        frame.pack(pady=20)
        label = ttk.Label(frame, text='Имя')
        label.pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT)
        return entry

    def search(self):
        surname = self.search_surname.get()
        name = self.search_name.get()
        staff_dto = StaffDto()
        searched = staff_dto.select_staff_by_name_surname(surname, name)
        self.set_data_to_table(searched)


    def init_search_button(self):
        btn = ttk.Button(text="Поиск", command=self.search)
        btn.pack()
        return btn

    def cancel(self):
        self.search_name.delete(0, 'end')
        self.search_surname.delete(0, 'end')
        user_dto = StaffDto()
        users = user_dto.select_staff()
        self.set_data_to_table(users)

    def init_cancel_button(self):
        btn_cancel = ttk.Button(text="Отменить", command=self.cancel)
        btn_cancel.pack()
        return btn_cancel

    def init_search_surname(self):
        frame = tk.Frame()
        frame.pack(pady=20)
        label = ttk.Label(frame, text='Фамилия')
        label.pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT)
        return entry

    def init_entry_surname(self):
        frame = tk.Frame()
        ttk.Label(frame, text="Фамилия").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_name(self):
        frame = tk.Frame()
        ttk.Label(frame, text="Имя").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_patronymic(self):
        frame = tk.Frame()
        ttk.Label(frame, text="Отчество").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_phone(self):
        frame = tk.Frame()
        ttk.Label(frame, text="Телефон").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_email(self):
        frame = tk.Frame()
        ttk.Label(frame, text="Почта").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def save(self):
        user_dto = StaffDto()
        name = self.nameEntry.get()
        surname = self.surnameEntry.get()
        patronymic = self.patronymicEntry.get()
        phone = self.phoneEntry.get()
        email = self.emailEntry.get()
        if name and surname:
            user_dto.insert_staff(surname, name, patronymic, phone, email)
            users = user_dto.select_staff()
            self.set_data_to_table(users)
            self.nameEntry.delete(0, 'end')
            self.surnameEntry.delete(0, 'end')
            self.patronymicEntry.delete(0, 'end')
            self.phoneEntry.delete(0, 'end')
            self.emailEntry.delete(0, 'end')

    def init_button(self):
        btn = ttk.Button(text="Добавить", command=self.save)
        btn.pack(side=tk.RIGHT)
        return btn

    def set_data_to_table(self, users):
        print('set')
        print(users)
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i in users:
            self.tree.insert('', 'end',
                             values=(i['id'], i['surname'], i['name'], i['patronymic'], i['phone'], i['email']))
