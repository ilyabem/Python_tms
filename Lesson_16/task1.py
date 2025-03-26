#Вариант 2 – Система управления инвентарем:
#Функционал:
#Определение таблиц для товаров, категорий, поставщиков и заказов на поставку
#Простые операции, такие как добавление/удаление/редактирование товаров/поставщиков/заказов/категорий, вывод информации о товаре/поставщике/заказе/категории по имени/названию
#Создание отчетов о состоянии склада и истории движения товаров
#Сложные операции, такие как поиск товара по категории, поиск товара/поставщика/whatever по частичному совпадению имени

import psycopg2

try:
    conn = psycopg2.connect(
        dbname="python_tms",
        user="admin",
        password="1111",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Удаляем таблицы, если они уже существуют, чтобы избежать конфликтов
    cursor.execute("DROP TABLE IF EXISTS orders CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS suppliers CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS products CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS categories CASCADE;")

    # создаем таблицу категории
    create_table_query = '''
        CREATE TABLE categories(  -- создаем таблицу
        id SERIAL PRIMARY KEY,    -- задаем уникальный номер(id)
        name VARCHAR(255) NOT NULL -- задаем имя категории
        );
    '''
    cursor.execute(create_table_query)

    # создаем таблицу продукты
    create_table_query = '''
        CREATE TABLE products(
        id SERIAL PRIMARY KEY, 
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10,2),            -- цена товара с точностью до двух знаков после запятой
        stock_quantity INT,             -- количество товара на складе
        category_id INT,                -- ссылка на категорию товара
        FOREIGN KEY (category_id) REFERENCES categories (id) -- связь с таблицей категорий
        );
    '''
    cursor.execute(create_table_query)  # вызываем execute один раз после создания таблицы products

    # создаем таблицу поставщики
    create_table_query = '''
        CREATE TABLE suppliers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        address TEXT,
        phone VARCHAR(20),
        email VARCHAR(255),
        contact_person VARCHAR(255)
        ); 
    '''
    cursor.execute(create_table_query)

    # создаем таблицу заказы
    create_table_query = '''
        CREATE TABLE orders(
        id SERIAL PRIMARY KEY,
        product_id INT NOT NULL,
        supplier_id INT NOT NULL,
        order_date DATE NOT NULL,
        quantity INT NOT NULL,
        status VARCHAR(50) DEFAULT 'Pending',
        FOREIGN KEY (product_id) REFERENCES products(id),
        FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
        );
    '''
    cursor.execute(create_table_query)

    # Добавляем тестовые категории товаров
    insert_query = '''
        INSERT INTO categories (name) VALUES 
        ('Электроника'),
        ('Одежда'),
        ('Продукты питания'),
        ('Канцелярия');
    '''
    cursor.execute(insert_query)

    # Добавляем тестовые товары
    insert_query = '''
        INSERT INTO products (name, category_id, price, stock_quantity)
        VALUES
        ('Мобильный телефон', 1, 700, 50),
        ('Картон', 2, 22, 1000),
        ('Степлер', 3, 100, 24);
    '''
    cursor.execute(insert_query)

    # Добавляем тестовых поставщиков
    insert_query = '''
        INSERT INTO suppliers (name, address, phone, email, contact_person)
        VALUES
        ('5 Элемент', 'ул.Пушкина, 5', '+375291234567', 'contact@5element.by', 'Сара Конор'),
        ('Добрушская бумажная фабрика', 'ул.Колотушкина 1', '+375337654321', 'info@paper.by', 'Сергей Бумажный'),
        ('Детский Мир', 'ул.Детская 4', '+375256780122', 'zakaz@detmir.by', 'Саша Степлер');
    '''
    cursor.execute(insert_query)

    # Добавляем тестовые заказы
    insert_query = '''
        INSERT INTO orders (product_id, supplier_id, order_date, quantity, status)
        VALUES
        (1, 1, '2025-03-28', 5, 'Pending'),
        (2, 2, '2025-03-22', 6, 'Completed'),
        (3, 3, '2025-03-20', 7, 'Canceled');
    '''
    cursor.execute(insert_query)

    conn.commit()
    print("Все таблицы созданы и тестовые данные добавлены успешно!")

except Exception as error:
    print(f"Ошибка при работе с PostgreSQL: {error}")
finally:
    if conn:
        cursor.close()
        conn.close()