import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from dto.reviews_dto import ReviewsDto

class ReviewsView:
    def __init__(self, frame):
        # Header
        self.root = frame
        self.search_block = tk.Frame(self.root)
        button_frame = tk.Frame(self.root)
        self.init_heading()
        button_frame.pack()
        self.init_button_word(button_frame)
        self.init_button_excel(button_frame)
        self.init_button_employees(button_frame)
        self.search_employees_id_entry = self.init_search_by_employees_id()
        self.search_data_entry = self.init_search_by_data()
        self.init_search_button(button_frame)
        self.init_cancel_button(button_frame)
        self.search_block.pack()

        # Table
        self.tree = self.init_table()
        reviews_dto = ReviewsDto()
        reviews = reviews_dto.select_reviews()
        self.set_data_to_table(reviews)
        self.init_headingH2()
        self.root.pack()

    def init_heading(self):
        label = ttk.Label(self.root, text='Таблица "Отзывы"', font=font.Font(size=40))
        label.pack()

    def init_button_word(self, frame):
        btn_cancel = ttk.Button(frame, text="Общий отчет Word") # command=
        btn_cancel.pack(side=tk.LEFT)
        return btn_cancel

    def init_button_excel(self, frame):
        btn_cancel = ttk.Button(frame, text="Общий отчет Excel") # command=
        btn_cancel.pack(padx=80, side=tk.LEFT)
        return btn_cancel

    def init_button_employees(self, frame):
        btn_cancel = ttk.Button(frame, text="Отчет по сотруднику") # command=
        btn_cancel.pack(side=tk.LEFT)
        return btn_cancel

    def init_search_by_employees_id(self):
        entry_frame = ttk.Frame(self.search_block)
        ttk.Label(entry_frame, text="Сотрудник").pack(side=tk.LEFT)
        entry = ttk.Entry(entry_frame)
        entry.pack(side=tk.RIGHT)
        entry_frame.pack(side=tk.LEFT)
        return entry

    def init_search_by_data(self):
        entry_frame = ttk.Frame(self.search_block)
        ttk.Label(entry_frame, text="Дата").pack(side=tk.LEFT)
        entry = ttk.Entry(entry_frame)
        entry.pack(side=tk.RIGHT)
        entry_frame.pack(padx=40, side=tk.RIGHT)
        return entry

    def search(self):
        employees_id = self.search_employees_id_entry.get()
        date = self.search_data_entry.get()
        reviews_dto = ReviewsDto()
        searched = reviews_dto.select_reviews_by_employees_id_date(employees_id, date)
        self.set_data_to_table(searched)

    def init_search_button(self, frame):
        btn = ttk.Button(frame, text="Поиск", command=self.search)
        btn.pack(side=tk.LEFT, padx=0)
        return btn

    def cancel(self):
        self.search_employees_id_entry.delete(0, 'end')
        self.search_data_entry.delete(0, 'end')
        user_dto = ReviewsDto()
        users = user_dto.select_reviews_by_employees_id_date()
        self.set_data_to_table(users)

    def init_cancel_button(self, frame):
        btn_cancel = ttk.Button(frame, text="Отменить", command=self.cancel)
        btn_cancel.pack(side=tk.RIGHT)
        return btn_cancel

    def set_data_to_table(self, reviews):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i in reviews:
            self.tree.insert('', 'end',
                             values=(i['id'], i['department_id'], i['employee_id'], i['review'], i['date']))

    def init_table(self):
        tree = ttk.Treeview(self.root, column=('ID', 'department_id', 'employee_id', 'review', 'date'), height=10,
                            show='headings')
        # tree.bind('<Double-1>', self.route)

        tree.column('ID', width=35, anchor=tk.CENTER)
        tree.column('department_id', anchor=tk.CENTER)
        tree.column('employee_id', anchor=tk.CENTER)
        tree.column('review', anchor=tk.CENTER)
        tree.column('date', anchor=tk.CENTER)

        tree.heading('ID', text='ID')
        tree.heading('department_id', text='Отдел')
        tree.heading('employee_id', text='Сотрудник')
        tree.heading('review', text='Отзыв')
        tree.heading('date', text='Дата')
        tree.pack()
        return tree

    def init_headingH2(self):
        label = ttk.Label(self.root, text='Добавить новый отзыв', font=font.Font(size=20))
        label.pack()