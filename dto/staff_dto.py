import pymysql
from config import host, user, password, db_name


class StaffDto:
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
                create_table_query = "CREATE TABLE staff(id int AUTO_INCREMENT PRIMARY KEY," \
                                     "surname varchar(32)," \
                                     "name varchar(32)," \
                                     "patronymic varchar(32)," \
                                     "phone varchar(16) UNIQUE," \
                                     "email varchar (64) UNIQUE)"
                cursor.execute(create_table_query)
                print("Table created successfully")

        finally:
            connection.close()

    def insert_staff(self, surname, name, patronymic, phone, email):
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
                insert_query = f'INSERT INTO staff (`surname`, `name`, `patronymic`, `phone`, `email`) VALUES (%s, %s, %s, %s, %s)'
                cursor.execute(insert_query, (surname, name, patronymic, phone, email))
                connection.commit()

        finally:
            connection.close()

    def select_staff(self):
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
                select_table_query = "SELECT * from staff"
                cursor.execute(select_table_query)
                return cursor.fetchall()

        finally:
            connection.close()

    def select_name_and_surname(self):
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
                select_table_query = "SELECT name, surname from staff"
                cursor.execute(select_table_query)
                ar = cursor.fetchall()
                return list(map(lambda x: x['surname'] + ' ' + x['name'], ar))

        finally:
            connection.close()

    def select_staff_by_surname_name(self, surname, name):
        print(surname, name)
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
                select_table_query = f'SELECT * from staff WHERE surname=%s AND name=%s'
                cursor.execute(select_table_query, (surname, name))
                return cursor.fetchall()

        finally:
            connection.close()

    def delete_by_id(self, staff_id):
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
                select_table_query = f'DELETE from staff WHERE id=%s'
                cursor.execute(select_table_query, staff_id)
                connection.commit()

        finally:
            connection.close()

    def update(self, staff_id, surname, name, patronymic, phone, email):
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
                    select_table_query = f'UPDATE staff SET surname=%s, name=%s, patronymic=%s, phone=%s, email=%s where id=%s'
                    cursor.execute(select_table_query, (surname, name, patronymic, phone, email, staff_id))
                    connection.commit()

            finally:
                connection.close()