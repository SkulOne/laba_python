import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from dto.staff_dto import StaffDto


class StaffView:
    def __init__(self, frame):
        self.root = frame
        self.init_heading()
        self.search_surname = self.init_search_surname()
        self.search_name = self.init_search_name()
        self.init_search_button()
        self.init_cancel_button()
        self.tree = self.init_table()
        user_dto = StaffDto()
        users = user_dto.select_staff()
        self.set_data_to_table(users)
        self.surname_entry = self.init_entry_surname()
        self.name_entry = self.init_entry_name()
        self.patronymic_entry = self.init_entry_patronymic()
        self.phone_entry = self.init_entry_phone()
        self.email_entry = self.init_entry_email()
        self.add_button = self.init_add_button()
        self.root.pack()

    def init_table(self):
        tree = ttk.Treeview(self.root,
                            column=('ID', 'Surname', 'Name', 'Patronymic', 'Phone', 'Email', 'edit', 'delete'),
                            height=10,
                            show='headings')
        tree.bind('<ButtonRelease-1>', self.select_item)
        tree.column('ID', width=35, anchor=tk.CENTER)
        tree.column('Surname', anchor=tk.CENTER)
        tree.column('Name', anchor=tk.CENTER)
        tree.column('Patronymic', anchor=tk.CENTER)
        tree.column('Phone', anchor=tk.CENTER)
        tree.column('Email', anchor=tk.CENTER)
        tree.column('edit', anchor=tk.CENTER, width=75)
        tree.column('delete', anchor=tk.CENTER, width=75)

        tree.heading('ID', text='ID')
        tree.heading('Surname', text='Фамилия')
        tree.heading('Name', text='Имя')
        tree.heading('Patronymic', text='Отчество')
        tree.heading('Phone', text='Телефон')
        tree.heading('Email', text='Email')
        tree.heading('edit', text='Правка')
        tree.heading('delete', text='Удалить')
        tree.pack()
        return tree

    def init_heading(self):
        label = ttk.Label(self.root, text='Таблица "Заголовки"', font=font.Font(size=40))
        label.pack()

    def select_item(self, event):
        cur_item = self.tree.item(self.tree.focus())
        print(cur_item)
        col = self.tree.identify_column(event.x)[1]
        method = cur_item['values'][int(col) - 1]
        if method == 'УДАЛИТЬ':
            staff_dto = StaffDto()
            staff_dto.delete_by_id(cur_item['values'][0])
            self.set_data_to_table(staff_dto.select_staff())
        if method == 'ПРАВКА':
            self.surname_entry.insert(0, cur_item['values'][1])
            self.name_entry.insert(0, cur_item['values'][2])
            self.patronymic_entry.insert(0, cur_item['values'][3])
            self.phone_entry.insert(0, cur_item['values'][4])
            self.email_entry.insert(0, cur_item['values'][5])
            self.add_button.config(text='Править', command=lambda: self.update(cur_item['values'][0]))

    def update(self, id):
        staff_dto = StaffDto()
        surname_entry_value = self.surname_entry.get()
        name_entry_value = self.name_entry.get()
        patronymic_entry_value = self.patronymic_entry.get()
        phone_entry_value = self.phone_entry.get()
        email_entry_value = self.email_entry.get()
        if surname_entry_value and name_entry_value and patronymic_entry_value and phone_entry_value and email_entry_value:
            staff_dto.update(id, surname_entry_value, name_entry_value, patronymic_entry_value, phone_entry_value, email_entry_value)
        self.surname_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.patronymic_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.add_button.config(text='Добавить', command=self.save)
        self.set_data_to_table(staff_dto.select_staff())


    def init_search_name(self):
        frame = tk.Frame(self.root)
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
        searched = staff_dto.select_staff_by_surname_name(surname, name)
        self.set_data_to_table(searched)

    def init_search_button(self):
        btn = ttk.Button(self.root, text="Поиск", command=self.search)
        btn.pack()
        return btn

    def cancel(self):
        self.search_name.delete(0, 'end')
        self.search_surname.delete(0, 'end')
        user_dto = StaffDto()
        users = user_dto.select_staff()
        self.set_data_to_table(users)

    def init_cancel_button(self):
        btn_cancel = ttk.Button(self.root, text="Отменить", command=self.cancel)
        btn_cancel.pack()
        return btn_cancel

    def init_search_surname(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        label = ttk.Label(frame, text='Фамилия')
        label.pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT)
        return entry

    def init_entry_surname(self):
        frame = tk.Frame(self.root)
        ttk.Label(frame, text="Фамилия").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_name(self):
        frame = tk.Frame(self.root)
        ttk.Label(frame, text="Имя").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_patronymic(self):
        frame = tk.Frame(self.root)
        ttk.Label(frame, text="Отчество").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_phone(self):
        frame = tk.Frame(self.root)
        ttk.Label(frame, text="Телефон").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def init_entry_email(self):
        frame = tk.Frame(self.root)
        ttk.Label(frame, text="Почта").pack()
        entry = ttk.Entry(frame)
        entry.pack()
        frame.pack(side=tk.LEFT)
        return entry

    def save(self):
        user_dto = StaffDto()
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        patronymic = self.patronymic_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and surname:
            user_dto.insert_staff(surname, name, patronymic, phone, email)
            users = user_dto.select_staff()
            self.set_data_to_table(users)
            self.name_entry.delete(0, 'end')
            self.surname_entry.delete(0, 'end')
            self.patronymic_entry.delete(0, 'end')
            self.phone_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')

    def init_add_button(self):
        btn = ttk.Button(self.root, text="Добавить", command=self.save)
        btn.pack(side=tk.RIGHT)
        return btn

    def set_data_to_table(self, users):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i in users:
            self.tree.insert('', 'end',
                             values=(
                             i['id'], i['surname'], i['name'], i['patronymic'], i['phone'], i['email'], 'ПРАВКА',
                             'УДАЛИТЬ'))
