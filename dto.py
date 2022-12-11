import pymysql
from config import host, user, password, db_name
try:
    connection = pymysql.connect(
        user=user,
        host=host,
        port=3306,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('successfully connected...')
    print('#' * 20)

    try:
        with connection.cursor() as cursor:
            # insert_query = "INSERT INTO `staff` (Surname, Name, Patronymic, Phone, Email) VALUES ('Kuliev', 'Suleiman', 'Ibragimovich', '+71424431', 'getto_tawers@mail.ru')"
            # cursor.execute(insert_query)
            # connection.commit()

            select_table_query = "SELECT * from `staff`"
            cursor.execute(select_table_query)
            users = cursor.fetchall()
            print(users[0]["id"])
            total = cursor.rowcount
            print(total)

            # create_table_query = "CREATE TABLE `staff`(id int AUTO_INCREMENT," \
            #                      " Surname varchar(32)," \
            #                      " Name varchar(32)," \
            #                      " Patronymic varchar(32)," \
            #                      " Phone varchar(16)," \
            #                      " Email varchar (64), PRIMARY KEY (id));"
            # cursor.execute(create_table_query)
            # print("Table created successfully")
    finally:
        connection.close()

except Exception as ex:
    print('Connection refused')
    print(ex)