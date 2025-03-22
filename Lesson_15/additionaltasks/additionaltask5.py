#Создайте таблицу customers, которая будет хранить информацию о
#клиентах. В таблице должны быть такие столбцы, как id (первичный ключ), name (имя
#клиента), email, phone_number, address.


import psycopg2

try:
    conn=psycopg2.connect(
        dbname = "python_tms",
        user = "admin",
        password = "1111",
        host = "localhost",
        port = "5432"
    )
    cursor = conn.cursor()
    create_table_query = '''
        CREATE TABLE customers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(50),
        phone_number VARCHAR(20),
        address VARCHAR(255)
        )
        '''
    cursor.execute(create_table_query)
    conn.commit()
    print("Таблица успешно создана")

except Exception as erorr:
    print("Ошибка подключения к Postgress:", erorr)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с Postgres закрыто.")
