import psycopg2

try:
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="python_tms",
        user="admin",
        password="1111",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # LEFT JOIN для получения списка всех авторов, их книг и продаж
    left_join_query = '''
    SELECT authors.first_name, authors.last_name, books.title, sales.quantity
    FROM authors
    LEFT JOIN books ON authors.id = books.author_id
    LEFT JOIN sales ON books.id = sales.book_id;
    '''

    cursor.execute(left_join_query)
    rows = cursor.fetchall()

    print("Список авторов, их книг и продаж (LEFT JOIN):")
    for row in rows:
        print(f"{row[0]} {row[1]} - {row[2]}: {row[3]} продаж")

except Exception as error:
    print("Ошибка при подключении или выполнении SQL-запроса:", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто.")