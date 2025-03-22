#Создайте таблицу products, которая будет содержать информацию о
#товарах. В таблице должны быть такие столбцы, как id (первичный ключ),
#product_name (название товара), price (цена), category (категория товара).

import psycopg2

try:
    conn = psycopg2.connect(
        dbname = "python_tms",
        user = "admin",
        password = "1111",
        host = "localhost",
        port = "5432"
        )
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE products (
        id SERIAL PRIMARY KEY,                -- Поле id: автоинкрементируемый первичный ключ
        product_name VARCHAR(100) NOT NULL,   -- Название товара (максимум 100 символов), обязательное поле
        price INT CHECK (price >= 0),         -- Цена товара, положительное целое число с проверкой
        category VARCHAR(50)                  -- Категория товара (максимум 50 символов)
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

    print("Таблица уже создана")

except Exception as error:
    print("Ошибка подключения к Postgress", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с Postgress закрыто.")