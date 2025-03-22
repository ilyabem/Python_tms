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

    # Создание таблиц authors, books и sales
    create_tables_query = '''
        CREATE TABLE authors (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50)
        );

        CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            author_id INT REFERENCES authors(id),
            publication_year INT
        );

        CREATE TABLE sales (
            id SERIAL PRIMARY KEY,
            book_id INT REFERENCES books(id),
            quantity INT
        );
    '''
    cursor.execute(create_tables_query)
    conn.commit()
    print("Таблицы authors, books и sales успешно созданы")

    # Вставка авторов
    authors_data = [
        ("Джордж", "Оруэлл"),
        ("Федор", "Достоевский"),
        ("Лев", "Толстой")
    ]
    cursor.executemany("INSERT INTO authors (first_name, last_name) VALUES (%s, %s)", authors_data)
    conn.commit()

    # Вставка книг
    books_data = [
        ("1984", 1, 1949),  # Джордж Оруэлл
        ("Преступление и наказание", 2, 1866),  # Федор Достоевский
        ("Война и мир", 3, 1869)  # Лев Толстой
    ]
    cursor.executemany("INSERT INTO books (title, author_id, publication_year) VALUES (%s, %s, %s)", books_data)
    conn.commit()

    # Вставка продаж
    sales_data = [
        (1, 150),  # 150 продаж книги "1984"
        (2, 200),  # 200 продаж книги "Преступление и наказание"
        (3, 300)  # 300 продаж книги "Война и мир"
    ]
    cursor.executemany("INSERT INTO sales (book_id, quantity) VALUES (%s, %s)", sales_data)
    conn.commit()

    print("Данные успешно добавлены в таблицы authors, books и sales")

except Exception as error:
    print("Ошибка при подключении или выполнении SQL-запросов:", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто.")