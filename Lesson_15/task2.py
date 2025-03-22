#Использование JOIN
#Используйте INNER JOIN для получения списка всех книг и
#их авторов.
#Используйте LEFT JOIN для получения списка всех авторов
#и их книг (включая авторов, у которых нет книг).
#Используйте RIGHT JOIN для получения списка всех книг и
#их авторов, включая книги, у которых автор не указан

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

    # INNER JOIN: Получение списка всех книг и их авторов
    print("\nСписок всех книг и их авторов (INNER JOIN):")
    cursor.execute('''
        SELECT books.title, authors.first_name, authors.last_name 
        FROM books
        INNER JOIN authors ON books.author_id = authors.id;
    ''')
    for row in cursor.fetchall():
        print(f"Книга: {row[0]}, Автор: {row[1]} {row[2]}")

    # LEFT JOIN: Список всех авторов и их книг (включая авторов без книг)
    print("\nСписок всех авторов и их книг (LEFT JOIN):")
    cursor.execute('''
        SELECT authors.first_name, authors.last_name, books.title 
        FROM authors
        LEFT JOIN books ON books.author_id = authors.id;
    ''')
    for row in cursor.fetchall():
        print(f"Автор: {row[0]} {row[1]}, Книга: {row[2] if row[2] else 'Нет книг'}")

    # RIGHT JOIN: Список всех книг и их авторов (включая книги без автора)
    print("\nСписок всех книг и их авторов (RIGHT JOIN):")
    cursor.execute('''
        SELECT books.title, authors.first_name, authors.last_name 
        FROM books
        RIGHT JOIN authors ON books.author_id = authors.id;
    ''')
    for row in cursor.fetchall():
        print(f"Книга: {row[0] if row[0] else 'Нет автора'}, Автор: {row[1]} {row[2]}")

except Exception as error:
    print("Ошибка при выполнении SQL-запросов:", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("\nСоединение с PostgreSQL закрыто.")