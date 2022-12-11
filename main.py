import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.tree = ttk.Treeview(self, column=('ID', 'Surname', 'Name', 'Patronymic', 'Phone', 'Email'), height=10,
                                 show='headings')

        self.tree.column('ID', width=15, anchor=tk.CENTER)
        self.tree.column('Surname', width=60, anchor=tk.CENTER)
        self.tree.column('Name', width=60, anchor=tk.CENTER)
        self.tree.column('Patronymic', width=90, anchor=tk.CENTER)
        self.tree.column('Phone', width=90, anchor=tk.CENTER)
        self.tree.column('Email', width=120, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('Surname', text='Фамилия')
        self.tree.heading('Name', text='Имя')
        self.tree.heading('Patronymic', text='Отчество')
        self.tree.heading('Phone', text='Телефон')
        self.tree.heading('Email', text='Email')
        self.tree.pack()

        self.init_heading()
        self.surnameEntry = self.init_entry_surname()
        self.nameEntry = self.init_entry_name()
        self.patronymicEntry = self.init_entry_patronymic()
        self.phoneEntry = self.init_entry_phone()
        self.emailEntry = self.init_entry_email()
        self.button = self.init_button()



    def init_heading(self):
        label = ttk.Label(text='Таблица"Заголовки"', font=70)
        label.pack(pady=10)
        label = ttk.Label(text='Фамилия')
        label.pack(side=tk.LEFT)
        ttk.Entry().pack(pady=50)

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
        name = self.nameEntry.get()
        surname = self.surnameEntry.get()
        patronymic = self.patronymicEntry.get()
        phone = self.phoneEntry.get()
        email = self.emailEntry.get()
        print(f'{name} {surname} {patronymic} {phone} {email}')


    def init_button(self):
        btn = ttk.Button(text="Добавить", command=self.save)
        btn.place(relx=0.9, rely=0.8)
        return btn


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Управление персоналом организации")
    root.geometry("1650x1450")
    root.mainloop()