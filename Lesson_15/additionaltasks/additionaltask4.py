#Создайте таблицу orders для хранения информации о заказах. В таблице
#должны быть столбцы: id (первичный ключ), order_date (дата заказа), customer_id
#(внешний ключ на таблицу customers), total_amount (общая сумма заказа).

import psycopg2  # Импортируем библиотеку для работы с PostgreSQL

try:
    # Подключение к базе данных PostgreSQL
    conn = psycopg2.connect(
        dbname="python_tms",  # Имя базы данных
        user="admin",  # Имя пользователя PostgreSQL
        password="1111",  # Пароль для подключения
        host="localhost",  # Адрес сервера базы данных (локальный)
        port="5432"  # Порт PostgreSQL
    )
    cursor = conn.cursor()  # Создаем объект cursor для выполнения SQL-запросов

    # SQL-запрос для создания таблицы orders
    create_table_query = '''
    CREATE TABLE orders (
        id SERIAL PRIMARY KEY,                           -- Автоинкрементируемый первичный ключ
        order_date DATE NOT NULL,                        -- Дата заказа (тип DATE)
        customer_id INTEGER REFERENCES customers(id),    -- Внешний ключ на таблицу customers
        total_amount INT CHECK (total_amount >= 0)       -- Проверка: сумма заказа должна быть неотрицательной
    );
    '''

    cursor.execute(create_table_query)  # Выполняем SQL-запрос на создание таблицы
    conn.commit()  # Подтверждаем изменения

    print("Таблица 'orders' успешно создана!")  # Сообщение об успешном создании таблицы

except Exception as error:
    print("Ошибка подключения к PostgreSQL:", error)  # Выводим ошибку, если возникла

finally:
    if conn:
        cursor.close()  # Закрываем курсор
        conn.close()  # Закрываем соединение с PostgreSQL
        print("Соединение с PostgreSQL закрыто.")
