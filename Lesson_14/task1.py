import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="python_tms",  # Имя вашей базы данных
    user="admin",      # Имя пользователя
    password="1111",      # Ваш пароль
    host="localhost",     # Адрес хоста
    port="5432"           # Порт PostgreSQL
)

# Создание таблицы пользователей
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
cur = conn.cursor()
# Вставка данных

cur.execute("""
    INSERT INTO users (username, email, password)
    VALUES ('test_user', 'test@example.com', 'securepassword')
    RETURNING id
""")
user_id = cur.fetchone()[0]
print(f"Добавлен пользователь с ID {user_id}")

# Выборка данных
cur.execute("SELECT * FROM users")
users = cur.fetchall()
for user in users:
    print(user)

# Подтверждение изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()