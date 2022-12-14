import pymysql
from config import host, user, password, db_name


class DepartmentDto:
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
                create_table_query = "CREATE TABLE department (id int AUTO_INCREMENT," \
                                     "name varchar(32)," \
                                     "director varchar(32)," \
                                     "employees_count int(32)," \
                                     "workplace_count int(16), PRIMARY KEY (id));"
                cursor.execute(create_table_query)

        finally:
            connection.close()

    def insert_department(self, name, director, employees_count, workplace_count):
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
                insert_query = f'INSERT INTO department (`name`, `director`, `employees_count`, `workplace_count`) VALUES (%s, %s, %s, %s)'
                cursor.execute(insert_query, (name, director, employees_count, workplace_count))
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
                select_table_query = "SELECT * from department"
                cursor.execute(select_table_query)
                return cursor.fetchall()

        finally:
            connection.close()

    def select_department_name(self):
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
                select_table_query = "SELECT name from department"
                cursor.execute(select_table_query)
                ar = cursor.fetchall()
                return list(map(lambda x: x['name'], ar))

        finally:
            connection.close()

    def select_department_by_employees_count_workplace_count(self, employees_count, workplace_count):
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
                select_table_query = f'SELECT * from department WHERE employees_count=%s OR workplace_count=%s'
                cursor.execute(select_table_query, (employees_count, workplace_count))
                return cursor.fetchall()

        finally:
            connection.close()

    def select_department_by_name(self, name):
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
                select_table_query = f'SELECT * from department WHERE name=%s'
                cursor.execute(select_table_query, name)
                return cursor.fetchall()

        finally:
            connection.close()

    def delete_by_id(self, department_id):
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
                select_table_query = f'DELETE from department WHERE id=%s'
                cursor.execute(select_table_query, department_id)
                connection.commit()

        finally:
            connection.close()

    def update(self, department_id, name, director, employees_count, workplace_count):
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
                select_table_query = f'UPDATE department SET name=%s, director=%s, employees_count=%s, workplace_count=%s where id=%s'
                cursor.execute(select_table_query, (name, director, employees_count, workplace_count, department_id))
                connection.commit()

        finally:
            connection.close()