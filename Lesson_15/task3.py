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

    # INNER JOIN для получения списка всех книг, их авторов и продаж
    inner_join_query = '''
    SELECT authors.first_name, authors.last_name, books.title, sales.quantity
    FROM authors
    INNER JOIN books ON authors.id = books.author_id
    INNER JOIN sales ON books.id = sales.book_id;
    
    '''

    cursor.execute(inner_join_query)
    rows = cursor.fetchall()

    print("Список книг, их авторов и продаж (INNER JOIN):")
    for row in rows:
        print(f"{row[0]} {row[1]} - {row[2]}: {row[3]} продаж")

except Exception as error:
    print("Ошибка при подключении или выполнении SQL-запроса:", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто.")