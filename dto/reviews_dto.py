import pymysql
from config import host, user, password, db_name


class ReviewsDto:
    def create_table(self):
        connection = pymysql.connect(
            user=user,
            host=host,
            port=3306,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE reviews (" \
                                     "id int PRIMARY KEY AUTO_INCREMENT," \
                                     "department_id int," \
                                     "employee_id int," \
                                     "review varchar(256)," \
                                     "date DATE," \
                                     "FOREIGN KEY (department_id) REFERENCES organization_personnel_management.department(id),"\
                                     "FOREIGN KEY (employee_id) REFERENCES organization_personnel_management.staff(id))"
                cursor.execute(create_table_query)
                print("Table created successfully")

        finally:
            connection.close()

    def insert_reviews(self, department_id, employee_id, review, date):
        connection = pymysql.connect(
            user=user,
            host=host,
            port=3306,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                insert_query = f'INSERT INTO reviews (`department_id`, `employee_id`, `review`, `date`) VALUES (%s, %s, %s, %s)'
                cursor.execute(insert_query, (department_id, employee_id, review, date))
                connection.commit()

        finally:
            connection.close()

    def select_reviews(self):
        connection = pymysql.connect(
            user=user,
            host=host,
            port=3306,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                select_table_query = "select r.id, d.name, s.surname, s.name, date, review from reviews as r JOIN department d on r.department_id = d.id join staff s on r.employee_id = s.id"
                cursor.execute(select_table_query)
                return cursor.fetchall()

        finally:
            connection.close()

    def select_reviews_by_employees_id_date(self, employees_id, date):
        connection = pymysql.connect(
            user=user,
            host=host,
            port=3306,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                select_table_query = f'SELECT r.id, d.name, s.surname, s.name, date, review from reviews as r JOIN department d on d.id = r.department_id join staff s on s.id = r.employee_id WHERE employee_id=%s AND date=%s'
                cursor.execute(select_table_query, (employees_id, date))
                return cursor.fetchall()

        finally:
            connection.close()

    def delete_by_id(self, review_id):
        connection = pymysql.connect(
            user=user,
            host=host,
            port=3306,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                select_table_query = f'DELETE from reviews WHERE id=%s'
                cursor.execute(select_table_query, review_id)
                connection.commit()

        finally:
            connection.close()

    def update(self, review_id, department_id, staff_id, review_value, date):
        connection = pymysql.connect(
            user=user,
            host=host,
            port=3306,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                select_table_query = f'UPDATE reviews SET department_id=%s, employee_id=%s, date=%s, review=%s where id=%s'
                cursor.execute(select_table_query, (department_id, staff_id, date, review_value, review_id))
                connection.commit()

        finally:
            connection.close()