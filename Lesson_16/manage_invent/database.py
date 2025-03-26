#Файл для подключения к БД и создания таблиц

import psycopg2

def create_tables():
    try:
        conn = psycopg2.connect(
            dbname="python_tms",
            user="admin",
            password="1111",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Удаляем таблицы, если они уже существуют
        cursor.execute("DROP TABLE IF EXISTS orders CASCADE;")
        cursor.execute("DROP TABLE IF EXISTS suppliers CASCADE;")
        cursor.execute("DROP TABLE IF EXISTS products CASCADE;")
        cursor.execute("DROP TABLE IF EXISTS categories CASCADE;")

        # Создание таблиц
        cursor.execute('''CREATE TABLE categories (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);''')
        cursor.execute('''CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, price DECIMAL(10,2), 
                         stock_quantity INT, category_id INT, FOREIGN KEY (category_id) REFERENCES categories(id));''')
        cursor.execute('''CREATE TABLE suppliers (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, address TEXT, 
                         phone VARCHAR(20), email VARCHAR(255), contact_person VARCHAR(255));''')
        cursor.execute('''CREATE TABLE orders (id SERIAL PRIMARY KEY, product_id INT NOT NULL, supplier_id INT NOT NULL, 
                         order_date DATE NOT NULL, quantity INT NOT NULL, status VARCHAR(50) DEFAULT 'Pending', 
                         FOREIGN KEY (product_id) REFERENCES products(id), FOREIGN KEY (supplier_id) REFERENCES suppliers(id));''')

        # Добавление тестовых данных
        cursor.execute("INSERT INTO categories (name) VALUES ('Электроника'), ('Одежда'), ('Продукты питания'), ('Канцелярия');")
        cursor.execute("INSERT INTO products (name, category_id, price, stock_quantity) VALUES "
                       "('Мобильный телефон', 1, 700, 50), ('Картон', 2, 22, 1000), ('Степлер', 3, 100, 24);")
        cursor.execute("INSERT INTO suppliers (name, address, phone, email, contact_person) VALUES "
                       "('5 Элемент', 'ул.Пушкина, 5', '+375291234567', 'contact@5element.by', 'Сара Конор');")
        cursor.execute("INSERT INTO orders (product_id, supplier_id, order_date, quantity, status) VALUES "
                       "(1, 1, '2025-03-28', 5, 'Pending');")

        conn.commit()
        print("Таблицы созданы и тестовые данные добавлены успешно!")

    except Exception as error:
        print(f"Ошибка при создании таблиц: {error}")
    finally:
        if conn:
            cursor.close()
            conn.close()
