import csv
import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.font as font

import docx
import pandas as pd

from tkcalendar import DateEntry

from dto.department_dto import DepartmentDto
from dto.reviews_dto import ReviewsDto
from dto.staff_dto import StaffDto


class ReviewsView:
    def __init__(self, frame):
        # Header
        self.root = frame
        self.search_block = tk.Frame(self.root)
        self.add_block = tk.Frame(self.root)
        button_frame = tk.Frame(self.root)
        self.init_heading()
        button_frame.pack()
        self.init_button_word(button_frame)
        self.init_button_excel(button_frame)
        self.init_button_report_by_staff(button_frame)
        self.search_employees_id_entry = self.init_employee_select(self.search_block, tk.LEFT)
        self.search_data_entry = self.init_date_entry(self.search_block, tk.LEFT)
        self.search_block.pack()
        search_button_frame = tk.Frame(self.root)
        self.init_search_button(search_button_frame)
        self.init_cancel_button(search_button_frame)
        search_button_frame.pack()

        # Table
        self.tree = self.init_table()
        reviews_dto = ReviewsDto()
        reviews = reviews_dto.select_reviews()
        self.set_data_to_table(reviews)

        # Add
        self.init_headingH2()
        self.department_select = self.init_department_select()
        self.staff_select = self.init_employee_select(self.add_block, tk.TOP)
        self.date_entry = self.init_date_entry(self.add_block, tk.TOP)
        self.add_block.pack()
        self.review_entry = self.init_review_entry()
        self.add_button = self.init_add_button()

        self.root.pack()

    def init_heading(self):
        label = ttk.Label(self.root, text='Таблица "Отзывы"', font=font.Font(size=40))
        label.pack()

    def init_button_word(self, frame):
        btn_cancel = ttk.Button(frame, text="Общий отчет Word", command=self.word)  # command=
        btn_cancel.pack(side=tk.LEFT)
        return btn_cancel

    def word(self):
        self.create_cvs_form_table('source.csv')
        doc = docx.Document()
        with open('source.csv', newline='') as f:
            csv_reader = csv.reader(f)

            csv_headers = next(csv_reader)
            csv_cols = len(csv_headers)

            table = doc.add_table(rows=1, cols=csv_cols, style='Table Grid')
            hdr_cells = table.rows[0].cells

            for i in range(csv_cols):
                hdr_cells[i].text = csv_headers[i]

            for row in csv_reader:
                row_cells = table.add_row().cells
                for i in range(csv_cols):
                    row_cells[i].text = row[i]

        doc.add_page_break()
        doc.save("Отзывы.docx")

    def init_button_excel(self, frame):
        btn_cancel = ttk.Button(frame, text="Общий отчет Excel", command=self.exel)  # command=
        btn_cancel.pack(padx=80, side=tk.LEFT)
        return btn_cancel

    def exel(self):
        self.create_cvs_form_table('source.csv')
        writer = pd.ExcelWriter('Отзывы.xlsx')
        df = pd.read_csv('source.csv')
        df.to_excel(writer, 'Отзывы', index=False)

        writer.save()

    def init_button_report_by_staff(self, frame):
        btn_cancel = ttk.Button(frame, text="Отчет по сотруднику", command=self.report_by_selected)
        btn_cancel.pack(side=tk.LEFT)
        return btn_cancel

    def report_by_selected(self):
        if self.tree.focus():
            selected_name = self.tree.item(self.tree.focus())['values'][2].split(' ')
            staff_id = StaffDto().select_staff_by_surname_name(selected_name[0], selected_name[1])[0]['id']
            all_reviews = ReviewsDto().select_by_id(staff_id)
            file_name = f'Отзыв {selected_name[0]} {selected_name[1]}.xlsx'
            lst = []
            cols = ['ID', 'Отдел', 'Отзыв', 'Дата']
            with open('source-staff-report.cvs', "w", newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=',')
                for row in all_reviews:
                    lst.append(row.values())
                lst = list(map(list, lst))
                lst.insert(0, cols)
                for row in lst:
                    csvwriter.writerow(row)
            writer = pd.ExcelWriter(file_name)
            df = pd.read_csv('source-staff-report.cvs')
            df.to_excel(writer, file_name, index=False)
            writer.save()

    def init_search_by_date(self):
        entry_frame = ttk.Frame(self.search_block)
        ttk.Label(entry_frame, text="Дата").pack(side=tk.LEFT)
        entry = ttk.Entry(entry_frame)
        entry.pack(side=tk.RIGHT)
        entry_frame.pack(padx=40, side=tk.RIGHT)
        return entry

    def search(self):
        staff_value = self.search_employees_id_entry.get().split(' ')
        date_value = self.search_data_entry.get().split('.')
        if staff_value[0] and date_value:
            reviews_dto = ReviewsDto()
            staff_id = StaffDto().select_staff_by_surname_name(staff_value[0], staff_value[1])[0]['id']
            date = datetime.date(int(date_value[2]), int(date_value[1]), int(date_value[0]))
            searched = reviews_dto.select_reviews_by_employees_id_date(staff_id, date)
            self.set_data_to_table(searched)

    def init_search_button(self, frame):
        btn = ttk.Button(frame, text="Поиск", command=self.search)
        btn.pack(side=tk.LEFT, padx=0)
        return btn

    def cancel(self):
        self.search_employees_id_entry.delete(0, 'end')
        self.search_data_entry.delete(0, 'end')
        reviews_dto = ReviewsDto()
        reviews = reviews_dto.select_reviews()
        self.set_data_to_table(reviews)

    def init_cancel_button(self, frame):
        btn_cancel = ttk.Button(frame, text="Отменить", command=self.cancel)
        btn_cancel.pack(side=tk.RIGHT)
        return btn_cancel

    def set_data_to_table(self, reviews):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i in reviews:
            date = i['date'].strftime('%d.%m.%Y')
            self.tree.insert('', 'end',
                             values=(i['id'], i['name'], i['surname']+' '+i['s.name'], i['review'], date, 'ПРАВКА', 'УДАЛИТЬ' ))

    def init_table(self):
        tree = ttk.Treeview(self.root, column=('ID', 'department_id', 'employee_id', 'review', 'date', 'edit', 'delete'), height=10,
                            show='headings')
        tree.bind('<ButtonRelease-1>', self.select_item)

        tree.column('ID', width=35, anchor=tk.CENTER)
        tree.column('department_id', anchor=tk.CENTER)
        tree.column('employee_id', anchor=tk.CENTER)
        tree.column('review', anchor=tk.CENTER)
        tree.column('date', anchor=tk.CENTER)
        tree.column('edit', anchor=tk.CENTER, width=75)
        tree.column('delete', anchor=tk.CENTER, width=75)

        tree.heading('ID', text='ID')
        tree.heading('department_id', text='Отдел')
        tree.heading('employee_id', text='Сотрудник')
        tree.heading('review', text='Отзыв')
        tree.heading('date', text='Дата')
        tree.heading('edit', text='Правка')
        tree.heading('delete', text='Удалить')
        tree.pack()
        return tree

    def select_item(self, event):
        cur_item = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)[1]
        method = cur_item['values'][int(col)-1]
        if method == 'УДАЛИТЬ':
            reviews_dto = ReviewsDto()
            reviews_dto.delete_by_id(cur_item['values'][0])
            self.set_data_to_table(reviews_dto.select_reviews())
        if method == 'ПРАВКА':
            self.staff_select.set(cur_item['values'][2])
            self.department_select.set(cur_item['values'][1])
            self.date_entry.set_date(cur_item['values'][4])
            self.review_entry.delete('1.0', tk.END)
            self.review_entry.insert('1.0', cur_item['values'][3])
            self.add_button.config(text='Править', command=lambda: self.update(cur_item['values'][0]))

    def update(self, id):
        reviews_dto = ReviewsDto()
        department_value = self.department_select.get()
        staff_value = self.staff_select.get().split(' ')
        date_value = self.date_entry.get().split('.')
        review_value = self.review_entry.get('1.0', tk.END)
        if department_value and staff_value and date_value and review_value:
            department_id = DepartmentDto().select_department_by_name(department_value)[0]['id']
            staff_id = StaffDto().select_staff_by_surname_name(staff_value[0], staff_value[1])[0]['id']
            date = datetime.date(int(date_value[2]), int(date_value[1]), int(date_value[0]))
            reviews_dto.update(id, department_id, staff_id, review_value, date)
        self.department_select.set('')
        self.staff_select.set('')
        self.review_entry.delete('1.0', tk.END)
        self.date_entry.set_date(datetime.datetime.today())
        self.add_button.config(text='Добавить', command=self.save_reviews)
        self.set_data_to_table(reviews_dto.select_reviews())


    def init_headingH2(self):
        label = ttk.Label(self.root, text='Добавить новый отзыв', font=font.Font(size=20))
        label.pack()

    def init_department_select(self):
        frame = tk.Frame(self.add_block)
        ttk.Label(frame, text='Отдел').pack()
        department_dto = DepartmentDto()
        entry = ttk.Combobox(frame, values=department_dto.select_department_name(), state="readonly")
        entry.pack(side=tk.RIGHT)
        frame.pack(side=tk.LEFT)
        return entry

    def init_employee_select(self, frame, label_side):
        frame = tk.Frame(frame)
        ttk.Label(frame, text='Сотрудник').pack(side=label_side)
        staff_dto = StaffDto()
        entry = ttk.Combobox(frame, values=staff_dto.select_name_and_surname(), state="readonly")
        entry.pack(side=tk.RIGHT)
        frame.pack(side=tk.LEFT)
        return entry

    def init_date_entry(self, frame, label_side):
        frame = tk.Frame(frame)
        ttk.Label(frame, text='Дата').pack(side=label_side)
        entry = DateEntry(frame, state="readonly", date_pattern='dd.MM.yyyy')
        entry.pack(side=tk.RIGHT)
        frame.pack(side=tk.LEFT)
        return entry

    def init_review_entry(self):
        frame = tk.Frame(self.root)
        ttk.Label(frame, text='Отзыв').pack()
        entry = tk.Text(frame, height=10)
        entry.pack(side=tk.RIGHT)
        frame.pack()
        return entry

    def init_add_button(self):
        button = tk.Button(self.root, text='Добавить', command=self.save_reviews)
        button.pack()
        return button

    def save_reviews(self):
        reviews_dto = ReviewsDto()
        department_value = self.department_select.get()
        staff_value = self.staff_select.get().split(' ')
        date_value = self.date_entry.get().split('.')
        review_value = self.review_entry.get("1.0", 'end-1c')
        if department_value and staff_value and date_value and review_value:
            department_id = DepartmentDto().select_department_by_name(department_value)[0]['id']
            staff_id = StaffDto().select_staff_by_surname_name(staff_value[0], staff_value[1])[0]['id']
            date = datetime.date(int(date_value[2]), int(date_value[1]), int(date_value[0]))
            reviews_dto.insert_reviews(department_id, staff_id, review_value, date)
        self.set_data_to_table(reviews_dto.select_reviews())

    def create_cvs_form_table(self, path):
        cols = ['ID', 'Отдел', 'Сотрудник', 'Отзыв', 'Дата']  # Your column headings here
        lst = []
        child = self.tree.get_children()
        with open(path, "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
            for row_id in child:
                row = self.tree.item(row_id, 'values')[:-2]
                lst.append(row)
            lst = list(map(list, lst))
            lst.insert(0, cols)
            for row in lst:
                csvwriter.writerow(row)
