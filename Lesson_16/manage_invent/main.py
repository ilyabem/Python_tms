#В этом файле будет подключение к базе данных и вызовы функций из файла suppliers.py.

import psycopg2
from supplier_operations import delete_supplier_and_orders
from database import create_tables

def main():
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="python_tms",
        user="admin",
        password="1111",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Создание таблиц и тестовых данных
    create_tables()

    # Удаление поставщика с именем "5 Элемент" и связанных заказов
    delete_supplier_and_orders(conn, cursor, "5 Элемент")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()