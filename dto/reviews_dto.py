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
                                     "date DATE," \
                                     "FOREIGN KEY (department_id) REFERENCES organization_personnel_management.department(id),"\
                                     "FOREIGN KEY (employee_id) REFERENCES organization_personnel_management.staff(id))"
                cursor.execute(create_table_query)
                print("Table created successfully")

        finally:
            connection.close()

    def insert_department(self, department, employee, date):
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
                insert_query = f'INSERT INTO reviews (`department`, `employee`, `date`) VALUES (%s, %s, %s)'
                cursor.execute(insert_query, (department, employee, date))
                connection.commit()

        finally:
            connection.close()

    def select_department(self):
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
                select_table_query = "SELECT * from reviews"
                cursor.execute(select_table_query)
                return cursor.fetchall()

        finally:
            connection.close()