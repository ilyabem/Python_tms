#Создайте таблицу departments, в которой будут следующие столбцы: id
#(первичный ключ), department_name (название отдела), manager_id (идентификатор
#менеджера, внешний ключ на таблицу employees).


import psycopg2

# Подключение к PostgreSQL и создание таблицы departments
try:
    conn = psycopg2.connect(
        dbname="python_tms",  # Имя базы данных
        user="admin",  # Имя пользователя
        password="1111",  # Пароль
        host="localhost",  # Адрес хоста
        port="5432"  # Порт PostgreSQL
    )
    cursor = conn.cursor()

    # SQL-запрос для создания таблицы departments
    create_table_query = '''
    CREATE TABLE departments (
        id SERIAL PRIMARY KEY,                      -- Поле id: автоинкрементируемый первичный ключ
        department_name VARCHAR(100) NOT NULL,      -- Поле для названия отдела, обязательно для заполнения
        manager_id INTEGER REFERENCES employees(id) -- Внешний ключ, ссылающийся на поле id таблицы employees
    );
    '''

    # Выполнение SQL-запроса
    cursor.execute(create_table_query)
    conn.commit()  # Подтверждение изменений

    print("Таблица 'departments' успешно создана!")

except Exception as error:
    print("Ошибка при подключении к PostgreSQL:", error)

finally:
    if conn:
        cursor.close()  # Закрываем курсор
        conn.close()  # Закрываем соединение с PostgreSQL
        print("Соединение с PostgreSQL закрыто.")