#Задача 1: Создайте таблицу employees, которая будет хранить информацию о
#сотрудниках компании. В таблице должны быть следующие столбцы: id (первичный
#ключ, автоинкремент), first_name (имя), last_name (фамилия), email, date_of_birth,
#date_of_hire (дата приема на работу).

import psycopg2  # Импортируем библиотеку psycopg2 для работы с PostgreSQL

# Попытка подключения к базе данных PostgreSQL
try:
    # Устанавливаем соединение с PostgreSQL
    conn = psycopg2.connect(
        dbname="python_tms",  # Имя базы данных, к которой подключаемся
        user="admin",  # Имя пользователя PostgreSQL
        password="1111",  # Пароль пользователя PostgreSQL
        host="localhost",  # Адрес сервера базы данных (локальный компьютер)
        port="5432"  # Порт, на котором работает PostgreSQL (по умолчанию 5432)
    )

    # Создаем курсор для выполнения SQL-запросов
    cursor = conn.cursor()

    # SQL-запрос для создания таблицы employees с нужными полями
    create_table_query = '''
    CREATE TABLE employees (
        id SERIAL PRIMARY KEY,           -- Поле id: автоинкрементируемый первичный ключ
        first_name VARCHAR(50) NOT NULL, -- Поле для имени сотрудника, обязательное, длина до 50 символов
        last_name VARCHAR(50) NOT NULL,  -- Поле для фамилии сотрудника, обязательное, длина до 50 символов
        email VARCHAR(100) UNIQUE NOT NULL, -- Поле для email с уникальным значением и обязательным заполнением
        date_of_birth DATE NOT NULL,     -- Поле для даты рождения сотрудника, обязательное
        date_of_hire DATE NOT NULL       -- Поле для даты приема на работу, обязательное
    );
    '''

    # Выполняем SQL-запрос на создание таблицы
    cursor.execute(create_table_query)

    # Подтверждаем изменения в базе данных (commit фиксирует изменения)
    conn.commit()

    # Сообщение о том, что таблица успешно создана
    print("Таблица 'employees' успешно создана!")

# Обрабатываем возможные ошибки при подключении или выполнении запроса
except Exception as error:
    print("Ошибка при подключении к PostgreSQL:", error)

# Код в блоке finally выполняется в любом случае (при успехе или ошибке)
finally:
    if conn:  # Проверяем, что соединение с базой данных было установлено
        cursor.close()  # Закрываем курсор
        conn.close()  # Закрываем соединение с базой данных
        print("Соединение с PostgreSQL закрыто.")